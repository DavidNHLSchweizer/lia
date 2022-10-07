import numpy as np
from line import VectorLine
from plane import Plane, VectorPlane
from transformations import plane_mirror_matrix, plane_projection_matrix
from quaternion import QU, PointQuaternion, Quaternion, QuaternionTable, RotationQuaternion

def opgave1():
    print(f'*** OPGAVE 1 ***')
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
    print(f'\n*** OPGAVE 2 ***')
    vlak = Plane(2,-1,0,0)
    P = plane_projection_matrix(vlak)
    print(f'opgave 2a (*5):\n{P*5}')
    S = plane_mirror_matrix(vlak)
    print(f'opgave 2b (*5):\n{S*5}')
    B = np.dot(S,P)
    print(f'opgave 2c (*5):\n{B*5}')

def opgave3():
    print(f'\n*** OPGAVE 3 ***')
    p = PointQuaternion([2, 0,-1])    
    print(f'opgave 3a: {p}')
    qr = RotationQuaternion(90, [-4,0,3])
    print(f'opgave 3b: {qr}')
    qrT = qr.conjugate()
    print(f'opgave 3c: {qrT}')
    P_qrT = p*qrT
    print(f'opgave 3d(1):')
    print(f'tabel p * qrT ({P_qrT}):\n', QuaternionTable(p,qrT).table)
    qr_P_qrT=qr*P_qrT   
    print(f'tabel qr * p * qrT ({qr_P_qrT}):\n', QuaternionTable(qr, P_qrT).table)    
    print(f'de afbeelding van P wordt dus {[round(qr_P_qrT[qu],6) for qu in QU if qu is not qu.R]}')
    print(f'controle via PointQuaternion.transform: {p.transform(qr)}')

def opgave4():
    print(f'\n*** OPGAVE 4 ***')
    M = np.array([[3,7,-1],[4,2,0],[0,1,-2]])
    print(f'opgave 4a: {round(np.linalg.det(M),5)}')

def tentamen():
    opgave1()
    opgave2()
    opgave3()
    opgave4()

if __name__=='__main__':
    tentamen()