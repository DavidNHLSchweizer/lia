from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
import math
from pickle import FALSE
import numpy as np
from lia import Axis
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

def line_mirror(X: np.array, L: Line)->np.array:
    projection=line_projection(X, L)
    return np.array([2*projection[i]-X[i] for i in range(2)])

def line_mirror_matrix(L: Line)->np.array:
    p1 = line_mirror([1,0], L)
    p2 = line_mirror([0,1], L)
    print(f'{L}:!{np.round(5*p1,3)}   {np.round(5*p2,3)}')
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

def _get_cos_and_sin(degrees: float, clockwise: bool=False)->tuple:
    rads = math.radians(degrees)
    if clockwise:
        rads = -rads
    return (math.cos(rads), math.sin(rads))

def rotation_matrix_2d(degrees: float, clockwise: bool=False)->np.array:
    cos, sin = _get_cos_and_sin(degrees, clockwise)
    return np.array([[cos, -sin], [sin, cos]])

@dataclass
class AxisRotation:
    axis: Axis = Axis.x
    degrees: float = 0
    clockwise: bool = False

def axis_rotation_matrix(rotation: AxisRotation)->np.array:    
    cos, sin = _get_cos_and_sin(rotation.degrees, rotation.clockwise)
    match rotation.axis:
        case Axis.x:
            r1 = [1,0,0]
            r2 = np.array([0, cos, -sin])
            r3 = np.array([0, sin, cos])
        case Axis.y:
            r1 = np.array([cos, 0, sin])
            r2 = [0,1,0]
            r3 = np.array([-sin, 0, cos])
        case Axis.z:
            r1 = np.array([cos, -sin, 0])
            r2 = np.array([sin, cos, 0])
            r3 = [0,0,1]
    return np.array([r1,r2,r3])

def multiple_rotation_matrix(rotations: list[AxisRotation])->np.array:
    # order of application == order in list, checked with https://www.andre-gaschler.com/rotationconverter/
    result = np.identity(3)
    for rotation in rotations:
        M = axis_rotation_matrix(rotation)
        result = np.dot(M, result)
    return result

class AffineMatrix:
    def __init__(self, M: type[np.array|AffineMatrix], copy_matrix = False):        
        if not copy_matrix:
            lastcolumn = []
            for _ in range(len(M)):
                lastcolumn.append([0])
            self.matrix = np.append(M, np.array(lastcolumn),axis=1)
            lastrow=[]
            for _ in range(len(M[0]-1)):
                lastrow.append(0)
            lastrow.append(1)
            self.matrix = np.r_[self.matrix, [np.array(lastrow)]]
        else:
            if isinstance(M, AffineMatrix):
                self.matrix = M.matrix
            else:
                self.matrix = M
    def __str__(self):
        return str(self.matrix)
    def transform(self, vector: np.array)->np.array:        
        affine_vector = np.append(np.copy(vector), 1)
        return np.dot(self.matrix,affine_vector)[:-1]
    def __mul__(self, AM2: AffineMatrix):
        return AffineMatrix(np.dot(self.matrix, AM2.matrix), copy_matrix=True)

class TranslationMatrix(AffineMatrix):
    def __init__(self, vector: np.array):        
        super().__init__(np.identity(len(vector)))
        lastcol = len(vector)
        for row, value in enumerate(vector):
            self.matrix[row][lastcol] = value
