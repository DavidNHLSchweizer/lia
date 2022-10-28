from __future__ import annotations
from enum import IntEnum
import math
import numpy as np
import pandas as pd

class QuaternionException(Exception):
    pass

class QuaternionUnit(IntEnum):
    R = 0
    i = 1
    j = 2
    k = 3
QU=QuaternionUnit

def quaternion_unit_str(qu: QuaternionUnit)->str:
    return '' if qu == QU.R else qu.name      


PRECISION = 1e-6
def is_almost_integer(value:float)->bool:
    return abs(round(value, 0)-value)<=PRECISION

def is_almost_zero(value:float)->bool:
    return is_almost_integer(value) and abs(round(value, 0))<=PRECISION
def is_almost_one(value:float)->bool:
    return is_almost_integer(value) and abs(1 - round(value, 0))<=PRECISION

class QuaternionElement:
#SUPPORT CLASS mainly for string display 
#also supports (basic) multiplication to generate QuaternionTable
    def __init__(self, value: float, unit: QuaternionUnit):
        self._value = value
        self._unit = unit
    @property
    def value(self): 
        return self._value
    @property
    def unit(self):
        return self._unit
    def __display_value(self, value, unit):
        if isinstance(value,float):
            if is_almost_integer(value):
                if is_almost_one(value) and unit is not QU.R:
                    return ''
                elif is_almost_one(-value) and unit is not QU.R:
                    return '-'
                else:
                    return str(round(value))
            else: 
                return f'{value:.03f}'.rstrip('0')
        elif isinstance(value, np.int32|int) and unit is not QU.R:
            if value == 1:
                return ''
            elif value == -1:
                return '-'
            else:
                return str(value)            
        else:
            return str(value)   
    def __str__(self):
        if is_almost_zero(self.value):
            return '0'
        else:
            return f'{self.__display_value(self.value, self.unit)}{quaternion_unit_str(self.unit)}'
    def __mul__(self, qe2: QuaternionElement)->QuaternionElement:
        multipliers=[[1,1,1,1], [1,-1,1,-1], [1,-1,-1,1], [1,1,-1,-1]]
        result_unit = [[QU.R, QU.i, QU.j, QU.k], [QU.i, QU.R, QU.k, QU.j], [QU.j, QU.k, QU.R, QU.i], [QU.k, QU.j, QU.i, QU.R]]
        return QuaternionElement(multipliers[self.unit][qe2.unit]*self.value*qe2.value, result_unit[self.unit][qe2.unit])

class Quaternion:
    def __init__(self, a:float,b:float,c:float,d:float):
        self._q = np.array([a,b,c,d])
    @property
    def w(self)->float:
        return self._q[QU.R]
    @property
    def x(self)->float:
        return self._q[QU.i]
    @property
    def y(self)->float:
        return self._q[QU.j]
    @property
    def z(self)->float:
        return self._q[QU.k]
    def conjugate(self)->Quaternion:
        return Quaternion(self.w,-self.x,-self.y,-self.z)
    def __str__(self):
        result = ''
        first = True
        for qu in QU:
            qe = QuaternionElement(self[qu], qu)
            qe_str = str(qe)
            if qe_str == '0':
                continue
            elif qe.value > 0:
                if not first:
                    result = result + '+' + qe_str
                else:
                    result = result + qe_str
            else:
                result = result + qe_str
            if len(result) > 0:
                first = False
        if not result:
            result = '0'
        return result
    def all_close(self, q2: Quaternion):
        return np.allclose(self._q, q2._q)
    def __eq__(self, q2: Quaternion)->bool:
        if not isinstance(q2, Quaternion):
            return False
        return np.array_equal(self._q, q2._q)
    def __add__(self, q2: Quaternion)->Quaternion:
        return Quaternion(self.w+q2.w,self.x+q2.x,self.y+q2.y,self.z+q2.z)
    def __sub__(self, q2: Quaternion)->Quaternion:
        return Quaternion(self.w-q2.w,self.x-q2.x,self.y-q2.y,self.z-q2.z)
    def __neg__(self)->Quaternion:
        return Quaternion(-self.w,-self.x,-self.y,-self.z)
    def __mul__(self,q2)->Quaternion:
        if isinstance(q2,Quaternion):
            return Quaternion(  self.w*q2.w - self.x*q2.x - self.y*q2.y - self.z*q2.z, 
                            self.x*q2.w + self.w*q2.x + self.y*q2.z - self.z*q2.y,
                            self.w*q2.y - self.x*q2.z + self.y*q2.w + self.z*q2.x,
                            self.w*q2.z + self.x*q2.y - self.y*q2.x + self.z*q2.w
                        )
        elif isinstance(q2,int|float):
            return Quaternion(q2*self.w, q2*self.x,q2*self.y,q2*self.z)
        else:
            return None
    def __rmul__(self,q2)->Quaternion:
        # to support left-multiplication with numbers
        if isinstance(q2,Quaternion):
            return q2*self
        elif isinstance(q2,int|float):
            return Quaternion(q2*self.w, q2*self.x,q2*self.y,q2*self.z)
        else:
            return None   
    def __getitem__(self,index_value):
        match(index_value):
            case 0: return self.w
            case 1: return self.x
            case 2: return self.y
            case 3: return self.z
            case _: raise QuaternionException('invalid index for quaternion')

class RotationQuaternion(Quaternion):
    def __init__(self, degrees: float, vector: list[float]):
        self.degrees = degrees
        self.vector=np.array(vector)
        self.unit_vector = self.vector / np.linalg.norm(self.vector)
        halftheta = math.radians(0.5 * degrees)
        sinhalftheta = math.sin(halftheta)
        super().__init__(math.cos(halftheta), sinhalftheta*self.unit_vector[0], sinhalftheta*self.unit_vector[1], sinhalftheta*self.unit_vector[2])

class PointQuaternion(Quaternion):
    def __init__(self, point: list[float]):
        super().__init__(0, point[0], point[1], point[2])
    def transform(self, rq: RotationQuaternion)->list[float]:
        return PointQuaternion.to_point(rq * self * rq.conjugate())
    @staticmethod
    def to_point(q: Quaternion)->list[float]:
        return [q[qu] for qu in [QU.i,QU.j,QU.k]]


class QuaternionTable(pd.DataFrame):
# presents quaternion multiplication as a (pandas) table/DataFrame
    def __init__(self, q1: Quaternion, q2: Quaternion, **kwargs):
        data=[]
        for qu1 in QU:
            row=[]
            for qu2 in QU:
                row.append(str(QuaternionElement(q1[qu1], qu1) * QuaternionElement(q2[qu2], qu2)))
            data.append(row)
        index = [str(QuaternionElement(q1[qu1], qu1)) for qu1 in QU]
        columns = [str(QuaternionElement(q2[qu2], qu2)) for qu2 in QU]
        super().__init__(data=data, index=index, columns=columns, **kwargs)    
        self.result = q1*q2
    