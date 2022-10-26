import pytest
import math
import numpy as np
from lia import PRECISION, LiaException, angle, normal_vector, vector_equivalent

#angle testing
def _test_angle(V1, V2, degrees, expected):
    assert round(angle(V1, V2, degrees)-expected, PRECISION) == 0

def _test_angle_degrees(testcases):
    for testcase in testcases:
        _test_angle(testcase['V1'], testcase['V2'], True, testcase['expected'])
def _test_angle_radians(testcases):
    for testcase in testcases:
        _test_angle(testcase['V1'], testcase['V2'], False, math.radians(testcase['expected']))

TESTCASES2D= [{'V1': [1,0], 'V2':[0,1],'expected': 90},
             {'V1': [1,0], 'V2':[1,1],'expected': 45},
             {'V1': [0,1], 'V2':[1,1],'expected': 45},
             {'V1': [0,1], 'V2':[0,1],'expected': 0},
             {'V1': [1,1], 'V2':[1,1],'expected': 0},
             {'V1': [1,0], 'V2':[math.sqrt(3), 1],'expected': 30},
             {'V1': [1,0], 'V2':[1, math.sqrt(3)],'expected': 60},
            ]

def test_angles_2d_degrees():
    _test_angle_degrees(TESTCASES2D)
def test_angles_2d_radians():
    _test_angle_radians(TESTCASES2D)

TESTCASES3D= [{'V1': [1,0,0], 'V2':[0,1,0],'expected': 90},
             {'V1': [1,0,0], 'V2':[0,0,1],'expected': 90},
             {'V1': [0,1,0], 'V2':[0,0,1],'expected': 90},
             {'V1': [1,0,0], 'V2':[1,0,0],'expected': 0},
             {'V1': [1,0,0], 'V2':[2,0,0],'expected': 0},
             {'V1': [0,1,0], 'V2':[0,1,0],'expected': 0},
             {'V1': [0,0,1], 'V2':[0,0,1],'expected': 0},
             {'V1': [1,0,0], 'V2':[0,1,1],'expected': 90},
             {'V1': [1,0,0], 'V2':[1,1,0],'expected': 45},
             {'V1': [1,0,0], 'V2':[1,0,1],'expected': 45},
             {'V1': [0,1,0], 'V2':[0,1,1],'expected': 45},
             {'V1': [0,0,1], 'V2':[0,1,1],'expected': 45},
             {'V1': [1,0,0], 'V2':[1,math.sqrt(3),0],'expected': 60},
             {'V1': [0,1,0], 'V2':[0,math.sqrt(3),1],'expected': 30},
            ]
def test_angles_3d_degrees():
    _test_angle_degrees(TESTCASES3D)

def test_angles_3d_radians():
    _test_angle_radians(TESTCASES3D)

TESTCASESINV=[{'V1': [1],   'V2':[0,1]},
             {'V1': [1,0], 'V2':[1,1,2]},
             {'V1': [0,1,1], 'V2':[1,1,2,3]},
            ]
def test_angles_invalid():
    for testcase in TESTCASESINV:
        with pytest.raises(LiaException):
            _test_angle(testcase['V1'], testcase['V2'],True, None)    

#normal vector testing
def _test_normal(V):
    assert round(np.inner(normal_vector(V), V),PRECISION) == 0
def _test_normal_vector(testcases):
    for testcase in testcases:
        _test_normal(testcase['V'])

NTESTCASES2D= [{'V': [1,0]},
               {'V': [2,0]},
               {'V': [0,1]},
               {'V': [-1,1]},
               {'V': [-1,5]},
               {'V': [5,-12]},
               {'V': [0,-12]},
                ]
def test_normal_vector2d():
    _test_normal_vector(NTESTCASES2D)

NTESTCASES3D= [{'V': [1,0,0]},
               {'V': [2,0,0]},
               {'V': [0,1,0]},
               {'V': [-1,1,0]},
               {'V': [-1,5,-2]},
               {'V': [5,-12,-1]},
               {'V': [0,-12,0]},
               {'V': [1,-12,0]},
               {'V': [1,-12,3]},
                ]
def test_normal_vector3d():
    _test_normal_vector(NTESTCASES3D)

#equivalent_vector tests
def _test_equivalent(V1, V2, expected):
    assert vector_equivalent(V1, V2) == expected

def _test_equivalent_cases(testcases):
    for testcase in testcases:
        _test_equivalent(testcase['V1'], testcase['V2'], testcase['expected'])

EQTESTCASES2D= [{'V1': [1,0], 'V2':[1,0],'expected': True},
             {'V1': [1,0], 'V2':[0,1],'expected': False},
             {'V1': [1,0], 'V2':[-1,0],'expected': True},
             {'V1': [1,0], 'V2':[-1,1],'expected': False},
             {'V1': [1,0], 'V2':[2,0],'expected': True},
             {'V1': [0,1], 'V2':[0,20],'expected': True},
             {'V1': [1,0], 'V2':[3,0],'expected': True},
             {'V1': [1,1], 'V2':[3,3],'expected': True},
             {'V1': [1,1], 'V2':[3,3.1],'expected': False},
             {'V1': [1,3], 'V2':[3,9],'expected': True},
             {'V1': [1,2], 'V2':[-3,-6],'expected': True},
             {'V1': [1,2], 'V2':[-3,6],'expected': False},
             {'V1': [1,2], 'V2':[3,4],'expected': False},
             {'V1': [2,4], 'V2':[3,6],'expected': True},
            ]

EQTESTCASES3D= [{'V1': [1,0,0], 'V2':[1,0,0],'expected': True},
             {'V1': [1,0,0], 'V2':[0,0,1],'expected': False},
             {'V1': [1,0,0], 'V2':[-1,0,0],'expected': True},
             {'V1': [1,0,0], 'V2':[-1,1,0],'expected': False},
             {'V1': [1,0,0], 'V2':[2,0,0],'expected': True},
             {'V1': [0,1,0], 'V2':[0,20,0],'expected': True},
             {'V1': [1,0,1], 'V2':[3,0,3],'expected': True},
             {'V1': [1,0,1], 'V2':[3,0.1,3],'expected': False},
             {'V1': [1,2,3], 'V2':[3,6,9],'expected': True},
             {'V1': [1,2,3], 'V2':[-3,-6,-9],'expected': True},
             {'V1': [1,2,3], 'V2':[-3,6,-9],'expected': False},
             {'V1': [1,2,3], 'V2':[4,5,6],'expected': False},
             {'V1': [2,4,6], 'V2':[3,6,9],'expected': True},
            ]


def test_equivalent_vector2d():
    _test_equivalent_cases(EQTESTCASES2D)

def test_equivalent_vector3d():
    _test_equivalent_cases(EQTESTCASES3D)