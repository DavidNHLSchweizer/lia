import numpy as np

class Plane:
    def __init__(self, a, b, c, d: float):
        #ax + by + cz = d
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
        return np.array([self.a,self.b, self.c])

p = Plane(1,2,3,42)
print(p)
print(p.normal_vector())