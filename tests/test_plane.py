from cmath import exp
import itertools
import pytest
import numpy as np
from lia import LAMBDA, MU, PRECISION
from plane import Plane, PlaneInvalidException, PlaneVector
from lia_test_const import _TEST_VALUES, _TEST_VECTORS_2D, _TEST_VECTORS_3D, ABCD_VALUES

#plane tests
def _test_init_plane(a,b,c,d):
    P = Plane(a,b,c,d)
    assert P.a == a    
    assert P.b == b    
    assert P.c == c    
    assert P.d == d
    assert str(P) == f'{P.a}x + {P.b}y + {P.c}z = {P.d}'

def test_init_plane():
    for (a,b,c,d) in ABCD_VALUES:
        _test_init_plane(a,b,c,d) 
    
def test_init_plane_invalid():
    with pytest.raises(PlaneInvalidException):
        Plane(0,0,0,1)

def _test_plane_normal_vector(a,b,c,d):
    P = Plane(a,b,c,d)
    assert np.array_equiv(P.normal_vector(), [a,b,c])

def test_plane_normal_vector():
    for (a,b,c,d) in ABCD_VALUES:
        _test_plane_normal_vector(a,b,c,d) 
    
def _test_plane_x(P):
    if not round(P.a, PRECISION) == 0:
        for (y,z) in itertools.combinations(_TEST_VALUES, 2):
            assert round(P.a * P.x(y,z) + P.b * y + P.c * z, PRECISION) == P.d

def test_plane_x():
    for (a,b,c,d) in ABCD_VALUES:
        _test_plane_x(Plane(a,b,c,d))

def _test_plane_y(P):
    if not round(P.b, PRECISION) == 0:
        for (x,z) in itertools.combinations(_TEST_VALUES, 2):
            assert round(P.a * x + P.b * P.y(x,z) + P.c * z, PRECISION) == P.d

def test_plane_y():
    for (a,b,c,d) in ABCD_VALUES:
        _test_plane_y(Plane(a,b,c,d))

def _test_plane_z(P):
    if not round(P.c, PRECISION) == 0:
        for (x,y) in itertools.combinations(_TEST_VALUES, 2):
            assert round(P.a * x + P.b * y + P.c * P.z(x,y), PRECISION) == P.d

def _test_parallel(P:Plane):
    assert round(P.a, PRECISION) != 0 ^ P.is_parallel_x()
    assert round(P.b, PRECISION) != 0 ^ P.is_parallel_y()
    assert round(P.c, PRECISION) != 0 ^ P.is_parallel_z()

def test_parallel():
    for (a,b,c,d) in ABCD_VALUES:
        _test_parallel(Plane(a,b,c,d))

def test_plane_z():
    for (a,b,c,d) in ABCD_VALUES:
        _test_plane_z(Plane(a,b,c,d))

def __test_is_on_plane(P:Plane, x, y, z):
    assert P.is_on_plane(x, y, z)
    if P.is_parallel_x():
        assert P.is_on_plane(x+0.1, y, z)
    else:
        assert not P.is_on_plane(x+0.1, y, z)
    if P.is_parallel_y():
        assert P.is_on_plane(x, y+0.1, z)
    else:
        assert not P.is_on_plane(x, y+0.1, z)
    if P.is_parallel_z():
        assert P.is_on_plane(x, y, z-0.1)
    else:
        assert not P.is_on_plane(x, y, z-0.1)

def _test_is_on_plane(P:Plane):
    if not P.is_parallel_z():
        for (x,y) in itertools.combinations(_TEST_VALUES, 2):
            __test_is_on_plane(P, x, y, P.z(x,y))

def test_is_on_plane():
    for (a,b,c,d) in ABCD_VALUES:
        _test_is_on_plane(Plane(a,b,c,d))

#plane vector tests
def _test_init_plane_vector(P, R1, R2):
    PV = PlaneVector(P, R1, R2)
    assert np.array_equiv(PV.P, P)    
    assert np.array_equiv(PV.R1, R1)
    assert np.array_equiv(PV.R2, R2)
    assert str(PV) == f'{PV.P} + {LAMBDA}{PV.R1} + {MU}{PV.R2}'

def test_init_plane_vector():
    _test_init_plane_vector([1,2,3], [2,4,6], [7,8,9])
    
def test_init_plane_vector_invalid1():
    with pytest.raises(PlaneInvalidException):
        PlaneVector([1,2], [2,4,6], [7,8,9])
    with pytest.raises(PlaneInvalidException):
        PlaneVector([1,2,3], [2,6], [7,8,9])
    with pytest.raises(PlaneInvalidException):
        PlaneVector([1,2,3], [2,4,6], [7,8])

def test_init_plane_vector_invalid2():
    with pytest.raises(PlaneInvalidException):
        PlaneVector([0,0,0], [1,0,0], [2,0,0])
    with pytest.raises(PlaneInvalidException):
        PlaneVector([0,0,0], [1,0,0], [-1,0,0])

def test_init_plane_vector_invalid3():
    with pytest.raises(PlaneInvalidException):
        PlaneVector([0,0,0], [0,0,0], [2,0,0])
    with pytest.raises(PlaneInvalidException):
        PlaneVector([0,0,0], [1,0,0], [0,0,0])

def _test_plane_vector_normal_vector(PV: PlaneVector, expected_vector):
    assert np.array_equiv(PV.normal_vector(), expected_vector)

def test_plane_vector_normal_vector():
    _test_plane_vector_normal_vector(PlaneVector([1,2,3], [1,0,0], [0,1,0]), [0,0,1])
    _test_plane_vector_normal_vector(PlaneVector([1,2,3], [1,2,3], [3,4,5]), [-2,4,-2])

