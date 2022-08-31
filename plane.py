from __future__ import annotations
import numpy as np
from lia import LAMBDA, MU, angle, PRECISION
from line import LineVector

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
        if self.is_parallel_x():
            return None
        else:
            return (self.d - self.b*y - self.c*z) / self.a
    def y(self, x: float, z: float)->float:
        if self.is_parallel_y():
            return None
        else:
            return (self.d - self.a*x - self.c*z) / self.b
    def z(self, x: float, y: float)->float:
        if self.is_parallel_z():
            return None
        else:
            return (self.d - self.a*x - self.b*y) / self.c
    def is_parallel_x(self):
        return round(self.a,PRECISION) == 0
    def is_parallel_y(self):
        return round(self.b,PRECISION) == 0
    def is_parallel_z(self):
        return round(self.c,PRECISION) == 0
    def is_on_plane(self, x: float, y: float, z: float)->bool:
        return round(self.a*x+self.b*y+self.c*z - self.d, PRECISION) == 0
    
class PlaneVector:
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
    def solve(self, V: np.array)->tuple(float,float):
        matrix = np.array([[self.P[i], self.R1[i], self.R2[i]] for i in range(3)])
        solution = np.linalg.solve(matrix, np.array([V[i] for i in range(3)]))
        if round(solution[0], PRECISION) == 0:
            return None
        solution = solution/solution[0]
        if np.allclose(np.dot(matrix,solution), V):
            return (solution[1], solution[2])
        else:
            return None
    def line_intersection(self, LV: LineVector)->np.array:
        matrix = np.array([[-LV.R[i], self.R1[i], self.R2[i]] for i in range(3)])
        solution = np.linalg.solve(matrix, np.array([LV.P[i]-self.P[i] for i in range(3)]))
        return LV.V(solution[0])


class PlaneConvertor:
    def plane_vector_from_plane(self, P: Plane)->PlaneVector:
        if not round(P.c,PRECISION) == 0:
            return PlaneVector([0,0,P.d/P.c], [1,0,-P.a/P.c], [0,1,-P.b/P.c])
        elif not round(P.b,PRECISION) == 0:
            return PlaneVector([0,P.d/P.b,0], [1,-P.a/P.b,0], [0,0,1])
        else:
            return PlaneVector([P.d/P.a,0,0], [0,1,0], [0,0,1])
    def plane_from_plane_vector(self, PV: PlaneVector)->Plane:
        normal = PV.normal_vector()
        return Plane(normal[0], normal[1], normal[2], np.inner(normal, PV.P))
    
