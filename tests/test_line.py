import random
import pytest
import itertools
import math
import numpy as np
from lia import LAMBDA, PRECISION
from line import Line, VerticalLine, VectorLine, LineConvertor, LineInvalidException
from lia_test_const import _TEST_VALUES, _TEST_VECTORS_2D, _TEST_VECTORS_3D

#--- line tests
def test_init_line():
    L = Line(1, 2)
    assert L.a == 1
    assert L.b == 2
def _test_str(a,b):
    L = Line(a,b)
    assert str(L) == f'y = {a}x + {b}'
def test_str_line():
    for (a,b) in itertools.combinations(_TEST_VALUES, 2):
        _test_str(a,b)
def _test_x_values(a, b):
    L = Line(a,b)
    for x in _TEST_VALUES:
        assert L.y(x) == a * x + b
def _test_y_values(a, b):
    L = Line(a,b)
    for y in _TEST_VALUES:
        assert round(y,PRECISION) == round(a*L.x(y) + b,PRECISION)
def test_x_values():
    _test_x_values(1, 2)
    _test_x_values(1, 0)
def test_x_values_horizontal_invalid():
    L = Line(0,3)
    with pytest.raises(LineInvalidException):
        L.x(4)
def test_y_values():
    _test_y_values(1, 2)
def _test_is_on_line(a,b):
    L = Line(a,b)
    for x in _TEST_VALUES:
        assert(L.is_on_line(x, x * a + b))
def _test_is_not_on_line(a,b):
    L = Line(a,b)
    for x in _TEST_VALUES:
        assert(not L.is_on_line(x, x * a + b-1))
        assert(not L.is_on_line(x, x * a + b+1))
def test_is_on_line():
    for (a,b) in itertools.combinations(_TEST_VALUES, 2):
        _test_is_on_line(a,b)
def test_is_not_on_line():
    for (a,b) in itertools.combinations(_TEST_VALUES, 2):
        _test_is_not_on_line(a,b)

#vertical line tests
def test_init_vertical_line():
    L = VerticalLine(2)
    assert L.a is None
    assert L.b == 2
def _test_str_vline(b):
    L = VerticalLine(b)
    assert str(L) == f'x = {b}'
def test_str_vline():
    for b in _TEST_VALUES:
        _test_str_vline(b)
def _test_x_values_vline(b):
    L = VerticalLine(b)
    for v in _TEST_VALUES:
        assert L.x(v) == b
def test_x_values_vline():
    _test_x_values_vline(2)
    _test_x_values_vline(0)
    _test_x_values_vline(-1)
def test_y_values_vline():
    L = VerticalLine(42)
    with pytest.raises(LineInvalidException):
        L.y(3)
def test_is_on_vline():
    L = VerticalLine(42)
    for y in _TEST_VALUES:
        assert L.is_on_line(42, y)
def test_is_not_on_vline():
    L = VerticalLine(42)
    for y in _TEST_VALUES:
        assert not L.is_on_line(43, y)

#--- linevector tests
def _test_init_line_vector(P, R, expected_dim):
    LV = VectorLine(P,R)
    assert np.array_equiv(LV.P, P)    
    assert np.array_equiv(LV.R, R)
    assert LV.dim() == expected_dim
def test_init_line_vector2D():
    _test_init_line_vector([1,2], [2,3], 2)
def test_init_line_vector3D():
    _test_init_line_vector([1,2,3], [2.5,3.5,4.5],3)
def test_init_line_vector_invalid():
    with pytest.raises(LineInvalidException):
        VectorLine([0,1], [1,2,3])
def test_init_line_vector_invalid_zero2D():
    with pytest.raises(LineInvalidException):
        VectorLine([0,1], [0,0])
def test_init_line_vector_invalid_zero3D():
    with pytest.raises(LineInvalidException):
        VectorLine([0,1,2], [0,0,0])
def _test_str_line_vector2D(P,R):
    L = VectorLine(P,R)
    assert str(L) == f'V = {L.P[0],L.P[1]} + {LAMBDA}{L.R[0],L.R[1]}'
def test_str_line_vector2D():
    tv = _TEST_VECTORS_2D(20)
    for (P,R) in itertools.combinations(tv, 2):
        _test_str_line_vector2D(P,R)
def _test_str_line_vector3D(P,R):
    L = VectorLine(P,R)
    assert str(L) == f'V = {L.P[0],L.P[1],L.P[2]} + {LAMBDA}{L.R[0],L.R[1],L.R[2]}'
def test_str_line_vector3D():
    tv = _TEST_VECTORS_3D(20)
    for (P,R) in itertools.combinations(tv, 2):
        _test_str_line_vector3D(P,R)
def _test_labda_values(P, R, test_values):
    LV = VectorLine(P, R)
    for l in test_values:
        assert np.array_equiv(LV.V(l), [P[i]+l*R[i] for i in range(LV.dim())])
def test_labda_values2D():
    _test_labda_values([1,2], [2,3], [-1, -.5, 0, .5, 1])
def test_labda_values3D():
    _test_labda_values([1,2,3], [2,3, -1], [-1, -.5, 0, .5, 1])
def _test_labdas(P, R, test_values):
    LV = VectorLine(P, R)
    for l in test_values:
        vv = LV.V(l)
        ll = LV.labda(vv)
        assert round(LV.labda(vv),PRECISION) == round(l, PRECISION)
def test_labdas2D():
    tv = _TEST_VECTORS_2D(20)
    for (P,R) in itertools.combinations(tv, 2):
        _test_labdas(P, R, _TEST_VALUES)
def test_labdas3D():
    tv = _TEST_VECTORS_3D(20)
    for (P,R) in itertools.combinations(tv, 2):
        _test_labdas(P,R, _TEST_VALUES)
def _test_is_on_line_vector(P,R,test_values):
    LV = VectorLine(P, R)
    for l in test_values:
        v = LV.V(l)
        assert LV.is_on_line(v)
def test_is_on_line2D():
    tv = _TEST_VECTORS_2D(20)
    for (P,R) in itertools.combinations(tv, 2):
        _test_is_on_line_vector(P,R, _TEST_VALUES)
def test_is_on_line3D():
    tv = _TEST_VECTORS_3D(20)
    for (P,R) in itertools.combinations(tv, 2):
        _test_is_on_line_vector(P,R, _TEST_VALUES)
def _test_is_not_on_line_vector(P,R,test_values):
    LV = VectorLine(P, R)
    for l in test_values:
        v = LV.V(l)
        v0 = v.copy()
        for r in range(LV.dim()):
            v[r] = v[r]+1
        assert not LV.is_on_line(v)
def test_is_not_on_line2D():
    tv = _TEST_VECTORS_2D(20)
    for (P,R) in itertools.combinations(tv,2):
        _test_is_not_on_line_vector(P,R, _TEST_VALUES)
def test_is_not_on_line3D():
    tv = _TEST_VECTORS_3D(20)
    for (P,R) in itertools.combinations(tv,2):
        _test_is_not_on_line_vector(P,R, _TEST_VALUES)
def __test_angle(LV1, LV2, expected_angle, degrees = True):
    assert round(LV1.angle(LV2,degrees),PRECISION) == round(expected_angle,PRECISION)
    assert round(LV2.angle(LV1, degrees),PRECISION) == round(expected_angle,PRECISION)
def _test_angle(LV1, LV2, expected_angle):
    __test_angle(LV1, LV2, expected_angle)
    __test_angle(LV1, LV2, expected_angle * math.pi/180, False)
def test_angles():
    LV1 = VectorLine([1,3], [1,0])
    _test_angle(LV1, VectorLine([42,42], [1, 0]), 0)
    _test_angle(LV1, VectorLine([42,42], [.5*math.sqrt(3), .5]), 30)
    _test_angle(LV1, VectorLine([42,42], [math.sqrt(3), 1]), 30)
    _test_angle(LV1, VectorLine([42,42], [.5*math.sqrt(2), .5*math.sqrt(2)]), 45)
    _test_angle(LV1, VectorLine([42,42], [5*math.sqrt(2), 5*math.sqrt(2)]), 45)
    _test_angle(LV1, VectorLine([42,42], [.5, .5*math.sqrt(3)]), 60)
    _test_angle(LV1, VectorLine([42,42], [0, 1]), 90)
    _test_angle(LV1, VectorLine([42,42], [-.5*math.sqrt(2), .5*math.sqrt(2)]), 135)
    _test_angle(LV1, VectorLine([42,42], [-1, 0]), 180)
def _test_normal_vector2D(R):
    LV = VectorLine([1,1],R)
    NV = LV.normal_vector()
    assert np.linalg.norm(NV) > 0
    assert round(np.inner(NV, LV.R),PRECISION) == 0
def _random_vector(dim):
    result = []
    for _ in range(dim):
        result.append(random.randrange(-10,10))
    return result
VECT_VALUES_2D = [[-2,-1],[-1.5,+2],[-1.25,-1],[.5,-.333], [0,.333],[.5,1],[1.25,1.5],[2,-1],[3,-1.4]]
def test_normal_vector_normal2D():
    for R in VECT_VALUES_2D:
        _test_normal_vector2D(R)
def test_normal_vector_vertical2D():
    _test_normal_vector2D([1,0])
def _test_intersection(L1, L2: VectorLine):
    IS1 = L1.line_intersection(L2)
    IS2 = L2.line_intersection(L1)
    assert np.allclose(IS1, IS2)
    assert L1.is_on_line(IS1)
    assert L2.is_on_line(IS1)
    assert L1.is_on_line(IS2)
    assert L2.is_on_line(IS2)
def test_intersection2D():
    lines = []
    for P,R in  zip(_TEST_VECTORS_2D(10), _TEST_VECTORS_2D(10)):
        lines.append(VectorLine(P,R))
    for L1 in lines:
        for L2 in lines:
            if L1 is not L2:
                _test_intersection(L1, L2)
        
#--- lineconvertor tests
def test_init_line_convertor():
    LC = LineConvertor()
    assert LC
def _test_line_convertor_vector_from_line(a, b, expected_line):
    LC = LineConvertor()
    line = Line(a,b)
    vector = LC.vector_line_from_line(line)
    assert vector.equivalent(expected_line)
def test_line_convertor_vector_from_line():
    _test_line_convertor_vector_from_line(1,1, VectorLine([-1,0], [1,1]))
    _test_line_convertor_vector_from_line(-1,1, VectorLine([1,0], [1,-1]))
    _test_line_convertor_vector_from_line(2.5,3, VectorLine([-1.2,0], [1,2.5]))
    _test_line_convertor_vector_from_line(0,1, VectorLine([0,1], [1,0]))
def test_line_convertor_vector_from_vline():
    LC = LineConvertor()
    line = VerticalLine(42)
    vector = LC.vector_line_from_line(line)
    assert np.array_equiv(vector.P, [42,0])
    assert np.array_equiv(vector.R, [0,1])
def _test_line_convertor_line_from_vector(P, R, expected_a, expected_b):
    LC = LineConvertor()
    vector = VectorLine(P,R)
    line = LC.line_from_vector_line(vector)
    assert line.a == expected_a
    assert line.b == expected_b
def test_line_convertor_line_from_vector():
    _test_line_convertor_line_from_vector([-1,0], [1,1], 1,1)
    _test_line_convertor_line_from_vector([1,0], [1,-1], -1,1)
    _test_line_convertor_line_from_vector([-1.2,0], [1,2.5], 2.5,3)
def test_line_convertor_vline_from_vector():
    LC = LineConvertor()
    vector = VectorLine([42,0],[0,1])
    line = LC.line_from_vector_line(vector)
    assert isinstance(line, VerticalLine)
    assert line.b == 42
