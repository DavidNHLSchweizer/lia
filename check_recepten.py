import math
import numpy as np
from line import Line, LineConvertor
from plane import Plane
from transformations import Axis, axis_rotation_matrix, line_projection_matrix, plane_mirror_matrix, plane_projection_matrix

def _print_projectie_line(L: Line, msg, factor=1):
    print(f'{msg}\nTransformatiematrix projectie:\n{factor*line_projection_matrix(L)}')

def _print_projectie_vlak(P: Plane, msg, factor=1):
    print(f'{msg}\nTransformatiematrix projectie:\n{factor*plane_projection_matrix(P)}')

def _print_rotation_axis(axis, degrees, clockwise, msg):
    matrix = axis_rotation_matrix(axis, degrees, clockwise)
    print(f'{msg}\nTransformatiematrix rotatie:\n{matrix}')

def _mirror_vlak(P: Plane, msg, factor=1):
    print(f'{msg}\nTransformatiematrix spiegeling:\n{factor*plane_mirror_matrix(P)}')

_print_rotation_axis(Axis.y,42,False, 'voorbeeld 3.6.4')
_print_rotation_axis(Axis.z,36,False, 'voorbeeld 3.6.5')
_print_rotation_axis(Axis.x,21,True, 'voorbeeld 3.6.6')
_print_projectie_line(Line(2,0), 'Voorbeeld 3.9', 5)
_print_projectie_vlak(Plane(2,-1,3,0), 'voorbeeld 3.11.1', 14)
_mirror_vlak(Plane(2,-1,3,0), 'voorbeeld 4.2.1', 14)

def voorbeeld_4_27_2():
    cos30=math.cos(math.radians(30))
    sin30=math.sin(math.radians(30))
    MR=np.array([[1,0,0],[0,cos30,-sin30],[0,sin30, cos30]])
    MS=np.array([[6,4,-12],[4,12,6],[-12,6,-4]])
    print('voorbeeld 4.27.2')
    print(MR)
    print(MS)
    print(f'A1: {np.dot(MS,MR)}')
    MA1_computed= np.array([[6,4*cos30-12*sin30,-4*sin30-12*cos30],
                            [4,12*cos30+6*sin30, -12*sin30+6*cos30],
                            [-12,6*cos30-4*sin30,-6*sin30-4*cos30]])
    print(f'computed:\n{MA1_computed}')
    print(f'A2: {np.dot(MR,MS)}')
    MA2_computed= np.array([[6,4,-12],
                            [4*cos30+12*sin30,12*cos30-6*sin30, 6*cos30+4*sin30],
                            [4*sin30-12*cos30,12*sin30+6*cos30,6*sin30-4*cos30]])
    print(f'computed:\n{MA2_computed}')

L1 = LineConvertor().vector_line_from_line(Line(10,3))
L2 = LineConvertor().vector_line_from_line(Line(2,-1))
print(L1.line_intersection(L2))
voorbeeld_4_27_2()