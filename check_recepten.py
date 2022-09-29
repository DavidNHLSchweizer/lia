
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

L1 = LineConvertor().vector_line_from_line(Line(10,3))
L2 = LineConvertor().vector_line_from_line(Line(2,-1))
print(L1.line_intersection(L2))