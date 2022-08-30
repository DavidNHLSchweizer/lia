from __future__ import annotations
import numpy as np
from lia import LAMBDA, angle, PRECISION

class LineInvalidException(Exception):
    pass

class LineBase:
    def __init__(self, a, b: float):
        self._a = a
        self._b = b
    @property
    def a(self)->float:
        return self._a
    @property
    def b(self)->float:
        return self._b
    def y(self, x: float)->float:
        return None
    def x(self, y: float)->float:
        return None
    def is_on_line(self, x, y)->bool:
        return False
class Line(LineBase):
    #y = ax+b    
    def __str__(self):
        return f'y = {self.a}x + {self.b}'
    def y(self, x: float)->float:
        return self.a * x + self.b
    def x(self, y: float)->float:
        if self.a == 0:
            raise LineInvalidException('horizontal line')
        return (y-self.b)/self.a
    def is_on_line(self, x: float, y: float)->bool:
        return self.y(x) == y 
class VerticalLine(LineBase):
    #x = b    
    def __init__(self, b: float):
        super().__init__(None, b)
    def __str__(self):
        return f'x = {self.b}'
    def y(self, x: float)->float:
        raise LineInvalidException('vertical line')
    def x(self, y: float)->float:
        return self.b
    def is_on_line(self, x: float, y: float)->bool:
        return x == self.b

class LineVector:
    #V = P + λ.R
    def __init__(self, P:list[float], R:list[float]):
        if len(P) != len(R):
            raise LineInvalidException('dimension vectors not equal')
        if round(np.linalg.norm(R), PRECISION) == 0:
            raise LineInvalidException(f'invalid line vector {R}')
        self._P = np.array(P)
        self._R = np.array(R)
    def __str__(self):
        return f'V = {tuple(self.P[i] for i in range(self.dim()))} + {LAMBDA}{tuple(self.R[i] for i in range(self.dim()))}'
    def dim(self):
        return len(self._P)
    @property
    def P(self)->np.array:
        return self._P
    @property
    def R(self)->np.array:
        return self._R
    def V(self, labda)->np.array:
        return np.array([self.P[i] + labda*self.R[i] for i in range(self.dim())])
    def labda(self, V)->float:
        for i in range(self.dim()):
            if self.R[i] != 0:
                lab = (V[i] - self.P[i]) / self.R[i]
                if np.allclose(V, self.V(lab)):
                    return lab
        return None
    def is_on_line(self, V)->bool:
        return self.labda(V) is not None
    def angle(self, LV2: LineVector, degrees = True)->float:
        return angle(self.R, LV2.R, degrees)
    def normal_vector(self)->np.array:
        if self.R[1] == 0:
            return np.array([0,1])
        else:
            return np.array([1,-self.R[0]/self.R[1]])

class LineConvertor:    
    def vector_from_line(self, l: Line)->LineVector:
        if isinstance(l, VerticalLine):
            return LineVector([l.b, 0], [0, 1])
        elif l.a == 0:
            return LineVector([0,l.b], [1,0])
        else:
            return LineVector([-l.b/l.a,0], [1,l.a])
    def line_from_vector(self, LV: LineVector)->LineBase:
        if LV.R[0] == 0:
            return VerticalLine(LV.P[0])
        else:
            a = LV.R[1] / LV.R[0]
            b = LV.P[1] - LV.P[0]*LV.R[1] / LV.R[0]
            return Line(a,b)
