import math
import numpy as np
from lia import ROOT
from quaternion import PointQuaternion, Quaternion, QuaternionTable, RotationQuaternion

def _multiply(q1:Quaternion, q2:Quaternion, msg, savefile=None):
    result = q1*q2
    print(f'{msg}: {result}')
    qt = QuaternionTable(q1,q2)
    print(qt)
    if savefile:
        qt.table.to_excel(savefile)
    return result

def vb_6_2_1():
    _multiply(Quaternion(6,3,-5,2),Quaternion(2,1,4,-2), 'Voorbeeld 6.2.1 (Rekenschema)')

def vb_6_4():
    qr = Quaternion(0,0,2,-1)
    p = PointQuaternion([3,0,1])
    print(f'Voorbeeld 6.4 (rotatie)\tpoint quaternion is {p}    rotatie quaternion is {qr}, geconjugeerd is {qr.conjugate()}')
    intermediate_q =_multiply(p,qr.conjugate(),'p_qr* is')
    _multiply(qr, intermediate_q, 'qr_p_qr* is')
    print(f'beeld van P: {np.round(p.transform(qr),2)}')

    qr = RotationQuaternion(180, [-3,0,4])
    p = PointQuaternion([-1,-1,0])
    print(f'\nTweede voorbeeld 6.4  (rotatie)\tunit vector is {qr.unit_vector}     point quaternion is {p}    rotatie quaternion is {qr}, geconjugeerd is {qr.conjugate()}')
    intermediate_q =_multiply(p,qr.conjugate(),'p_qr* is')
    _multiply(qr, intermediate_q, 'qr_p_qr* is')
    print(f'beeld van P: {np.round(p.transform(qr),2)}')

def hfst6_voorbeelden():
    vb_6_2_1()
    vb_6_4()

def _opgave1_2(msg, point, angle, vector, factor=1.0):
    p = PointQuaternion(point)
    q = RotationQuaternion(angle, vector)
    print(f'{msg}:\n\tpuntquaterion is {p}\n\tunit vector is {"1/"+str(factor) if not factor==1.0 else ""}{factor*q.unit_vector}, rotatiequaternion(geconjugeerd) is {q.conjugate()}')

def opgave1():
    _opgave1_2('Opgave 1', [-2,2,9], 84,[-4,0,3])
    sin42=math.sin(math.radians(42))
    print(f'NOTE: cos(42) = {math.cos(math.radians(42)):.3f}   4/5sin(42)= {.8*sin42:.3f}   3/5sin(42)= {.6*sin42:.3f}')
def opgave2():
    _opgave1_2('Opgave 2', [23,-15,7], 42,[6,-6,7], 11)
    sin21=math.sin(math.radians(21))
    print(f'NOTE: cos(21) = {math.cos(math.radians(21)):.3f}   6/11sin(21)= {6.*sin21/11:.3f}   7/11sin(21)= {7.*sin21/11:.3f}')
def opgave3():
    _multiply(Quaternion(0,2,-4,5), Quaternion(7,2,1,0), 'Opgave 3')
def opgave4():
    _multiply(Quaternion(-16,-2,3,2), Quaternion(-1,4,0,2), 'Opgave 4')
def opgave5():
    qr = RotationQuaternion(60,[-3,0,0])
    p = PointQuaternion([-2,0,5])
    print(f'Opgave 5:\nunit vector is {qr.unit_vector}   point quaternion is {p}   rotatie quaternion is {qr}, geconjugeerd is {qr.conjugate()}')
    cos30 = math.cos(math.radians(30))
    print(f'NOTE: cos(30) = {cos30:.3f}, 2cos(30) = {2*cos30:.3f}, 2.5cos(30) = {2.5*cos30:.3f}, 5cos(30) = {5*cos30:.3f}')
    intermediate_q =_multiply(qr,p, 'qr_p is')
    _multiply(intermediate_q, qr.conjugate(), 'qr_p_qr* is')
    print(f'beeld van P: {np.round(p.transform(qr),2)}')

def hfst6_opgaven():
    opgave1()
    opgave2()
    opgave3()
    opgave4()
    opgave5()

def opgave1_extra():
    _opgave1_2('Extra opgave 1', [2,2,0], 42, [4,-2,4], 6)
    sin21=math.sin(math.radians(21))
    print(f'NOTE: cos(21) = {math.cos(math.radians(21)):.3f}   2/3sin(21)= {2.*sin21/3:.3f}   1/3sin(21)= {1.*sin21/3:.3f}')
def opgave2_extra():
    _opgave1_2('Extra opgave 2', [6,2,-3], 84,[-12,12,6], 18)
    sin42=math.sin(math.radians(42))
    print(f'NOTE: cos(42) = {math.cos(math.radians(42)):.3f}   2/3sin(42)= {2.*sin42/3:.3f}   1/3sin(42)= {1.*sin42/3:.3f}')
def opgave3_extra():
    _multiply(Quaternion(3,0,2,-1), Quaternion(0,2,3,3), 'Extra opgave 3')
def opgave4_extra():
    qr = RotationQuaternion(60,[0,7,0])
    p = PointQuaternion([-2,0,0])
    print(f'Extra opgave 4:\nunit vector is {qr.unit_vector}  point quaternion is {p}    rotatie quaternion is {qr}, geconjugeerd is {qr.conjugate()}')
    cos30 = math.cos(math.radians(30))
    print(f'NOTE: cos(30) = {cos30:.3f}, 2cos(30) = {2*cos30:.3f}, 2.5cos(30) = {2.5*cos30:.3f}, 5cos(30) = {5*cos30:.3f}')
    intermediate_q =_multiply(qr,p, 'qr_p is')
    _multiply(intermediate_q, qr.conjugate(), 'qr_p_qr* is')
    print(f'beeld van P: {np.round(p.transform(qr),2)}')


def hfst6_extra():
    opgave1_extra()
    opgave2_extra()
    opgave3_extra()
    opgave4_extra()

def hfst6():
    print('HOOFDSTUK 6\n')
    print('VOORBEELDEN')
    hfst6_voorbeelden()
    print('OPGAVEN')
    hfst6_opgaven()
    print('EXTRA OPGAVEN')
    hfst6_extra()
    print('*** EINDE ***')

if __name__=='__main__':
    hfst6()