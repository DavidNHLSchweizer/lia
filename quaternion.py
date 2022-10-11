from __future__ import annotations
from enum import IntEnum
import math
import numpy as np
import pandas as pd

class QuaternionUnit(IntEnum):
    R = 0
    i = 1
    j = 2
    k = 3
QU=QuaternionUnit

PRECISION = 1e-6
def is_almost_integer(value:float)->bool:
    return abs(round(value, 0)-value)<=PRECISION

def is_almost_zero(value:float)->bool:
    return is_almost_integer(value) and abs(round(value, 0))<=PRECISION

def quaternion_unit(qu: QuaternionUnit)->str:
    return '' if qu == QU.R else qu.name      

def quaternion_string(value: float, qu: QuaternionUnit)->str:
    def display_value(value):
        if isinstance(value,float):
            if is_almost_integer(value):
                return str(round(value))
            else: 
                return f'{value:.3f}'
        else:
            return str(value)   
    return f'{display_value(value)}{quaternion_unit(qu)}'

def quaternion_multiplication_str(q1: Quaternion, q2: Quaternion, qu1: QuaternionUnit, qu2: QuaternionUnit)->str:
    result_index= [[QU.R, QU.i, QU.j, QU.k],
                   [QU.i, QU.R, QU.k, QU.j],
                   [QU.j, QU.k, QU.R, QU.i],
                   [QU.k, QU.j, QU.i, QU.R]]
    multipliers=[[1,1,1,1], [1,-1,1,-1], [1,-1,-1,1], [1,1,-1,-1]]
    return quaternion_string(multipliers[qu1][qu2] * q1[qu1] * q2[qu2], result_index[qu1][qu2])


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
        def join_value(value, qu, first)->str:
            plusmin=['-', '+']
            if is_almost_zero(value):
                return ''            
            elif first:
                return quaternion_string(value,qu)
            else:
                return f' {plusmin[value>=0]} ' + quaternion_string(abs(value),qu)
        result = ''
        first = True
        for qu in QU:
            result = result + join_value(self[qu],qu,first)
            if len(result) > 0:
                first = False
        return result
    def __repr__(self):
        return '+'.join(quaternion_string(self[i],i) for i in range(4))
    def __add__(self, q2: Quaternion)->Quaternion:
        return Quaternion(self.w+q2.w,self.x+q2.x,self.y+q2.y,self.z+q2.z)
    def __sub__(self, q2: Quaternion)->Quaternion:
        return Quaternion(self.w-q2.w,self.x-q2.x,self.y-q2.y,self.z-q2.z)
    def __neg__(self)->Quaternion:
        return Quaternion(-self.w,-self.x,-self.y,-self.z)
    def __mul__(self,q2: Quaternion)->Quaternion:
        return Quaternion(  self.w*q2.w - self.x*q2.x - self.y*q2.y - self.z*q2.z, 
                            self.x*q2.w + self.w*q2.x + self.y*q2.z - self.z*q2.y,
                            self.w*q2.y - self.x*q2.z + self.y*q2.w + self.z*q2.x,
                            self.w*q2.z + self.x*q2.y - self.y*q2.x + self.z*q2.w
                        )
    def __getitem__(self,index_value):
        match(index_value):
            case 0: return self.w
            case 1: return self.x
            case 2: return self.y
            case 3: return self.z
        return None

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
        p_qrT = self * rq.conjugate()
        qr_p_qrT = rq * p_qrT 
        return [qr_p_qrT[qu] for qu in [QU.i,QU.j,QU.k]]

class QuaternionTable:
    def __init__(self, q1: Quaternion, q2: Quaternion):
        self.table  = self._create_table(q1,q2)
    def __str__(self):
        return str(self.table)
    def _create_table(self, q1: Quaternion, q2: Quaternion)->pd.DataFrame:
        data=[]
        for qu1 in QU:
            row=[]
            for qu2 in QU:
                row.append(quaternion_multiplication_str(q1, q2, qu1, qu2))
            data.append(row)
        index = [quaternion_string(q1[qu],qu) for qu in QU]
        columns = [quaternion_string(q2[qu],qu) for qu in QU]
        return pd.DataFrame(data=data, index=index, columns=columns)
