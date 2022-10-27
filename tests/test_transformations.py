import numpy as np
from line import Line, VerticalLine
from plane import Plane
from transformations import line_mirror, line_projection, line_projection_matrix, plane_projection

#test line projections
def _test_line_projection(X: np.array, L: Line, expected)->np.array:
    assert np.allclose(line_projection(X, L), expected)

A_TEST_CASES= [-10,-5,-2,-0.3, -0.1, 0.1, 0.3, 2,5, 10]

def test_line_projection():
    for a in A_TEST_CASES:
        asq=a*a
        asq_1=a*a+1.
        L = Line(a,0)
        _test_line_projection([1,0], L, [1/asq_1, a/asq_1])
        _test_line_projection([0,1], L, [a/asq_1, asq/(asq_1)])

def test_vertical_line_projection():
    L = VerticalLine(0)
    _test_line_projection([1,0], L, [0,0])
    _test_line_projection([0,1], L, [0,1])

#test line mirrors
def _test_line_mirror(X: np.array, L: Line, expected)->np.array:
    assert np.allclose(line_mirror(X,L), expected)

def test_line_mirror():
    for a in A_TEST_CASES:
        asq=a*a
        asq_1=a*a+1.
        L = Line(a,0)
        _test_line_mirror([1,0], L, [(1-asq)/asq_1, 2*a/asq_1])
        _test_line_mirror([0,1], L, [2*a/asq_1, (asq-1)/asq_1])

def test_vertical_line_mirror():
    L = VerticalLine(0)
    _test_line_mirror([1,0], L, [-1,0])
    _test_line_mirror([0,1], L, [0,1])

def _test_line_projection_matrix(L):
    assert np.allclose(line_projection_matrix(L), [line_projection([1,0], L), line_projection([0,1], L)])

def test_line_projection_matrix():
    for a in A_TEST_CASES:
        _test_line_projection_matrix(Line(a,0))

def test_vertical_line_projection_matrix():
    _test_line_projection_matrix(VerticalLine(0))

#test plane projections
def _test_plane_projection(X: np.array, P: Plane, expected: np.array):
    assert np.allclose(plane_projection(X, P), expected)

