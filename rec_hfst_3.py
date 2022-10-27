import math
import numpy as np
from lia import Axis
from line import Line
from plane import Plane
from transformations import AxisRotation, axis_rotation_matrix, line_projection_matrix, plane_projection_matrix, rotation_matrix_2d

def _print_matrix(M, msg):
    print(f'{msg}\n{M}')

def vb_3_1_1():
    A = np.array([[3,1,0], [-1,2,3], [2,1,-1],[0,2,1]])
    B = np.array([[-2,0,2], [2,-1.5,2], [4,-2,1],[7,1,-1]])
    print('Voorbeeld 3.1.1:\n')
    _print_matrix(A+B, 'A+B')
    _print_matrix(A-B, 'A-B')

def _vb_3_1_2(M, msg):
    _print_matrix(np.transpose(M), msg)

def vb_3_1_2():
    print('Voorbeelden 3.1.2:\n')
    _vb_3_1_2(np.array([[1,2], [3,4]]), 'Voorbeeld 1')
    _vb_3_1_2(np.array([[1,2,3], [4,5,6], [7,8,9]]), 'Voorbeeld 2')
    _vb_3_1_2(np.array([[1,2,3], [4,5,6]]), 'Voorbeeld 3')
    _vb_3_1_2(np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]), 'Voorbeeld 4')
    
def _mat_mul(A,B, msg):
    _print_matrix(np.dot(A,B), msg)

def vb_3_3():
    print('Voorbeelden 3.3:')
    _mat_mul(np.array([[1,2], [3,4]]), np.array([[5,7], [6,8]]), 'Voorbeeld 3.3.1')
    _mat_mul(np.array([[1,2,3], [4,5,6]]), np.array([[1,-1], [2,-2],[3,-3]]), 'Voorbeeld 3.3.2')
    _mat_mul(np.array([[1,-1], [2,-2],[3,-3]]), np.array([[1,2,3], [4,5,6]]), 'Voorbeeld 3.3.3')

def vb_3_4():
    print('Voorbeelden 3.4:')
    _mat_mul(np.array([[1,2], [3,4]]), np.array([5,6]), 'Voorbeeld 3.4.1')
    _mat_mul(np.array([[1,2,3],[4,5,6],[7,8,9]]), np.array([-1,0,-2]), 'Voorbeeld 3.4.2')
    _mat_mul(np.array([[1,2,3],[4,5,6]]), np.array([-1,0,-2]), 'Voorbeeld 3.4.3')

def __sin_cos_str(degrees):
    return f'cos:{math.cos(math.radians(degrees)):.3f}   sin:{math.sin(math.radians(degrees)):.3f}'

def _rotation_matrix2D(degrees, clockwise, msg):
    matrix = rotation_matrix_2d(degrees, clockwise)
    print(f'{msg} ({__sin_cos_str(degrees)})\n{np.around(matrix,2)}')

def vb_3_5():
    print('Voorbeelden 3.5')
    _rotation_matrix2D(32, False, 'Voorbeeld 3.5.3')
    _rotation_matrix2D(-42, False, 'Voorbeeld 3.5.4')

def _rotation_axis3D(axis, degrees, clockwise, msg):
    matrix = axis_rotation_matrix(AxisRotation(axis, degrees, clockwise))
    print(f'{msg} ({__sin_cos_str(degrees)})\n{np.around(matrix,2)}')

def vb_3_6():
    print('Voorbeelden 3.6')
    _rotation_axis3D(Axis.y, 42, False, 'Voorbeeld 3.6.4')
    _rotation_axis3D(Axis.z, 36, False, 'Voorbeeld 3.6.5')
    _rotation_axis3D(Axis.x, 21, True, 'Voorbeeld 3.6.6')

def vb_3_9_1():
    print(f'Voorbeeld 3.9.1 (factor: 5)\n{5*line_projection_matrix(Line(2,0))}')

def vb_3_11_1():
    print(f'Voorbeeld 3.11.1 (factor: 14)\n{14*plane_projection_matrix(Plane(2,-1,3,0))}')

def vb_hfst_3():
    vb_3_1_1()
    vb_3_1_2()
    vb_3_3()
    vb_3_4()
    vb_3_5()
    vb_3_6()
    vb_3_9_1()
    vb_3_11_1()

if __name__ == '__main__':
    print('*** VOORBEELDEN HOOFDSTUK 3 ***')
    vb_hfst_3()
    print('*** EINDE ***')
