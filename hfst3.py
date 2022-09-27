import numpy as np
from line import VectorLine

from plane import Plane, PlaneConvertor
from transformations import Axis, axis_rotation_matrix, plane_projection_matrix

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

def _projectie_vlak(P: Plane, msg):
    print(f'{msg}\nTransformatiematrix:\n{plane_projection_matrix(P)}')

def _print_rotation_axis(axis, degrees, clockwise, check_value, msg):
    matrix = axis_rotation_matrix(axis, degrees, clockwise)
    print(f'{msg}\nTransformatiematrix:\n{matrix}\ncontrole: {np.dot(matrix, check_value)}')
   

def opgave3():
    _print_rotation_axis(Axis.x, 62, True, [0,0,2], 'opgave 3')

def opgave_3_extra():
    _print_rotation_axis(Axis.z, 4, True, [1,0,-2], 'opgave 3 extra')

def opgave4():
    _projectie_vlak(Plane(-3,1,0,0), 'opgave 4')

def opgave_4_extra():
    _print_rotation_axis(Axis.y, 42, False, [3,0,0], 'opgave 4 extra')

def opgave_5_extra():
    _print_rotation_axis(Axis.x, 126, False, [3,0,1], 'opgave 5 extra')

def opgave_6_extra():
    _projectie_vlak(Plane(-1,1,0,0), 'extra opgave 6')
def hfst3():
    print('HOOFDSTUK 3\n')
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

