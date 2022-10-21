from cmath import exp
import itertools
import math
import random
from re import L
import pytest
import numpy as np
from lia import LAMBDA, MU, PRECISION, Axis
from line import VectorLine
from plane import Plane, PlaneConvertor, PlaneInvalidException, VectorPlane
from lia_test_const import _TEST_VALUES, _TEST_VECTORS_2D, _TEST_VECTORS_3D, ABCD_VALUES, LABDA_MU_VALUES, TEST_PLANES

#Plane tests
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
    assert round(P.a, PRECISION) != 0 ^ P.is_parallel(Axis.x)
    assert round(P.b, PRECISION) != 0 ^ P.is_parallel(Axis.y)
    assert round(P.c, PRECISION) != 0 ^ P.is_parallel(Axis.z)

def test_parallel():
    for (a,b,c,d) in ABCD_VALUES:
        _test_parallel(Plane(a,b,c,d))

def test_plane_z():
    for (a,b,c,d) in ABCD_VALUES:
        _test_plane_z(Plane(a,b,c,d))

def __test_is_on_plane(P:Plane, x, y, z):
    assert P.is_on_plane(x, y, z)
    if P.is_parallel(Axis.x):
        assert P.is_on_plane(x+0.1, y, z)
    else:
        assert not P.is_on_plane(x+0.1, y, z)
    if P.is_parallel(Axis.y):
        assert P.is_on_plane(x, y+0.1, z)
    else:
        assert not P.is_on_plane(x, y+0.1, z)
    if P.is_parallel(Axis.z):
        assert P.is_on_plane(x, y, z-0.1)
    else:
        assert not P.is_on_plane(x, y, z-0.1)

def _test_is_on_plane(P:Plane):
    if not P.is_parallel(Axis.z):
        for (x,y) in itertools.combinations(_TEST_VALUES, 2):
            __test_is_on_plane(P, x, y, P.z(x,y))

def test_is_on_plane():
    for (a,b,c,d) in ABCD_VALUES:
        _test_is_on_plane(Plane(a,b,c,d))

def _test_is_parallel(a,b,c,d,px,py,pz):
    P = Plane(a,b,c,d)
    assert P.is_parallel(Axis.x) == px
    assert P.is_parallel(Axis.y) == py
    assert P.is_parallel(Axis.z) == pz

def test_is_parallel():
    for tpp in TEST_PLANES: 
        _test_is_parallel(tpp['a'],tpp['b'],tpp['c'],tpp['d'], tpp['px'],tpp['py'],tpp['pz'])

def _test_plane_equivalent(P1, P2: Plane, expected=True):
    assert P1.equivalent(P2) == expected
    assert P2.equivalent(P1) == expected

def test_plane_equivalent_factor():
    for tp in TEST_PLANES:
        P = Plane(tp['a'],tp['b'],tp['c'],tp['d'])
        for factor in [-math.pi, -2, -1, -0.1, 0.1, 1, 2, math.pi]:
            _test_plane_equivalent(P, Plane(factor*tp['a'],factor*tp['b'],factor*tp['c'],factor*tp['d']))  
def test_plane_equivalent_factor_false():
    for tp in TEST_PLANES:
        P = Plane(tp['a'],tp['b'],tp['c'],tp['d'])
        for factor in [-math.pi, -2, -1, -0.1, 0.1, 1, 2, math.pi]:
            _test_plane_equivalent(P, Plane(factor*tp['a']+.01, factor*tp['b'],factor*tp['c'],factor*tp['d']-0.01), False)  

#plane vector tests
def _test_init_plane_vector(P, R1, R2):
    VP = VectorPlane(P, R1, R2)
    assert np.array_equiv(VP.P, P)    
    assert np.array_equiv(VP.R1, R1)
    assert np.array_equiv(VP.R2, R2)
    assert str(VP) == f'{VP.P} + {LAMBDA}{VP.R1} + {MU}{VP.R2}'

def test_init_plane_vector():
    _test_init_plane_vector([1,2,3], [2,4,6], [7,8,9])
    
def test_init_plane_vector_invalid1():
    with pytest.raises(PlaneInvalidException):
        VectorPlane([1,2], [2,4,6], [7,8,9])
    with pytest.raises(PlaneInvalidException):
        VectorPlane([1,2,3], [2,6], [7,8,9])
    with pytest.raises(PlaneInvalidException):
        VectorPlane([1,2,3], [2,4,6], [7,8])

def test_init_plane_vector_invalid2():
    with pytest.raises(PlaneInvalidException):
        VectorPlane([0,0,0], [1,0,0], [2,0,0])
    with pytest.raises(PlaneInvalidException):
        VectorPlane([0,0,0], [1,0,0], [-1,0,0])

def test_init_plane_vector_invalid3():
    with pytest.raises(PlaneInvalidException):
        VectorPlane([0,0,0], [0,0,0], [2,0,0])
    with pytest.raises(PlaneInvalidException):
        VectorPlane([0,0,0], [1,0,0], [0,0,0])

def _test_plane_vector_normal_vector(VP: VectorPlane, expected_vector):
    assert np.array_equiv(VP.normal_vector(), expected_vector)

def test_plane_vector_normal_vector():
    _test_plane_vector_normal_vector(VectorPlane([1,2,3], [1,0,0], [0,1,0]), [0,0,1])
    _test_plane_vector_normal_vector(VectorPlane([1,2,3], [1,2,3], [3,4,5]), [-2,4,-2])

def __test_plane_vector_V(VP, labda, mu):
    assert np.allclose(VP.V(labda,mu), [VP.P[i]+labda*VP.R1[i]+mu*VP.R2[i] for i in range(3)])

def _test_plane_vector_V(VP):
    for labda in LABDA_MU_VALUES:
        for mu in LABDA_MU_VALUES:
            __test_plane_vector_V(VP, labda, mu)

def test_plane_vector_V():
    _test_plane_vector_V(VectorPlane([1,2,3], [1,0,0], [0,1,0]))
    _test_plane_vector_V(VectorPlane([1,2,3], [1,2,3], [3,4,5]))

def _test_is_parallel_vector(P, R1, R2, px,py,pz):
    VP = VectorPlane(P, R1, R2)
    assert VP.is_parallel(Axis.x) == px
    assert VP.is_parallel(Axis.y) == py
    assert VP.is_parallel(Axis.z) == pz

def test_is_parallel_vector():
    for tpp in TEST_PLANES: 
        _test_is_parallel_vector(tpp['P'],tpp['R1'],tpp['R2'],tpp['px'],tpp['py'],tpp['pz'])

def __test_is_on_plane_vector(VP:VectorPlane, vector):
    assert VP.is_on_plane(vector)
    if VP.is_parallel(Axis.x):
        assert VP.is_on_plane([vector[0]+0.1, vector[1], vector[2]])
    else:
        assert not VP.is_on_plane([vector[0]+0.1, vector[1], vector[2]])
    if VP.is_parallel(Axis.y):
        assert VP.is_on_plane([vector[0], vector[1]+0.1, vector[2]])
    else:
        assert not VP.is_on_plane([vector[0], vector[1]+0.1, vector[2]])
    if VP.is_parallel(Axis.z):
        assert VP.is_on_plane([vector[0], vector[1], vector[2]+0.1])

    else:
        assert not VP.is_on_plane([vector[0], vector[1], vector[2]+0.1])

def _test_is_on_plane_vector(VP:VectorPlane):
    P = PlaneConvertor().plane_from_vector_plane(VP)
    for labda in LABDA_MU_VALUES:
        for mu in LABDA_MU_VALUES:
            __test_is_on_plane_vector(VP, VP.V(labda, mu))

def test_is_on_plane_vector():
    for tp in TEST_PLANES:
        _test_is_on_plane_vector(VectorPlane(tp['P'], tp['R1'], tp['R2']))

def _test_line_intersection_vector(VP: VectorPlane, VL: VectorLine):
    intersection = VP.line_intersection(VL)
    if intersection is not None:
        assert VP.is_on_plane(intersection)
        assert VL.is_on_line(intersection)
    else:
        assert abs(np.inner(VP.normal_vector(),VL.R)) < PRECISION

def test_line_intersection_vector():
    lines = []
    for P,R in zip(_TEST_VECTORS_3D(10), _TEST_VECTORS_3D(10)):
        lines.append(VectorLine(P,R))
    for tp in TEST_PLANES:
        VP = VectorPlane(tp['P'], tp['R1'], tp['R2'])
        for line in lines:
            _test_line_intersection_vector(VP,line)  
        _test_line_intersection_vector(VP, VectorLine([VP.P[0]+1,VP.P[1]+1,VP.P[2]+1], VP.R1))      
        _test_line_intersection_vector(VP, VectorLine([VP.P[0]+1,VP.P[1]+1,VP.P[2]+1], VP.R2))      

def _test_vector_plane_equivalent(VP1, VP2: VectorPlane, expected=True):
    assert VP1.equivalent(VP2) == expected
    assert VP2.equivalent(VP1) == expected

def test_vector_plane_equivalent_factor():
    for tp in TEST_PLANES:
        VP = VectorPlane(tp['P'], tp['R1'], tp['R2'])
        for factor in [-math.pi, -2, -1, -0.1, 0.1, 1, 2, math.pi]:
            _test_vector_plane_equivalent(VP, VectorPlane(tp['P'], factor*np.array(tp['R1']), factor*np.array(tp['R2'])))  

def test_vector_plane_equivalent_switch():
    for tp in TEST_PLANES:
        VP = VectorPlane(tp['P'], tp['R1'], tp['R2'])
        for factor in [-math.pi, -2, -1, -0.1, 0.1, 1, 2, math.pi]:
            _test_vector_plane_equivalent(VP, VectorPlane(tp['P'], factor*np.array(tp['R2']), factor*np.array(tp['R1'])))  

def test_vector_plane_equivalent_false_vector():
    def tilt_vector(VP, V):
        n = np.array(VP.normal_vector())
        v = V.copy()
        while round(np.inner(n,v),PRECISION) == 0:
            v[0] = v[0]+1.1 * random.random()
            v[1] = v[1]-1.1 * random.random()
            v[2] = v[2]+1.1 * random.random()
        return v
    for tp in TEST_PLANES:
        VP = VectorPlane(tp['P'], tp['R1'], tp['R2'])        
        _test_vector_plane_equivalent(VP, VectorPlane(np.array(tp['P']), tilt_vector(VP, np.array(tp['R1'])), np.array(tp['R2'])), False)  

def test_vector_plane_equivalent_false_point():
    def shift_vector(VP, P):
        p = P.copy()
        while VP.is_on_plane(p):
            p[0] = p[0]+1.1 * random.random()
            p[1] = p[1]-1.1 * random.random()
            p[2] = p[2]+1.1 * random.random()
        return p
    for tp in TEST_PLANES:
        VP = VectorPlane(tp['P'], tp['R1'], tp['R2'])        
        _test_vector_plane_equivalent(VP, VectorPlane(shift_vector(VP, np.array(tp['P'])), np.array(tp['R1']), np.array(tp['R2'])), False)  

#plane convertor tests
def _test_plane_convertor_vector_to_plane(VP: VectorPlane, expected: Plane):
    P = PlaneConvertor().plane_from_vector_plane(VP)
    assert P.equivalent(expected)
    assert expected.equivalent(P)

def test_plane_convertor_vector_to_plane():
    for tp in TEST_PLANES:
        _test_plane_convertor_vector_to_plane(VectorPlane(tp['P'], tp['R1'], tp['R2']), Plane(tp['a'],tp['b'],tp['c'],tp['d']))

def _test_plane_convertor_plane_to_vector(P: Plane, expected: VectorPlane):
    VP = PlaneConvertor().vector_plane_from_plane(P)
    assert VP.equivalent(expected)
    assert expected.equivalent(VP)

def test_plane_convertor_plane_to_vector():
    for tp in TEST_PLANES:
        _test_plane_convertor_plane_to_vector(Plane(tp['a'],tp['b'],tp['c'],tp['d']), VectorPlane(tp['P'], tp['R1'], tp['R2']))