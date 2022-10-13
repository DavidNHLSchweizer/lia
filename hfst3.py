import math
import numpy as np
from line import Line, VectorLine

from plane import Plane, PlaneConvertor
from transformations import Axis, axis_rotation_matrix, line_projection_matrix, plane_projection_matrix

def _projectie_vlak(P: Plane, msg, factor=1):
    print(f'{msg}\nTransformatiematrix:\n{factor*plane_projection_matrix(P)}')
def _print_rotation_axis(axis, degrees, clockwise, check_value, msg):
    matrix = axis_rotation_matrix(axis, degrees, clockwise)
    print(f'{msg}\nsin{degrees}={math.sin(math.radians(degrees)):.4f}, cos{degrees}={math.cos(math.radians(degrees)):.4f} Transformatiematrix:\n{np.round(matrix,4)}\ncontrole: {np.dot(matrix, check_value)}')

def vb_3_1():
    A = np.array([[3,-1,2],[4,-5,0]])
    B=np.array([[-4,5],[1,7],[-2,6]])
    print(f'Voorbeeld 3.1 (vermenigvuldiging):A=\n{A}\nB=\n{B}\nA.B\n{np.dot(A,B)}')
def vb_3_2():
    A = np.array([[3,-1,2],[4,-5,0]])
    B=np.array([[-4,5],[1,7],[-2,6]])
    print(f'Voorbeeld 3.2 (vermenigvuldiging/ABBA):A=\n{A}\nB=\n{B}\nB.A\n{np.dot(B,A)}\nA.B\n{np.dot(A,B)}')
def vb_3_3():
    A = np.array([[0,2,-1],[3,0,0], [1,1,1]])
    v = np.array([3,2,-1])
    print(f'Voorbeeld 3.3 (matrix-vector vermenigvuldiging):A=\n{A}\nv={v}\nA.v={np.dot(A,v)}')
def vb_3_4_1():
    cos60 = math.cos(math.radians(60))
    sin60 = math.sin(math.radians(60))
    print(f'Voorbeeld 3.4.1 (2d rotatie; cos60={cos60:.4f}  sin60={sin60:.4f}')
    R60 = np.array([[cos60,-sin60],[sin60,cos60]])
    print(f'matrix:\n{np.round(R60,4)}')
    print(f'afbeelding (4,2): {np.round(np.dot(R60,[4,2]),4)}')
def vb_3_5_1():
    matrix = line_projection_matrix(Line(1,0))
    print(f'Voorbeeld 3.5.1 (projectie op lijn y=x)\n{matrix}')
    matrix = line_projection_matrix(Line(4,0))
    print(f'Voorbeeld 3.5.1 (projectie op lijn y=4x, maal 17)\n{17*matrix}')
def vb_3_5_2():
    _projectie_vlak(Plane(2,-3,1,0), 'Voorbeeld 3.5.2 (projectie op vlak 2x-3y+z), maal 14', 14)

def hfst3_voorbeelden():
    vb_3_1()
    vb_3_2()
    vb_3_3()
    vb_3_4_1()
    vb_3_5_1()
    vb_3_5_2()
    

def _opgave1(M, msg):
    print(f'{msg}\ntransposed:\n{np.transpose(M)}')

def opgave1():
    _opgave1(np.array([[3,4,0,3],[2,0,7,-4],[-1,9,2,0]]),'opgave 1')

def _opgave2(M1, M2, M3, msg):
    print(f'{msg}\nproduct= \n{np.dot(np.dot(M1,M2), M3)}')

def opgave2():
    _opgave2(np.array([[3,0,2],[4,-1,1]]), np.array([[2,-1,-2],[1,3,1],[0,5,6]]), np.array([[1,2],[2,4],[-1,2]]), 'opgave 2')

def opgave1_extra():
    _opgave1(np.array([[2,5,-3,5],[1,0,4,0],[4,9,6,-1]]), 'extra opgave 1')

def opgave2_extra():
    _opgave2(np.array([[1,2],[2,4],[-1,2]]), np.array([[3,0,2],[4,-1,1]]), np.array([[2,-1,-2],[1,3,1],[0,5,6]]), 'extra opgave 2')


  

def opgave3():
    _print_rotation_axis(Axis.x, 62, True, [0,0,2], 'opgave 3')

def opgave_3_extra():
    _print_rotation_axis(Axis.z, 4, True, [1,0,-2], 'opgave 3 extra')

def opgave4():
    _projectie_vlak(Plane(-3,1,0,0), 'opgave 4 (maal 10)', 10)

def opgave_4_extra():
    _print_rotation_axis(Axis.y, 42, False, [3,0,0], 'opgave 4 extra')

def opgave_5_extra():
    _print_rotation_axis(Axis.x, 126, False, [3,0,1], 'opgave 5 extra')

def opgave_6_extra():
    _projectie_vlak(Plane(-1,1,0,0), 'extra opgave 6')
def hfst3():
    print('HOOFDSTUK 3\n')
    print('VOORBEELDEN')
    hfst3_voorbeelden()
    print('OPGAVEN')
    opgave1()
    opgave2()
    opgave3()
    opgave4()
    print('EXTRA OPGAVEN')
    opgave1_extra()
    opgave2_extra()
    opgave_3_extra()
    opgave_4_extra()
    opgave_5_extra()
    opgave_6_extra()
    print('*** EINDE ***')
    
if __name__ == '__main__':
    hfst3()

