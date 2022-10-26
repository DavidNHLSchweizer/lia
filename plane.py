from __future__ import annotations
from pickle import FALSE
import numpy as np
from lia import EPSILON, LAMBDA, MU, Axis, angle, PRECISION, vector_equivalent
from line import VectorLine

class PlaneInvalidException(Exception):
    pass
class Plane:
    def __init__(self, a, b, c, d: float):
        #ax + by + cz = d
        if a == 0 and b == 0 and c == 0:
            raise PlaneInvalidException(f'Invalid plane: a = b = c = 0')
        self._a = a        
        self._b = b
        self._c = c
        self._d = d
    @property
    def a(self)->float:
        return self._a
    @property
    def b(self)->float:
        return self._b
    @property
    def c(self)->float:   
        return self._c
    @property
    def d(self)->float:
        return self._d
    def __str__(self):
        return f'{self.a}x + {self.b}y + {self.c}z = {self.d}'
    def normal_vector(self):
        return np.array([self.a,self.b,self.c])
    def x(self, y: float, z: float)->float:
        if self.is_parallel(Axis.x):
            return None
        else:
            return (self.d - self.b*y - self.c*z) / self.a
    def y(self, x: float, z: float)->float:
        if self.is_parallel(Axis.y):
            return None
        else:
            return (self.d - self.a*x - self.c*z) / self.b
    def z(self, x: float, y: float)->float:
        if self.is_parallel(Axis.z):
            return None
        else:
            return (self.d - self.a*x - self.b*y) / self.c
    def is_parallel(self, axis: Axis):
        match axis:
            case Axis.x: return round(self.a,PRECISION) == 0
            case Axis.y: return round(self.b,PRECISION) == 0
            case Axis.z: return round(self.c,PRECISION) == 0
    def is_on_plane(self, x: float, y: float, z: float)->bool:
        return round(self.a*x+self.b*y+self.c*z - self.d, PRECISION) == 0
    '''
    Plane.equivalent
    A different plane is equivalent to this plane if the a,b,c and d (possibly multiplied with a constant) are equal withing compunting errors
    '''
    def equivalent(self, P: Plane)->bool:
        if P.a:
            scale = self.a / P.a
        elif P.b:
            scale = self.b / P.b
        elif P.c:
            scale = self.c / P.c
        else: 
            scale = 1 
        return abs(self.a - scale*P.a) < EPSILON and\
               abs(self.b - scale*P.b) < EPSILON and\
               abs(self.c - scale*P.c) < EPSILON and\
               abs(self.d - scale*P.d) < EPSILON

class VectorPlane:
    def __init__(self, P:list[float], R1:list[float], R2:list[float]):
        #V = P + λ.R1 + μ.R2
        if not (len(P) == 3 and len(R1) == 3 and len(R2) == 3):
            raise PlaneInvalidException(f'invalid plane vectors {P}, {R1} and/or {R2}')
        if np.linalg.norm(R1) == 0:
            raise PlaneInvalidException(f'invalid plane vector {R1}')
        if np.linalg.norm(R2) == 0:
            raise PlaneInvalidException(f'invalid plane vector {R1}')
        if round(angle(R1,R2),PRECISION) in [0, 180]:
            raise PlaneInvalidException(f'invalid plane {R1} and {R2} are parallel')
        self._P = P
        self._R1 = R1
        self._R2 = R2
    @property
    def P(self)->np.array:
        return self._P
    @property
    def R1(self)->np.array:
        return self._R1
    @property
    def R2(self)->np.array:
        return self._R2
    def __str__(self):
        return f'{self.P} + {LAMBDA}{self.R1} + {MU}{self.R2}'
    def normal_vector(self)->np.array:
        return np.cross(self.R1, self.R2)
    def V(self, labda: float, mu: float)->np.array:
        return np.array([self.P[i] + labda*self.R1[i] + mu*self.R2[i] for i in range(3)])    
    def is_on_plane(self, V: np.array)->bool:
        return self.solve(V) is not None         
    def is_parallel(self, axis: Axis):
        normal = self.normal_vector()
        match axis:
            case Axis.x: return round(normal[0],PRECISION) == 0
            case Axis.y: return round(normal[1],PRECISION) == 0
            case Axis.z: return round(normal[2],PRECISION) == 0
    def solve(self, V: np.array)->tuple(float,float):
        #find non-singular set of coordinates to solve against
        tries = [(0,1), (0,2), (1,2)]
        found = False
        for t1,t2 in tries:
            matrix = [[self.R1[t1], self.R2[t1]], [self.R1[t2], self.R2[t2]]]
            if np.linalg.det(matrix):
                found = True
                b = [V[t1]-self.P[t1], V[t2]-self.P[t2]]
                break
        if not found:
            return None               
        try:
            labda_mu = np.linalg.solve(matrix, b)
            if np.allclose(self.V(labda_mu[0], labda_mu[1]), V):
                return labda_mu
            else:
                return None
        except:
            return None               
    def line_intersection(self, VL: VectorLine)->np.array:
        matrix = np.array([[-VL.R[i], self.R1[i], self.R2[i]] for i in range(3)])
        try:
            solution = np.linalg.solve(matrix, np.array([VL.P[i]-self.P[i] for i in range(3)]))
            return VL.V(solution[0])
        except:
            return None
    '''
    equivalent
    A vectorplane VP2 is equivalent to this plane if it has the same (within computing errors) normal vector (possibly multiplied with a factor) 
    AND the point VP2.P is on this plane.
    '''
    def equivalent(self, VP2: VectorPlane)->bool:
        return vector_equivalent(self.normal_vector(), VP2.normal_vector()) and self.is_on_plane(VP2.P)

class PlaneConvertor:
    def vector_plane_from_plane(self, P: Plane)->VectorPlane:
        if not round(P.c,PRECISION) == 0:
            return VectorPlane([0,0,P.d/P.c], [1,0,-P.a/P.c], [0,1,-P.b/P.c])
        elif not round(P.b,PRECISION) == 0:
            return VectorPlane([0,P.d/P.b,0], [1,-P.a/P.b,0], [0,0,1])
        else:
            return VectorPlane([P.d/P.a,0,0], [0,1,0], [0,0,1])
    def plane_from_vector_plane(self, VP: VectorPlane)->Plane:
        normal = VP.normal_vector()
        return Plane(normal[0], normal[1], normal[2], np.inner(normal, VP.P))
    