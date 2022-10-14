import math
import numpy as np
from line import Line

from plane import Plane
from transformations import AffineMatrix, Axis, TranslationMatrix, axis_rotation_matrix, line_projection_matrix, plane_mirror_matrix, plane_projection_matrix

def _print_affine_translation(vector, msg):
    print(f'{msg}  affiene matrix:\n{TranslationMatrix(vector)}')

def _print_mirror_matrix(plane: Plane, msg, factor=1):
    print(f'{msg}   matrix:\n{factor*plane_mirror_matrix(plane)}')


def opgave1():
    _print_affine_translation(np.array([5,-2]-np.array([3,2])), 'Opgave 1')
def opgave2():
    _print_mirror_matrix(Plane(1,-3,0,0), 'Opgave 2')
def opgave3():
    T3 = TranslationMatrix(np.array([3,-2])-np.array([5,2]))
    cos62=math.cos(math.radians(62))
    sin62=math.sin(math.radians(62))
    Ra = AffineMatrix(np.array([[cos62,sin62],[-sin62,cos62]]))
    print(f'Opgave 3    sin{62}={sin62:.3f} cos{62}={cos62:.3f}  T3a=\n{T3}   \nRa=\n{np.round(Ra.matrix, 4)}\nmatrix\n{np.round((T3*Ra).matrix,4)}')
def opgave4():
    T4 = TranslationMatrix(np.array([2,-1,4])-np.array([-1,0,3]))
    Sa = AffineMatrix(np.array([[2,-1,2],[0,-1,2],[-2,-3,-1]])/6)
    print(f'Opgave 4   T4a=\n{T4}   \nSa(*6)=\n{np.round(6*Sa.matrix, 4)}\nmatrix(*6)\n{np.round(6*(Sa*T4).matrix,4)}')
    
def opgave1_extra():
    _print_mirror_matrix(Plane(-2,1,0,0), 'Extra Opgave 1')
def opgave2_extra():
    _print_mirror_matrix(Plane(0,1,3,0), 'Extra Opgave 2', 10)
def opgave3_extra():
    _print_affine_translation(np.array([0,1,6])-np.array([5,1,2]), 'Extra Opgave 3')
def opgave4_extra():
    _print_affine_translation(np.array([6,2,-2])-np.array([9,0,-1]), 'Extra Opgave 4')
def opgave5_extra():
    S2a = AffineMatrix(plane_mirror_matrix(Plane(-2,1,0,0)))
    T1 = TranslationMatrix(np.array([0,1,6])-np.array([5,1,2]))
    S3a = AffineMatrix(plane_mirror_matrix(Plane(0,1,3,0)))
    print(f'ExtraOpgave 5\nS2a(*5)=\n{5*S2a.matrix}   \nT1=\n{T1}\nS3a(*5)\n{np.round(5*S3a.matrix,4)}')
    print(f'A (*25):\n{np.round(25*(S3a*T1*S2a).matrix, 4)}')

def vb_4_1_1():
    M = line_projection_matrix(Line(4,0))
    print(f'Voorbeeld 4.1.1 (spiegeling in lijn y=4x)\nmatrix projectie (*17):\n{17*M}')
    P_10= np.dot(M,[1,0])
    print(f'basis vector [1,0]: projectie*17 {17*P_10}  spiegeling*17 {17*(2*P_10-np.array([1,0]))}')
    P_01= np.dot(M,[0,1])
    print(f'basis vector [0,1]: projectie*17 {17*P_01}  spiegeling*17 {17*(2*P_01-np.array([0,1]))}')

def vb_4_1_2():
    M = plane_projection_matrix(Plane(2,-3,1,0))
    M2 = plane_mirror_matrix(Plane(2,-3,1,0))
    print(f'Voorbeeld 4.1.2 (spiegeling in vlak 2x-3y+z=0)\nmatrix projectie (*14):\n{14*M}\nmatrix spiegeling (*7)\n{7*M2}')

def vb_4_3_1():
    R = np.array([[1,-1],[1,1]])
    P = np.array([[0.5,0.5],[0.5,0.5]])
    print(f'Voorbeeld 4.3.1:\nP*R=\n{np.dot(P,R)}\nR*P=\n{np.dot(R,P)}')
def vb_4_3_2():
    Ta = TranslationMatrix([4,-3])
    Ra = AffineMatrix(np.array([[1,-1],[1,1]]))
    Sa = AffineMatrix(np.array([[0,1],[1,0]]))
    print(f'Voorbeeld 4.3.2: Ra*Ta*Sa=\n{np.dot(Ra,np.dot(Ta,Sa))}')
def vb_4_3_3():
    Ta = TranslationMatrix([4,-3,2])
    Ra = AffineMatrix(np.array([[1,-1,0],[1,1,-1],[0,-1,1]]))
    Pa = AffineMatrix(np.array([[0,1,0],[1,0,0],[0,0,1]]))
    RaTaPa=np.dot(Ra,np.dot(Ta,Pa))
    print(f'Voorbeeld 4.3.3: Ra*Ta*Pa=\n{RaTaPa}\ntransform [1,1,1]: {RaTaPa.transform([1,1,1])}\ntransform [1,0,0]: {RaTaPa.transform([1,0,0])}\ntransform [0,0,1]: {RaTaPa.transform([0,0,1])}')

def hfst4_voorbeelden():
    vb_4_1_1()
    vb_4_1_2()
    vb_4_3_1()
    vb_4_3_2()
    vb_4_3_3()
    
def hfst4_opgaven():
    opgave1()
    opgave2()
    opgave3()
    opgave4()
def hfst4_extra():
    opgave1_extra()
    opgave2_extra()
    opgave3_extra()
    opgave4_extra()
    opgave5_extra()
    
def hfst4():
    print('HOOFDSTUK 4\n')
    print('VOORBEELDEN')    
    hfst4_voorbeelden()
    print('OPGAVEN')
    hfst4_opgaven()
    print('EXTRA OPGAVEN')
    hfst4_extra()
    print('*** EINDE ***')
    
if __name__ == '__main__':
    hfst4()

