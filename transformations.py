from __future__ import annotations
from enum import Enum, auto
import math
from pickle import FALSE
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

def _get_cos_and_sin(degrees: float, clockwise: bool=False)->tuple:
    rads = math.radians(degrees)
    if clockwise:
        rads = -rads
    return (math.cos(rads), math.sin(rads))

def rotation_matrix_2d(degrees: float, clockwise: bool=False)->np.array:
    cos, sin = _get_cos_and_sin(degrees, clockwise)
    return np.array([[cos, -sin], [sin, cos]])

class Axis(Enum):
    x=auto()
    y=auto()
    z=auto()
def axis_rotation_matrix(axis: Axis, degrees: float, clockwise: bool=False)->np.array:    
    cos, sin = _get_cos_and_sin(degrees, clockwise)
    match axis:
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

class AffineMatrix:
    def __init__(self, M: np.array, copy_matrix = False):        
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
            self.matrix = M
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

# M = plane_mirror_matrix(Plane(2,-1,3,0))
# print(M*14)
# AM = AffineMatrix(M)
# print(14*AM.matrix)
# print(AM.transform([4,6,-1]))
# print(14*AM.transform([4,6,-1]))
# # TM = TranslationMatrix([5,6])
# # print(TM.matrix)
# # print(TM.transform([1,2]))

# TM = TranslationMatrix([5,6,2])
# print(TM.matrix)


# TM = TranslationMatrix([4,5,6])
# print(TM.matrix)
# print(TM.transform([1,2,3]))