from cmath import exp
import pytest
import numpy as np
from lia import lamda, mu
from plane import Plane, PlaneInvalidException, PlaneVector

T_VALUES = [
            (1,2,3,4),    
            (1,-2,3,0),
            (0,2,0,2),    
            (42,0,0,42),    
            (0,0,42,0),    
        ]
#plane tests
def _test_init_plane(a,b,c,d):
    P = Plane(a,b,c,d)
    assert P.a == a    
    assert P.b == b    
    assert P.c == c    
    assert P.d == d
    assert str(P) == f'{P.a}x + {P.b}y + {P.c}z = {P.d}'

def test_init_plane():
    for (a,b,c,d) in T_VALUES:
        _test_init_plane(a,b,c,d) 
    
def test_init_plane_invalid():
    with pytest.raises(PlaneInvalidException):
        Plane(0,0,0,1)

def _test_plane_normal_vector(a,b,c,d):
    P = Plane(a,b,c,d)
    assert np.array_equiv(P.normal_vector(), [a,b,c])

def test_plane_normal_vector():
    for (a,b,c,d) in T_VALUES:
        _test_plane_normal_vector(a,b,c,d) 
    
#plane vector tests
def _test_init_plane_vector(P, R1, R2):
    PV = PlaneVector(P, R1, R2)
    assert np.array_equiv(PV.P, P)    
    assert np.array_equiv(PV.R1, R1)
    assert np.array_equiv(PV.R2, R2)
    assert str(PV) == f'{PV.P} + {lamda}{PV.R1} + {mu}{PV.R2}'

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

