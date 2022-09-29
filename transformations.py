from enum import Enum, auto
import math
import numpy as np
from line import Line, LineConvertor, VectorLine
from plane import Plane, PlaneConvertor

def line_projection(X: np.array, L: Line)->np.array:
    vector_line = LineConvertor().vector_line_from_line(L)
    normal_line = VectorLine(X, vector_line.normal_vector())
    return vector_line.line_intersection(normal_line)

def line_projection_matrix(L: Line)->np.array:
    p1 = line_projection([1,0], L)
    p2 = line_projection([0,1], L)
    return np.array([p1,p2])

def plane_projection(X: np.array, P: Plane)->np.array:
    n = P.normal_vector()
    return PlaneConvertor().vector_plane_from_plane(P).line_intersection(VectorLine(X,[n[i]for i in range(len(n))]))

def plane_projection_matrix(P: Plane)->np.array:
    p1 = plane_projection([1,0,0], P)
    p2 = plane_projection([0,1,0], P)
    p3 = plane_projection([0,0,1], P)
    return np.array([p1,p2,p3])

def plane_mirror(X: np.array, P: Plane)->np.array:
    projection=plane_projection(X, P)
    return [2*projection[i]-X[i] for i in range(3)]

def plane_mirror_matrix(P: Plane)->np.array:
    p1 = plane_mirror([1,0,0], P)
    p2 = plane_mirror([0,1,0], P)
    p3 = plane_mirror([0,0,1], P)
    return np.array([p1,p2,p3])

class Axis(Enum):
    x=auto()
    y=auto()
    z=auto()
def axis_rotation_matrix(axis: Axis, degrees: float, clockwise: bool)->np.array:    
    rads = math.radians(degrees)
    if clockwise:
        rads = -rads
    match axis:
        case Axis.x:
            r1 = [1,0,0]
            r2 = np.array([0, math.cos(rads), -math.sin(rads)])
            r3 = np.array([0, math.sin(rads), math.cos(rads)])
        case Axis.y:
            r1 = np.array([math.cos(rads), 0, math.sin(rads)])
            r2 = [0,1,0]
            r3 = np.array([-math.sin(rads), 0, math.cos(rads)])
        case Axis.z:
            r1 = np.array([math.cos(rads), -math.sin(rads), 0])
            r2 = np.array([math.sin(rads), math.cos(rads), 0])
            r3 = [0,0,1]
    return np.array([r1,r2,r3])
