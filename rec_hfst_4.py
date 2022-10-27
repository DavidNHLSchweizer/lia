import math
import numpy as np
from lia import Axis
from line import Line
from plane import Plane
from transformations import AffineMatrix, AxisRotation, TranslationMatrix, axis_rotation_matrix, line_mirror_matrix, line_projection, line_projection_matrix, plane_mirror_matrix, rotation_matrix_2d

def vb_4_1_1():
    print(f'Voorbeeld 4.1.1 (factor: 5)\n{5*line_mirror_matrix(Line(-2,0))}')

def vb_4_2_1():
    print(f'Voorbeeld 4.2.1 (factor: 14)\n{14*plane_mirror_matrix(Plane(2,-1,3,0))}')

def vb_4_3():
    print('Voorbeelden hfst 4.3')
    print(f'Voorbeeld 4.3.1: T(v)={np.array([3,0]+ np.array([2,4]))}')
    print(f'Voorbeeld 4.3.2: T(v)={np.array([4,-1]-np.array([2,1]))}')

def vb_4_4():
    print('Voorbeelden hfst 4.4')
    print(f'Voorbeeld 4.4.1: T(v)={np.array([3,0,1]+ np.array([2,4,-1]))}')
    print(f'Voorbeeld 4.4.2: T(v)={np.array([4,-1,2]-np.array([2,1,0]))}')

def vb_4_5_1():
    print(f'Voorbeeld 4.5.1:\n{TranslationMatrix([3,-2])}')

# def _sin_cos_str(degrees):
#     return f'cos:{math.cos(math.radians(degrees)):.3f}   sin:{math.sin(math.radians(degrees)):.3f}'

def _cos_sin_str(degrees, cos_fac=1, sin_fac=1):
    a = cos_fac if cos_fac!=1 else ''
    b = sin_fac if sin_fac!=1 else ''
    return f'{a}cos:{cos_fac*math.cos(math.radians(degrees)):.3f}   {b}sin:{sin_fac*math.sin(math.radians(degrees)):.3f}'
def _cos_plus_sin_str(degrees, cos_fac=1, sin_fac=1):
    a = cos_fac if cos_fac!=1 else ''
    b = sin_fac if sin_fac!=1 else ''
    return f'{a}cos+{b}sin:{cos_fac*math.cos(math.radians(degrees))+sin_fac*math.sin(math.radians(degrees)):.3f}'

def vb_4_6_1():
    matrix = rotation_matrix_2d(32)
    print(f'Voorbeeld 4.6.1 ({_cos_sin_str(32)})\n{np.around(AffineMatrix(matrix).matrix,2)}')

def vb_4_7():
    print('Voorbeelden 4.7.1')
    matrix = TranslationMatrix([3,-2])
    print(f'Voorbeeld 4.7.1:\nmatrix=\n{matrix}\nafbeelding: {matrix.transform([4,6])}')
    matrix2 = AffineMatrix(rotation_matrix_2d(32))
    print(f'Voorbeeld 4.7.2:\nmatrix ({_cos_sin_str(32)})=\n{np.around(matrix2.matrix,2)}\nafbeelding ({_cos_plus_sin_str(32, 4, -6)}, {_cos_plus_sin_str(32, 6, 4)}): {np.around(matrix2.transform([4,6]),2)}')
    
def vb_4_8_1():
    print(f'Voorbeeld 4.8.1:\n{TranslationMatrix([3,-2,2])}')

def vb_4_9_1():
    matrix = AffineMatrix(plane_mirror_matrix(Plane(2,-1,3,0)))
    print(f'Voorbeeld 4.9.1 (factor: 14):\n{14*matrix.matrix}')

def vb_4_10():
    print('Voorbeelden 4.10')
    matrix = TranslationMatrix([3,-2,2])
    print(f'Voorbeeld 4.10.1\nmatrix\n{matrix}\nafbeelding:{matrix.transform([4,0,6])}')
    matrix2 = AffineMatrix(plane_mirror_matrix(Plane(2,-1,3,0)))
    print(f'Voorbeeld 4.10.2\nmatrix (factor: 14)\n{14*matrix2.matrix}\nafbeelding (factor: 14): {14*matrix2.transform([4,6,-1])}')

def vb_4_11_1():
    MR = rotation_matrix_2d(30)
    MS = line_mirror_matrix(Line(2,0))
    print(f'Voorbeeld 4.11.1\nrotatie-matrix ({_cos_sin_str(30)})\n{MR}\nspiegelmatrix (factor: 5)\n{5*MS}')
    MA1 = np.dot(MS,MR)
    print(f'eerst roteren dan spiegelen (factor: 5) [{_cos_plus_sin_str( 30, -3, 4)}, {_cos_plus_sin_str( 30, 4, 3)}], [{_cos_plus_sin_str( 30, 4, 3)}, {_cos_plus_sin_str( 30, 3, -4)}]\n{np.around(5*MA1,3)}\nzonder factor\n{np.around(MA1,2)}')
    MA2 = np.dot(MR,MS)
    print(f'eerst spiegelen dan roteren (factor: 5) [{_cos_plus_sin_str( 30, -3, -4)}, {_cos_plus_sin_str( 30, 4, -3)}], [{_cos_plus_sin_str( 30, 4, -3)}, {_cos_plus_sin_str( 30, 3, 4)}]\n{np.around(5*MA2,3)}\nzonder factor\n{np.around(MA2,2)}')

def vb_4_11_2():
    MR = axis_rotation_matrix(AxisRotation(Axis.x, 30))
    MS = plane_mirror_matrix(Plane(2,-1,3,0))
    print(f'Voorbeeld 4.11.2\nrotatie-matrix ({_cos_sin_str(30)})\n{MR}\nspiegelmatrix (factor: 14)\n{14*MS}')
    MA1 = np.dot(MS,MR)
    print(f'eerst roteren dan spiegelen (factor: 14) [{_cos_plus_sin_str( 30, 4, -12)}, {_cos_plus_sin_str( 30, -12, -4)}, [{_cos_plus_sin_str( 30, 12, 6)}, {_cos_plus_sin_str( 30, 6, -12)}], [{_cos_plus_sin_str( 30, 6, -4)}, {_cos_plus_sin_str( 30, -4, 6)}]\n{np.around(14*MA1,3)}\nzonder factor\n{np.around(MA1,2)}')
    MA2 = np.dot(MR,MS)
    print(f'eerst spiegelen dan roteren (factor: 14) [{_cos_plus_sin_str( 30, 4, 12)}, {_cos_plus_sin_str( 30, 12, -6)}, {_cos_plus_sin_str( 30, 6, 4)}], [{_cos_plus_sin_str( 30, -12, 4)},{_cos_plus_sin_str( 30, 6, 12)},{_cos_plus_sin_str( 30, -4, 6)}]\n{np.around(14*MA2,3)}\nzonder factor\n{np.around(MA2,2)}')

def vb_4_12_1():
    MTA = TranslationMatrix([3,-1])
    MRA = AffineMatrix(rotation_matrix_2d(30))
    print(f'Voorbeeld 4.12.1\nrotatie-matrix ({_cos_sin_str(30)})\n{np.around(MRA.matrix,3)}\ntranslatiematrix \n{MTA.matrix}')
    MA1 = MTA*MRA
    A1 = MA1.transform([2,-1])
    print(f'eerst roteren dan transleren \n{np.around(MA1.matrix,3)}\nafbeelding: {np.around(A1,2)}')
    MA2 = MRA*MTA
    A2 = MA2.transform([2,-1])
    print(f'eerst transleren dan roteren [{_cos_plus_sin_str( 30, 3, 1)}, {_cos_plus_sin_str( 30, -1, 3)}]\n{np.around(MA2.matrix,3)}\
        \nafbeelding: {np.around(A2,2)}\n')

def vb_4_12_2():
    MTA = TranslationMatrix([3,-1,1])
    MMA = AffineMatrix(plane_mirror_matrix(Plane(2,-1,3,0)))
    print(f'Voorbeeld 4.12.2\spiegel-matrix (factor: 14)\n{np.around(14*MMA.matrix,3)}\ntranslatiematrix \n{MTA.matrix}')
    MA1 = MTA*MMA
    A1 = MA1.transform([2,0,-1])
    print(f'eerst spiegeleren dan transleren (factor: 14)\n{np.around(14*MA1.matrix,3)}\nafbeelding (factor 14): {np.around(14*A1,2)}')
    MA2 = MMA*MTA
    A2 = MA2.transform([2,0,-1])
    print(f'eerst transleren dan spiegelen (factor: 14)\n{np.around(14*MA2.matrix,3)}\nafbeelding (factor 14): {np.around(14*A2,2)}')

def vb_hfst_4():
    vb_4_1_1()
    vb_4_2_1()
    vb_4_3()
    vb_4_4()
    vb_4_5_1()
    vb_4_6_1()
    vb_4_7()
    vb_4_8_1()
    vb_4_9_1()
    vb_4_10()
    vb_4_11_1()
    vb_4_11_2()
    vb_4_12_1()
    vb_4_12_2()

if __name__ == '__main__':
    print('*** VOORBEELDEN HOOFDSTUK 4 ***')
    vb_hfst_4()
    print('*** EINDE ***')
