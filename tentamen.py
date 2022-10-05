import math
import numpy as np
import quaternion
from line import VectorLine
from plane import Plane, VectorPlane
from transformations import Axis, axis_rotation_matrix, plane_mirror_matrix, plane_projection_matrix

def opgave1():
    a = [3,-2,0]
    b = [-2,0,1]
    c = np.cross(a, b)
    print(f'opgave1a: {c}')
    print(f'opgave1b: inproduct van c en a is {np.dot(c,a)}')
    vlak_c = VectorPlane([2,    1,-3], [3,-2,0], [-2,0,1])
    P = np.array([2,1,0])
    snijpunt=vlak_c.line_intersection(VectorLine(P, c))
    distance=np.linalg.norm(snijpunt-P)
    print(f'opgave 1c: afstand: {distance:.3f}')

def opgave2():
    vlak = Plane(2,-1,0,0)
    P = plane_projection_matrix(vlak)
    print(f'opgave 2a (*5):\n{P*5}')
    S = plane_mirror_matrix(vlak)
    print(f'opgave 2b (*5):\n{S*5}')
    B = np.dot(S,P)
    print(f'opgave 2c (*5):\n{B*5}')

def qstr(q):
    return(f'{q.w:.3f} + {q.x:.3f}i + {q.y:.3f}j + {q.z:.3f}k')

def opgave3():
    p = np.quaternion(0, 2, 0,-1)    
    print(f'opgave 3a: {qstr(p)}')
    cos45= math.cos(math.radians(45))
    sin45= math.sin(math.radians(45))
    qr = np.quaternion(cos45, -4.0/5*sin45, 0, 3.0/5*sin45)
    print(f'opgave 3b: {qstr(qr)}')
    qrT = np.quaternion(cos45, +4.0/5*sin45, 0, -3.0/5*sin45)
    print(f'opgave 3c: {qstr(qrT)}')
    qrT_P = np.multiply(p, qrT)
    print(f'opgave 4a(1): {qstr(qrT_P)}')
    

def opgave4():
    M = np.array([[3,7,-1],[4,2,0],[0,1,-2]])
    print(f'opgave 4a: {np.linalg.det(M)}')


    


def tentamen():
    opgave1()
    opgave2()
    opgave3()
    opgave4()

if __name__=='__main__':
    tentamen()