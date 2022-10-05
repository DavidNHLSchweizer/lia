from __future__ import annotations
import numpy as np
import quaternion
import pandas as pd

def quaternion_string(value: float, index: int)->str:
    suffixes=['','i','j','k']
    if index>=0 and index < 4:
        return f'{value:.3f}{suffixes[index]}'
    return None

def quaternion_multiplication_str(q1: Quaternion, q2: Quaternion, index1, index2)->str:
    result_index= [[0, 1, 2, 3],
                   [1, 0, 3, 2],
                   [2, 3, 0, 1],
                   [3, 2, 1, 0]]
    multipliers=[[1,1,1,1], [1,-1,1,-1], [1,-1,-1,1], [1,1,-1,-1]]
    return quaternion_string(multipliers[index1][index2] * q1[index1] * q2[index2], result_index[index1][index2])

class Quaternion:
    def __init__(self, a:float,b:float,c:float,d:float):
        self._q = np.quaternion(a,b,c,d)
    @property
    def w(self)->float:
        return self._q.w
    @property
    def x(self)->float:
        return self._q.x
    @property
    def y(self)->float:
        return self._q.y
    @property
    def z(self)->float:
        return self._q.z
    def conjugate(self)->Quaternion:
        return Quaternion(self.w,-self.x,-self.y,-self.z)
    def __str__(self):
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

class QuaternionTable:
    def __init__(self,q1: Quaternion, q2: Quaternion):
        self._q1 = q1
        self._q2 = q2
        self.table  = self._create_table()
    def _create_table(self)->pd.DataFrame:
        index=self.__as_strings(self._q1)
        columns = self.__as_strings(self._q2)
        data=[]
        for i in range(4):
            row=[]
            for j in range(4):
                row.append(quaternion_multiplication_str(self._q1, self._q2, i, j))
            data.append(row)
        return pd.DataFrame(data=data, index=index, columns=columns)
    def __table_value(self, i1:int,i2:int)->str:
        value = self._q1[i1]*self._q2[i2]
        return quaternion_string(value,1)
    def __as_strings(self,q: Quaternion)->list[str]:
        return [quaternion_string(q[i],i) for i in range(4)]
        


q1 = Quaternion(1,2,3,4)
q2=Quaternion(-1,2,-1,3)
# print(f'q1={q1} q2={q2}\nconj: {q1.conjugate()}  {q2.conjugate()} \nsum: {q1+q2} \nsub: {q1-q2}')
# print(f'neg: {-q1}   {-q2}')
# print(f'mult: {q1*q2}')

a=Quaternion(0,2,-4,5)
b=Quaternion(7,2,1,0)
QT=QuaternionTable(a,b)
print(QT.table)
print(a*b)

c=Quaternion(-16,-2,3,2)
d=Quaternion(-1,0,4,2)
# 
# print([c[i] for i in range(4)])

QT=QuaternionTable(c,d)
print(QT.table)
print(c*d)