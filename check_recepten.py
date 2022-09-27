
from plane import Plane
from transformations import Axis, axis_rotation_matrix, plane_projection_matrix


def _projectie_vlak(P: Plane, msg, factor=1):
    print(f'{msg}\nTransformatiematrix:\n{factor*plane_projection_matrix(P)}')

def _print_rotation_axis(axis, degrees, clockwise, msg):
    matrix = axis_rotation_matrix(axis, degrees, clockwise)
    print(f'{msg}\nTransformatiematrix:\n{matrix}')

_projectie_vlak(Plane(2,-1,3,0), 'voorbeeld 3.10.1', 14)
_print_rotation_axis(Axis.y,42,False, 'voorbeeld 3.6.4')
_print_rotation_axis(Axis.z,36,False, 'voorbeeld 3.6.5')
_print_rotation_axis(Axis.x,21,True, 'voorbeeld 3.6.6')

