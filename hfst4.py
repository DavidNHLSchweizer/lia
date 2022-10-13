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



def hfst4_voorbeelden():
    pass
    # vb_3_1()
    # vb_3_2()
    # vb_3_3()
    # vb_3_4_1()
    # vb_3_5_1()
    # vb_3_5_2()
    
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
    print('dit moet ik nog controleren!')
    hfst4_voorbeelden()
    print('OPGAVEN')
    hfst4_opgaven()
    print('EXTRA OPGAVEN')
    hfst4_extra()
    print('*** EINDE ***')
    
if __name__ == '__main__':
    hfst4()

