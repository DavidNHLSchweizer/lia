from __future__ import annotations
import numpy as np
import math
lamda= '\u03BB'
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
    def is_on_line(self, x, y)->bool:
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
    def is_on_line(self, x, y)->bool:
        return x == self.b

class LineVector:
    #V = V1 + labda*V2
    def __init__(self, V1:list[float], V2:list[float]):
        if len(V1) != len(V2):
            raise LineInvalidException('dimension vectors not equal')
        self._V1 = np.array(V1)
        self._V2 = np.array(V2)
    def __str__(self):
        return f'V = {tuple(self.V1[i] for i in range(self.dim()))} + {lamda}{tuple(self.V2[i] for i in range(self.dim()))}'
    def dim(self):
        return len(self._V1)
    @property
    def V1(self)->np.array:
        return self._V1
    @property
    def V2(self)->np.array:
        return self._V2
    def V(self, labda)->np.array:
        return np.array([self.V1[i] + labda*self.V2[i] for i in range(self.dim())])
    def labda(self, V)->float:
        for i in range(self.dim()):
            if self.V2[i] != 0:
                lab = (V[i] - self.V1[i]) / self.V2[i]
                if np.allclose(V, self.V(lab)):
                    return lab
        return None
    def is_on_line(self, V)->bool:
        return self.labda(V) is not None
    def angle(self, LV2: LineVector, degrees = True)->float:
        angle_in_radians = math.acos((np.inner(self.V2,LV2.V2)/(np.linalg.norm(self.V2)*np.linalg.norm(LV2.V2))))
        return angle_in_radians if not degrees else angle_in_radians * 180 / math.pi

class LineConvertor:    
    def vector_from_line(self, l: Line)->LineVector:
        if isinstance(l, VerticalLine):
            return LineVector([l.b, 0], [0, 1])
        elif l.a == 0:
            return LineVector([0,l.b], [1,0])
        else:
            return LineVector([-l.b/l.a,0], [1,l.a])
    def line_from_vector(self, LV: LineVector)->Line:
        if LV.V2[0] == 0:
            return VerticalLine(LV.V1[0])
        else:
            a = LV.V2[1] / LV.V2[0]
            b = LV.V1[1] - LV.V1[0]*LV.V2[1] / LV.V2[0]
            return Line(a,b)
