import pytest
import math
import numpy as np
from line import Line, VerticalLine, LineVector, LineConvertor, LineInvalidException, lamda


#--- line tests
def test_init_line():
    L = Line(1, 2)
    assert L.a == 1
    assert L.b == 2
def _test_str(a,b):
    L = Line(a,b)
    assert str(L) == f'y = {a}x + {b}'
def test_str_line():
    for (a,b) in zip([-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2], [-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2]):
        _test_str(a,b)
def _test_x_values(a, b, test_values):
    L = Line(a,b)
    for v in test_values:
        assert L.y(v) == a * v + b
def _test_y_values(a, b, test_values):
    L = Line(a,b)
    for v in test_values:
        assert L.x(v) == (v-b)/a        
def test_x_values():
    _test_x_values(1, 2, [-1, -.5, 0, .5, 1])
def test_x_values_horizontal():
    L = Line(0,3)
    with pytest.raises(LineInvalidException):
        L.x(4)
def test_y_values():
    _test_y_values(1, 2, [-1, -.5, 0, .5, 1])
def _test_is_on_line(a,b):
    L = Line(a,b)
    for x in [-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2]:
        assert(L.is_on_line(x, x * a + b))
def _test_is_not_on_line(a,b):
    L = Line(a,b)
    for x in [-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2]:
        assert(not L.is_on_line(x, x * a + b-1))
        assert(not L.is_on_line(x, x * a + b+1))
def test_is_on_line():
    for (a,b) in zip([-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2], [-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2]):
        _test_is_on_line(a,b)
def test_is_not_on_line():
    for (a,b) in zip([-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2], [-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2]):
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
    for b in [-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2]:
        _test_str_vline(b)
def _test_x_values_vline(b, test_values):
    L = VerticalLine(b)
    for v in test_values:
        assert L.x(v) == b
def test_x_values_vline():
    _test_x_values_vline(2, [-1, -.5, 0, .5, 1])
def test_y_values_vline():
    L = VerticalLine(42)
    with pytest.raises(LineInvalidException):
        L.y(3)
def test_is_on_vline():
    L = VerticalLine(42)
    for y in [-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2]:
        assert L.is_on_line(42, y)
def test_is_not_on_vline():
    L = VerticalLine(42)
    for y in [-2,-1.5,-1.25,-1,.5,-.333, 0,.333,.5,1,1.25,1.5,2]:
        assert not L.is_on_line(43, y)

#--- linevector tests
def test_init_line_vector2D():
    LV = LineVector([1,2], [2,3])
    assert np.array_equiv(LV.P, [1,2])    
    assert np.array_equiv(LV.R, [2,3])
    assert LV.dim() == 2
def test_init_line_vector3D():
    LV = LineVector([1,2,3], [2.5,3.5,4.5])
    assert np.array_equiv(LV.P, [1,2,3])    
    assert np.array_equiv(LV.R, [2.5,3.5,4.5])
    assert LV.dim() == 3
def test_init_line_vector_invalid():
    with pytest.raises(LineInvalidException):
        LineVector([0,1], [1,2,3])
def _test_str_line_vector2D(P,R):
    L = LineVector(P,R)
    assert str(L) == f'V = {L.P[0],L.P[1]} + {lamda}{L.R[0],L.R[1]}'
def test_str_line_vector2D():
    for (P,R) in zip([[-2,-1],[-1.5,+2],[-1.25,-1],[.5,-.333], [0,.333],[.5,1],[1.25,1.5],[2,-1],[3,-1.4]], [[-2,-1],[-1.5,+2],[-1.25,-1],[.5,-.333], [0,.333],[.5,1],[1.25,1.5],[2,-1],[3,-1.4]]):
        _test_str_line_vector2D(P,R)
def _test_str_line_vector3D(P,R):
    L = LineVector(P,R)
    assert str(L) == f'V = {L.P[0],L.P[1],L.P[2]} + {lamda}{L.R[0],L.R[1],L.R[2]}'
def test_str_line_vector3D():
    for (P,R) in zip([[-2,-1,4],[-1.5,+2,-1],[-1.25,0,-1],[1,.5,-.333], [-4,0,.333],[.5,1,1],[1.25,.87,1.5],[42,2,-1],[3,-42,-1.4]], 
                        [[-2,-1,4],[-1.5,+2,-1],[-1.25,0,-1],[1,.5,-.333], [-4,0,.333],[.5,1,1],[1.25,.87,1.5],[42,2,-1],[3,-42,-1.4]]):
        _test_str_line_vector3D(P,R)
def _test_labda_values(P, R, test_values):
    LV = LineVector(P, R)
    for l in test_values:
        assert np.array_equiv(LV.V(l), [P[i]+l*R[i] for i in range(LV.dim())])
def test_labda_values2D():
    _test_labda_values([1,2], [2,3], [-1, -.5, 0, .5, 1])
def test_labda_values3D():
    _test_labda_values([1,2,3], [2,3, -1], [-1, -.5, 0, .5, 1])
def _test_labdas(P, R, test_values):
    LV = LineVector(P, R)
    for l in test_values:
        vv = LV.V(l)
        ll = LV.labda(vv)
        assert round(LV.labda(vv),6) == round(l, 6)
def test_labdas2D():
    for (P,R) in zip([[-2,-1],[-1.5,+2],[-1.25,-1],[.5,-.333], [0,.333],[.5,1],[1.25,1.5],[2,-1],[3,-1.4]], [[-2,-1],[-1.5,+2],[-1.25,-1],[.5,-.333], [0,.333],[.5,1],[1.25,1.5],[2,-1],[3,-1.4]]):
        _test_labdas(P,R, [-3,-2, -1.4, -1.3, -1, .75, 0, 0.1, 0.4, 0.9, 1, 1.2, 2, 3, 50, 100])
def test_labdas3D():
    for (P,R) in zip([[-2,-1,4],[-1.5,+2,-1],[-1.25,0,-1],[1,.5,-.333], [-4,0,.333],[.5,1,1],[1.25,.87,1.5],[42,2,-1],[3,-42,-1.4]], 
                        [[-2,-1,4],[-1.5,+2,-1],[-1.25,0,-1],[1,.5,-.333], [-4,0,.333],[.5,1,1],[1.25,.87,1.5],[42,2,-1],[3,-42,-1.4]]):
        _test_labdas(P,R, [-3,-2, -1.4, -1.3, -1, .75, 0, 0.1, 0.4, 0.9, 1, 1.2, 2, 3, 50, 100])
def _test_is_on_line_vector(P,R,test_values):
    LV = LineVector(P, R)
    for l in test_values:
        v = LV.V(l)
        assert LV.is_on_line(v)
def test_is_on_line2D():
    for (P,R) in zip([[-2,-1],[-1.5,+2],[-1.25,-1],[.5,-.333], [0,.333],[.5,1],[1.25,1.5],[2,-1],[3,-1.4]], [[-2,-1],[-1.5,+2],[-1.25,-1],[.5,-.333], [0,.333],[.5,1],[1.25,1.5],[2,-1],[3,-1.4]]):
        _test_is_on_line_vector(P,R, [-3,-2, -1.4, -1.3, -1, .75, 0, 0.1, 0.4, 0.9, 1, 1.2, 2, 3, 50, 100])
def test_is_on_line3D():
    for (P,R) in zip([[-2,-1,4],[-1.5,+2,-1],[-1.25,0,-1],[1,.5,-.333], [-4,0,.333],[.5,1,1],[1.25,.87,1.5],[42,2,-1],[3,-42,-1.4]], 
                        [[-2,-1,4],[-1.5,+2,-1],[-1.25,0,-1],[1,.5,-.333], [-4,0,.333],[.5,1,1],[1.25,.87,1.5],[42,2,-1],[3,-42,-1.4]]):
        _test_is_on_line_vector(P,R, [-3,-2, -1.4, -1.3, -1, .75, 0, 0.1, 0.4, 0.9, 1, 1.2, 2, 3, 50, 100])
def _test_is_not_on_line_vector(P,R,test_values):
    LV = LineVector(P, R)
    for l in test_values:
        v = LV.V(l)
        v0 = v.copy()
        for r in range(LV.dim()):
            v[r] = v[r]+1
        assert not LV.is_on_line(v)
def test_is_not_on_line2D():
    for (P,R) in zip([[-2,-1],[-1.5,+2],[-1.25,-1],[.5,-.333], [0,.333],[.5,1],[1.25,1.5],[2,-1],[3,-1.4]], [[-2,-1],[-1.5,+2],[-1.25,-1],[.5,-.333], [0,.333],[.5,1],[1.25,1.5],[2,-1],[3,-1.4]]):
        _test_is_not_on_line_vector(P,R, [-3,-2, -1.4, -1.3, -1, .75, 0, 0.1, 0.4, 0.9, 1, 1.2, 2, 3, 50, 100])
def test_is_not_on_line3D():
    for (P,R) in zip([[-2,-1,4],[-1.5,+2,-1],[-1.25,0,-1],[1,.5,-.333], [-4,0,.333],[.5,1,1],[1.25,.87,1.5],[42,2,-1],[3,-42,-1.4]], 
                        [[-2,-1,4],[-1.5,+2,-1],[-1.25,0,-1],[1,.5,-.333], [-4,0,.333],[.5,1,1],[1.25,.87,1.5],[42,2,-1],[3,-42,-1.4]]):
        _test_is_not_on_line_vector(P,R, [-3,-2, -1.4, -1.3, -1, .75, 0, 0.1, 0.4, 0.9, 1, 1.2, 2, 3, 50, 100])
def __test_angle(LV1, LV2, expected_angle, degrees = True):
    assert round(LV1.angle(LV2,degrees),6) == round(expected_angle,6)
    assert round(LV2.angle(LV1, degrees),6) == round(expected_angle,6)
def _test_angle(LV1, LV2, expected_angle):
    __test_angle(LV1, LV2, expected_angle)
    __test_angle(LV1, LV2, expected_angle * math.pi/180, False)
def test_angles():
    LV1 = LineVector([1,3], [1,0])
    _test_angle(LV1, LineVector([42,42], [1, 0]), 0)
    _test_angle(LV1, LineVector([42,42], [.5*math.sqrt(3), .5]), 30)
    _test_angle(LV1, LineVector([42,42], [math.sqrt(3), 1]), 30)
    _test_angle(LV1, LineVector([42,42], [.5*math.sqrt(2), .5*math.sqrt(2)]), 45)
    _test_angle(LV1, LineVector([42,42], [5*math.sqrt(2), 5*math.sqrt(2)]), 45)
    _test_angle(LV1, LineVector([42,42], [.5, .5*math.sqrt(3)]), 60)
    _test_angle(LV1, LineVector([42,42], [0, 1]), 90)
    _test_angle(LV1, LineVector([42,42], [-.5*math.sqrt(2), .5*math.sqrt(2)]), 135)
    _test_angle(LV1, LineVector([42,42], [-1, 0]), 180)
def _test_normal_vector(R):
    LV = LineVector([1,1],R)
    NV = LV.normal_vector()
    assert round(np.inner(NV, LV.R),6) == 0
def test_normal_vector_normal():
    for R in [[-2,-1],[-1.5,+2],[-1.25,-1],[.5,-.333], [0,.333],[.5,1],[1.25,1.5],[2,-1],[3,-1.4]]:
        _test_normal_vector(R)
def test_normal_vector_vertical():
    _test_normal_vector([1,0])

#--- lineconvertor tests
def test_init_line_convertor():
    LC = LineConvertor()
    assert LC
def _test_line_convertor_vector_from_line(a, b, expected_V1, expected_V2):
    LC = LineConvertor()
    line = Line(a,b)
    vector = LC.vector_from_line(line)
    assert np.array_equiv(vector.P, expected_V1)
    assert np.array_equiv(vector.R, expected_V2)
def test_line_convertor_vector_from_line():
    _test_line_convertor_vector_from_line(1,1, [-1,0], [1,1])
    _test_line_convertor_vector_from_line(-1,1, [1,0], [1,-1])
    _test_line_convertor_vector_from_line(2.5,3, [-1.2,0], [1,2.5])
    _test_line_convertor_vector_from_line(0,1, [0,1], [1,0])
def test_line_convertor_vector_from_vline():
    LC = LineConvertor()
    line = VerticalLine(42)
    vector = LC.vector_from_line(line)
    assert np.array_equiv(vector.P, [42,0])
    assert np.array_equiv(vector.R, [0,1])
def _test_line_convertor_line_from_vector(P, R, expected_a, expected_b):
    LC = LineConvertor()
    vector = LineVector(P,R)
    line = LC.line_from_vector(vector)
    assert line.a == expected_a
    assert line.b == expected_b
def test_line_convertor_line_from_vector():
    _test_line_convertor_line_from_vector([-1,0], [1,1], 1,1)
    _test_line_convertor_line_from_vector([1,0], [1,-1], -1,1)
    _test_line_convertor_line_from_vector([-1.2,0], [1,2.5], 2.5,3)
def test_line_convertor_vline_from_vector():
    LC = LineConvertor()
    vector = LineVector([42,0],[0,1])
    line = LC.line_from_vector(vector)
    assert isinstance(line, VerticalLine)
    assert line.b == 42

