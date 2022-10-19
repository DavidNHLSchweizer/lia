import math
import numpy as np
import pytest
from quaternion import QU, PointQuaternion, Quaternion, QuaternionException, RotationQuaternion
from transformations import Axis, AxisRotation, axis_rotation_matrix, multiple_rotation_matrix

TESTQ = [{'q': [1,2,3,4], 's':'1+2i+3j+4k'},{'q':[1,0,3,4], 's':'1+3j+4k'}, {'q':[1,2,0,4], 's':'1+2i+4k'}, {'q':[1,2,3,0], 's':'1+2i+3j'}, {'q':[0,0,0,0], 's':'0'}, {'q':[1,0,0,0], 's':'1'}, {'q':[0,1,0,0], 's':'i'}, 
        {'q':[0,0,1,0], 's':'j'}, {'q':[0,0,0,1], 's':'k'}, {'q':[1,1,0,0], 's':'1+i'}, {'q':[1,0,1,0], 's':'1+j'}, {'q':[1,0,0,1], 's':'1+k'}, {'q':[1,1,1,0], 's':'1+i+j'}, {'q':[1,0,1,1], 's':'1+j+k'}, {'q':[1,1,0,1], 's':'1+i+k'},
        {'q':[1,1,1,1], 's':'1+i+j+k'},{'q':[0,1,2,3], 's':'i+2j+3k'}, {'q':[-1,0,0,0], 's':'-1'}, {'q':[-1,1,0,0], 's':'-1+i'}, {'q':[-1,1,2,3], 's':'-1+i+2j+3k'}, {'q':[0,-1,2,3], 's':'-i+2j+3k'}, {'q':[0,0,-1,0], 's':'-j'}, 
        {'q':[0,0,0,-1], 's':'-k'}, {'q':[1,-1,2,-3], 's':'1-i+2j-3k'},{'q':[1.1,-1.2,2.2,-3.3], 's':'1.1-1.2i+2.2j-3.3k'}, {'q':[math.pi,-math.pi,math.pi,-math.pi], 's':'3.142-3.142i+3.142j-3.142k'}]

def Q(tq):
    return Quaternion(tq['q'][0], tq['q'][1], tq['q'][2], tq['q'][3])

#QUATERNION BASE CLASS TESTS
def _test_init(a,b,c,d):
    q = Quaternion(a,b,c,d)
    assert q.w == a
    assert q.x == b
    assert q.y == c
    assert q.z == d
def test_init():
    for tq in TESTQ:
        _test_init(tq['q'][0], tq['q'][1], tq['q'][2], tq['q'][3])

def _test_index(a,b,c,d):
    q = Quaternion(a,b,c,d)
    assert q[QU.R]==a    
    assert q[QU.i]==b    
    assert q[QU.j]==c
    assert q[QU.k]==d
def test_index():
    for tq in TESTQ:
        _test_index(tq['q'][0], tq['q'][1], tq['q'][2], tq['q'][3])

def test_index_invalid():
    q = Quaternion(1,2,3,4)
    with pytest.raises(QuaternionException):
        q[-1]
    with pytest.raises(QuaternionException):
        q[4]

def squeeze(s):
    return "".join(s.split())

def _test_str(tq):
    assert squeeze(str(Q(tq)))==tq['s']
def test_str():
    for tq in TESTQ:
        _test_str(tq)

def _test_equal(q1, q2, expected):
    assert (q1 == q2) == expected
def test_equal():
    for tq1 in TESTQ:
        for tq2 in TESTQ:
            _test_equal(Q(tq1), Q(tq2), tq1==tq2)

def _test_conjugate(a,b,c,d):
    q = Quaternion(a,b,c,d)
    assert q.conjugate() == Quaternion(a,-b,-c,-d)
def test_conjugate():
    for tq in TESTQ:
        _test_conjugate(tq['q'][0], tq['q'][1], tq['q'][2], tq['q'][3])

def _test_add(q1, q2):
    assert q1 + q2 == Quaternion(q1.w + q2.w, q1.x + q2.x, q1.y + q2.y, q1.z + q2.z)
def test_add():
    for tq1 in TESTQ:
        for tq2 in TESTQ:
            _test_add(Q(tq1), Q(tq2))

def _test_sub(q1, q2):
    assert q1 - q2 == Quaternion(q1.w - q2.w, q1.x - q2.x, q1.y - q2.y, q1.z - q2.z)
def test_sub():
    for tq1 in TESTQ:
        for tq2 in TESTQ:
            _test_sub(Q(tq1), Q(tq2))

def _test_neg(q1):
    assert -q1 == Quaternion(-q1.w, -q1.x, -q1.y, -q1.z)
def test_neg():
    for tq1 in TESTQ:
        _test_neg(Q(tq1))

def _test_mul(q1, q2):
    #source: https://en.wikipedia.org/wiki/Quaternion#Multiplication_of_basis_elements
    assert q1 * q2 == Quaternion(q1.w*q2.w - q1.x*q2.x - q1.y*q2.y - q1.z*q2.z, 
                                 q1.x*q2.w + q1.w*q2.x + q1.y*q2.z - q1.z*q2.y,
                                 q1.w*q2.y - q1.x*q2.z + q1.y*q2.w + q1.z*q2.x,
                                 q1.w*q2.z + q1.x*q2.y - q1.y*q2.x + q1.z*q2.w)
def test_mul():
    for tq1 in TESTQ:
        for tq2 in TESTQ:
            _test_mul(Q(tq1), Q(tq2))

def _test_mul_scalar(q1, value):
    q = Quaternion(value*q1.w, value*q1.x, value*q1.y, value*q1.z)
    assert value*q1 == q
    assert q1*value == q
TESTVALUES = [-42, -3.5, -math.pi, -2, -1, -0.5, -0.1, 0, 0.1, 0.5, 1, 2, math.pi, 3.5, 42]
def test_mul_scalar():
    for tq in TESTQ:
        for value in TESTVALUES:
            _test_mul_scalar(Q(tq), value)

#ROTATION QUATERNION TESTS
TESTDEGREES = [-180, -142, -110, -90, -60, -45, -42, -30, 15, 0, 30, 42, 45, 60, 90, 110, 142, 180]
def _test_rotation_quaternion_init(degrees, vector):
    RQ = RotationQuaternion(degrees, vector)
    cos = math.cos(math.radians(degrees*.5))
    sin = math.sin(math.radians(degrees*.5))
    uv = vector / np.linalg.norm(vector)
    assert np.allclose(uv, RQ.unit_vector)
    assert np.allclose(RQ._q, [cos, uv[0] * sin, uv[1] * sin, uv[2] * sin])
def test_rotation_quaternion_init():
    for degrees in TESTDEGREES:
        _test_rotation_quaternion_init(degrees, [1,2,3])

#POINT QUATERNION TESTS
def _test_point_quaternion_init(vector):
    PQ = PointQuaternion(vector)
    assert np.array_equal(PQ._q, [0,vector[0],vector[1],vector[2]])

def test_point_quaternion_init():
    for vector in [[1,0,0], [0,1,0], [0,0,1], [-1,-2,-3], [1,2,3]]:
        _test_point_quaternion_init(vector)

def _test_point_quaternion_transform_x(vector, degrees):
    PQ = PointQuaternion(vector)
    RQ = RotationQuaternion(degrees, [2,0,0])
    P_image = PQ.transform(RQ)
    matrix = axis_rotation_matrix(AxisRotation(Axis.x, degrees))
    assert np.allclose(P_image, np.dot(matrix, vector))

def test_point_quaternion_transform_x():
    for degrees in TESTDEGREES:
        _test_point_quaternion_transform_x([1,2,3], degrees)

def _test_point_quaternion_transform_y(vector, degrees):
    PQ = PointQuaternion(vector)
    RQ = RotationQuaternion(degrees, [0,2,0])
    P_image = PQ.transform(RQ)
    matrix = axis_rotation_matrix(AxisRotation(Axis.y, degrees))
    assert np.allclose(P_image, np.dot(matrix, vector))

def test_point_quaternion_transform_y():
    for degrees in TESTDEGREES:
        _test_point_quaternion_transform_y([1,2,3], degrees)

def _test_point_quaternion_transform_z(vector, degrees):
    PQ = PointQuaternion(vector)
    RQ = RotationQuaternion(degrees, [0,0,2])
    P_image = PQ.transform(RQ)
    matrix = axis_rotation_matrix(AxisRotation(Axis.z, degrees))
    assert np.allclose(P_image, np.dot(matrix, vector))

def test_point_quaternion_transform_z():
    for degrees in TESTDEGREES:
        _test_point_quaternion_transform_z([1,2,3], degrees)

def _test_point_quaternion_transform_xyz(rotations: list[AxisRotation], effective_degrees: float, rotation_vector: list[float], P: list[float]):
    Matrix = multiple_rotation_matrix(rotations)
    PQ = PointQuaternion(P)
    RQ = RotationQuaternion(effective_degrees, rotation_vector)
    P_image = PQ.transform(RQ)
    assert np.allclose(P_image, np.dot(Matrix, P))

def test_point_quaternion_transform_xyz():
    #values generated with https://www.andre-gaschler.com/rotationconverter/
    _test_point_quaternion_transform_xyz([AxisRotation(Axis.z,40), AxisRotation(Axis.y, 50), AxisRotation(Axis.x, 60)], 96.5925037, [ 0.7380231, 0.2530664, 0.6255232 ], [1,2,3])
    _test_point_quaternion_transform_xyz([AxisRotation(Axis.x,60), AxisRotation(Axis.z, 40), AxisRotation(Axis.y, 50)], 96.5925037, [ 0.7380231, 0.6682522, 0.0935997 ], [1,2,3])
    _test_point_quaternion_transform_xyz([AxisRotation(Axis.y,44), AxisRotation(Axis.z, 55), AxisRotation(Axis.x, 33)], 66.2077347, [ 0.1240108, 0.3607056, 0.9243986 ], [1,2,3])
    _test_point_quaternion_transform_xyz([AxisRotation(Axis.y,44), AxisRotation(Axis.x, 33), AxisRotation(Axis.z, 55)], 84.6346987, [ 0.1006029, 0.6538431, 0.7499121 ], [1,2,3])
