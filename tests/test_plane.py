import pytest
import numpy as np
from plane import Plane, PlaneInvalidException

#plane tests
def _test_init_plane(a,b,c,d):
    P = Plane(a,b,c,d)
    assert P.a == a    
    assert P.b == b    
    assert P.c == c    
    assert P.d == d
    assert str(P) == f'{P.a}x + {P.b}y + {P.c}z = {P.d}'

t_values = [
            (1,2,3,4),    
            (1,-2,3,0),
            (0,2,0,2),    
            (42,0,0,42),    
            (0,0,42,0),    
        ]
def test_init_plane():
    for (a,b,c,d) in t_values:
        _test_init_plane(a,b,c,d) 
    
def test_init_plane_invalid():
    with pytest.raises(PlaneInvalidException):
        Plane(0,0,0,1)

def _test_plane_normal_vector(a,b,c,d):
    P = Plane(a,b,c,d)
    assert np.array_equiv(P.normal_vector(), [a,b,c])

def test_plane_normal_vector():
    for (a,b,c,d) in t_values:
        _test_plane_normal_vector(a,b,c,d) 
    
