import math
import cmath
import numpy as np
import pandas as pd
from line import Line, LineConvertor, VectorLine
from plane import Plane, VectorPlane
from quaternion import PointQuaternion, Quaternion, QuaternionTable, RotationQuaternion

def vb_6_2_1():
    print('Voorbeelden 6.2.1:')
    C1 = complex(3,4)
    C2 = complex(-1,2)
    print(f'\tC1+C2 = {C1+C2}')
    print(f'\tC1-C2 = {C1-C2}')
    C1b = complex(0,4)
    print(f'\t{C1b} + {C2} = {C1b+C2}')
    print(f'\t{C1b} - {C2} = {C1b-C2}')
    print(f'\t4 + {C2} = {4+C2}')
    print(f'\t4 - {C2} = {4-C2}')

def vb_6_3_1():
    print('Voorbeeld 6.3.1:')
    C1 = complex(3,4)
    C2 = complex(-1,2)
    print(f'\tC1*C2 = {C1*C2}')

def _vb_6_5_1(q, msg):
    print(f'\t{msg}: q={q}  q*={q.conjugate()}')
def vb_6_5_1():
    print(f'Voorbeeld 6.5.1:')
    _vb_6_5_1(Quaternion(1,2,-1,3), 'q1')
    _vb_6_5_1(Quaternion(0,2,-1,3), 'q2')

def vb_6_6_1():
    print('Voorbeeld 6.6.1')
    q1 = Quaternion(1,2,3,4)
    q2 = Quaternion(2,4,-1,-1)
    print(f'\t{q1}\t+\t{q2}\t= {q1+q2}')
    print(f'\t{q1}\t-\t{q2}\t= {q1-q2}')
    q1b=Quaternion(0,2,0,4)
    print(f'\t{q1b}\t+\t{q2}\t= {q1b+q2}')
    print(f'\t{q1b}\t-\t{q2}\t= {q1b-q2}')


def vb_6_8_1():
    q1 = Quaternion(1,2,-1,3)
    q2 = Quaternion(2,1,-2,4)
    print(f'Voorbeeld 6.8.1: {q1} * {q2} = {q1*q2}')


   
def _quaternion_rotatie(q1, q2, msg, check_result, check_table):
    result = q1*q2
    qt = QuaternionTable(q1, q2)
    print(f'{msg}: ({q1}) * ({q2})\nresultaat {result}  (check: {check_result})\ntable:\n{qt}')
    if check_table is not None:
        print(f'\ncheck:\n{check_table}')
    return result

def vb_6_9_1():
    _quaternion_rotatie(Quaternion(1,2,-1,3),  Quaternion(2,1,-2,4), 'Voorbeeld 6.9.1', Quaternion(-14,7,-9,7), None)#, np.array([[2, "i", "-2j", "4k"], ["4i",-2, "-4i"]

def __cs_str(func, degrees, fac=1):
    a = fac if fac!=1 else ''
    return f'{a}{func.__name__}{degrees}:{fac*func(math.radians(degrees)):.3f}' 

def _cos_str(degrees, fac=1):
    return __cs_str(math.cos, degrees, fac)

def _sin_str(degrees, fac=1):
    return __cs_str(math.sin, degrees, fac)

def vb_6_10_1():
    rq = RotationQuaternion(64, [3,4,0])
    print(f'Voorbeeld 6.10.1: {rq} ({_cos_str(32)}  {_sin_str(32,3/5)}  {_sin_str(32,4/5)})')

def vb_6_11_1():
    pq = PointQuaternion([1,0,-2])
    print(f'Voorbeeld 6.11.1:\n\t(1): {pq}\t(2):{PointQuaternion.to_point(Quaternion(0,4,-2,0))}')

def voorbeeld_6_12_1():
    p=PointQuaternion([-2,3,6])
    qr = RotationQuaternion(80, [-1,2,2])
    cos40=math.cos(math.radians(40))
    sin40=math.sin(math.radians(40))
    coscos40 = cos40*cos40
    sinsin40 = sin40*sin40
    sincos40 = sin40*cos40
    print('Voorbeeld 6-12-1')
    tem = _quaternion_rotatie(p, qr.conjugate(), 'pqr*', Quaternion(20/3*sin40, -2*cos40+2*sin40, 3*cos40+2/3*sin40, 6*cos40+1/3*sin40),
                              pd.DataFrame( [['0','0','0','0'],
                                    [f'{-2*cos40:.3f}i', f'{2/3*sin40:.3f}', f'{4/3*sin40:.3f}k', f'{-4/3*sin40:.3f}j'],
                                    [f'{3*cos40:.3f}j', f'{-sin40:.3f}k', f'{2*sin40:.3f}', f'{-2*sin40:.3f}i'],
                                    [f'{6*cos40:.3f}k', f'{2*sin40:.3f}j', f'{4*sin40:.3f}i', f'{4*sin40:.3f}']],
                                    columns = [f'{cos40:.3f}', f'{1/3*sin40:.3f}i', f'{-2/3*sin40:.3f}j', f'{-2/3*sin40:.3f}k'], index = ['0', '-2i', '3j', '6k']
                                    ))
    
    _quaternion_rotatie(qr, tem, 'qr(pqr*)', Quaternion(0,-22/9*sinsin40+4*sincos40-2*coscos40,53/9*sinsin40+4/3*sincos40+3*coscos40,26/9*sinsin40+2/3*sincos40+6*coscos40), 
                              pd.DataFrame( [[f'{20/3*sincos40:.3f}', f'{(-2*coscos40+2*sincos40):.3f}i', f'{(3*coscos40+2/3*sincos40):.3f}j', f'{(6*coscos40+1/3*sincos40):.3f}k'],
                                    [f'{-20/9*sinsin40:.3f}i', f'{-2/3*sincos40+2/3*sinsin40:.3f}', f'{-(sincos40+2/9*sinsin40):.3f}k', f'{2*sincos40+1/9*sinsin40:.3f}j'],
                                    [f'{40/9*sinsin40:.3f}j',  f'{4/3*sincos40-4/3*sinsin40:.3f}k', f'{-(2*sincos40+4/9*sinsin40):.3f}', f'{4*sincos40+2/9*sinsin40:.3f}i'],
                                    [f'{40/9*sinsin40:.3f}k',  f'{-4/3*sincos40+4/3*sinsin40:.3f}j', f'{-(2*sincos40+4/9*sinsin40):.3f}i', f'{-4*sincos40-2/9*sinsin40:.3f}']],
                                    columns = [f'{20/3*sin40:.3f}', f'{(-2*cos40 + 2* sin40):.3f}i', f'{(3*cos40 + 2/3* sin40):.3f}j', f'{(6*cos40 + 1/3* sin40):.3f}k'], 
                                    index = [f'{cos40:.3f}', f'{-1/3*sin40:.3f}i', f'{2/3*sin40:.3f}j', f'{2/3*sin40:.3f}k']
                                    ))
    print(f'EINDRESULTAAT is dus {np.around(PointQuaternion.to_point(qr*tem),3)}')    

def vb_hfst_6():
    vb_6_2_1()
    vb_6_3_1()
    vb_6_5_1()
    vb_6_6_1()
    vb_6_8_1()
    vb_6_9_1()
    vb_6_10_1()
    vb_6_11_1()
    voorbeeld_6_12_1()

if __name__ == '__main__':
    print('*** VOORBEELDEN HOOFDSTUK 6 ***')
    vb_hfst_6()
    print('*** EINDE ***')
