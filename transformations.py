from enum import Enum, auto
import math
import numpy as np
from line import VectorLine
from plane import Plane, PlaneConvertor

def plane_projection(X: np.array, P: Plane)->np.array:
    n = P.normal_vector()
    return PlaneConvertor().vector_plane_from_plane(P).line_intersection(VectorLine(X,[n[i]for i in range(len(n))]))

def plane_projection_matrix(P: Plane)->np.array:
    p1 = plane_projection([1,0,0], P)
    p2 = plane_projection([0,1,0], P)
    p3 = plane_projection([0,0,1], P)
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
