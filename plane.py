import numpy as np
from lia import lamda, mu, angle, PRECISION

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
        if round(self.a,PRECISION) == 0:
            return None
        else:
            return (self.d - self.b*y - self.c*z) / self.a
    def y(self, x: float, z: float)->float:
        if round(self.b,PRECISION) == 0:
            return None
        else:
            return (self.d - self.a*x - self.c*z) / self.b
    def z(self, x: float, y: float)->float:
        if round(self.c,PRECISION) == 0:
            return None
        else:
            return (self.d - self.a*x - self.b*y) / self.c
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
        return f'{self.P} + {lamda}{self.R1} + {mu}{self.R2}'
    def normal_vector(self)->np.array:
        return np.cross(self.R1, self.R2)
    def V(self, labda: float, mu: float)->np.array:
        return np.array([self.P[i] + labda*self.R1[i] + mu*self.R2[i] for i in range(3)])
    def as_matrix(self)->np.array:
        return [[]]

class PlaneConvertor:
    def plane_vector_from_plane(self, P: Plane)->PlaneVector:
        if not round(P.c,PRECISION) == 0:
            return PlaneVector([0,0,P.d/P.c], [1,0,-P.a/P.c], [0,1,-P.b/P.c])
        elif not round(P.b,PRECISION) == 0:
            return PlaneVector([0,P.d/P.b,0], [1,-P.a/P.b,0], [0,0,1])
        else:
            return PlaneVector([P.d/P.a,0,0], [0,1,0], [0,0,1])

    def plane_from_plane_vector(self, PV: PlaneVector)->Plane:
        matrix = PV.as_matrix()
    

# PC=PlaneConvertor()
# P = Plane(-1, 2, -2, 6)
# PV = PC.plane_vector_from_plane(P)
# print(PV)

# def plm(PV, l, m):
#     print(f'{lamda}:{l} {mu}:{m} \t{PV.V(l,m)}')    
# P = Plane(2, 3, 0, 5)
# PV = PC.plane_vector_from_plane(P)
# print(PV)
# plm(PV, 0,0)
# plm(PV, 1,0)
# plm(PV, 0, 1)
# plm(PV, .5,.5)
# plm(PV, 1, 1)
