import numpy as np
from plane import Plane
from transformations import plane_mirror_matrix


def vb_5_1_2():
    M = plane_mirror_matrix(Plane(2,-1,3,0))
    print(f'matrix: (factor 14)\n{14*M}')
    print(f'determinant is {round(np.linalg.det(M),4)}')
    print(f'controle inverse M*M (moet eenheidsmatrix zijn):\n {np.round(np.dot(M,M))}')

def _vb(M, msg):
    print(f'Voorbeeld {msg}:\nmatrix =\n{M}\ndeterminant = {round(np.linalg.det(M),4)}')
def vb_5_4_1():
    _vb(np.array([[3,2],[4,-1]]), '5.4.1')
def vb_5_5_1():
    _vb(np.array([[3,2,1],[4,-1,0],[-2,4,2]]), '5.5.1')
def vb_5_6_1():
    _vb(np.array([[3,2,1,2],[4,-1,0,5],[-2,4,2,2], [-3,0,-1,1]]), '5.6.1 eindresultaat')
    _vb([[-1,0,5],[4,2,2],[0,-1,1]], 'eerste 3x3')
    _vb([[2,1,2],[4,2,2],[0,-1,1]], 'tweede 3x3')
    _vb([[2,1,2],[-1,0,5],[0,-1,1]], 'derde 3x3')
    _vb([[2,1,2],[-1,0,5],[4,2,2]], 'vierde 3x3')

def vb_5_7_2():
    _vb(np.array([[3,2,1,2],[4,-1,0,5],[-2,4,2,2], [-3,0,-1,1]]), '5.7.2 oorspronkelijk')
    _vb(np.array([[3,2,1,2],[4,-1,0,5],[-2,4,2,2], [0,2,0,3]]), '5.7.2 na stap 1')
    _vb(np.array([[3,2,1,2],[4,-1,0,5],[-8,0,0,-2], [0,2,0,3]]), '5.7.2 na stap 2')
    _vb(np.array([[4,-1,5],[-8,0,-2], [0,2,3]]), '5.7.2 voor stap 3')
    _vb(np.array([[4,-1,5],[-8,0,-2], [8,0,13]]), '5.7.2 na stap 3')
    _vb(np.array([[-8,-2], [8,13]]), '5.7.2 na stap 4')

def vb_5_3_1():
    M = np.array([[1,-1],[2,3]])
    print('Voorbeeld 5.3.1:')
    _vb(M, '5.3.1 (oorspronkelijk)')
    M_inv = np.linalg.inv(M)
    _vb(5*M_inv, '5.3.1 (inverse *5)')
    print(f'controle inverse M*M (moet eenheidsmatrix zijn):\n {np.round(np.dot(M, M_inv),3)}')

def vb_hfst_5():
    vb_5_1_2()
    vb_5_3_1()
    vb_5_4_1()
    vb_5_5_1()
    vb_5_6_1()
    vb_5_7_2()

if __name__ == '__main__':
    print('*** VOORBEELDEN HOOFDSTUK 5 ***')
    vb_hfst_5()
    print('*** EINDE ***')

