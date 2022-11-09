import math
import numpy as np
from lia import LAMBDA
from line import VectorLine
from plane import Plane, PlaneConvertor, VectorPlane
from transformations import plane_mirror_matrix, plane_projection_matrix
from quaternion import QU, PointQuaternion, Quaternion, QuaternionTable, RotationQuaternion

#tentamen toetsweek T1 2022 (3 november 2022)
def opgave1():
    print(f'*** OPGAVE 1 ***')
    a = [3,-2,0]
    b = [-2,0,1]
    c = np.cross(a, b)
    print(f'opgave1a: {c}')
    print(f'opgave1b: inproduct van c en a is {np.dot(c,a)}')
    vlak_c = VectorPlane([2,    1,-3], [3,-2,0], [-2,0,1])
    P = np.array([2,1,0])
    L = VectorLine(P, c)
    print(f'opgave 1c:\n\tvlak: {PlaneConvertor().plane_from_vector_plane(vlak_c)}    lijn: {L}')
    snijpunt=vlak_c.line_intersection(L)
    print(f'\tsnijpunt: {np.around(snijpunt, 3)} ({LAMBDA} (factor: 29): {29*L.labda(snijpunt):.3f})')

    distance=np.linalg.norm(snijpunt-P)
    print(f'\tafstand: {distance:.3f}')

def opgave2():
    print(f'\n*** OPGAVE 2 ***')
    vlak = Plane(2,-1,0,0)
    print(f'opgave 2a:\n\tvlak: {vlak}   normaal: {vlak.normal_vector()}')
    P = plane_projection_matrix(vlak)
    print(f'\tmatrix:\n{P*5}')
    S = plane_mirror_matrix(vlak)
    print(f'opgave 2b (*5):\n{S*5}')
    B = np.dot(S,P)
    print(f'opgave 2c (*5):\n{B*5}')

def opgave3():
    print(f'\n*** OPGAVE 3 ***')
    p = PointQuaternion([2, 0,-1])    
    print(f'opgave 3a: {p}')
    v = [-4,0,3]
    qr = RotationQuaternion(90, v)
    sin45 = math.sin(math.radians(45))
    print(f'opgave 3b: {qr} (unit vector: {qr.unit_vector}   ... sin 45  * unit: {np.around(sin45 * qr.unit_vector,3)})')
    qrT = qr.conjugate()
    print(f'opgave 3c: {qrT}')
    P_qrT = p*qrT
    print(f'opgave 3d(1):')
    print(f'tabel p * qrT ({P_qrT}):\n', QuaternionTable(p,qrT))
    qr_P_qrT=qr*P_qrT   
    print(f'tabel qr * p * qrT ({qr_P_qrT}):\n', QuaternionTable(qr, P_qrT))    
    print(f'de afbeelding van P wordt dus {[round(qr_P_qrT[qu],6) for qu in QU if qu is not qu.R]}')
    print(f'controle via PointQuaternion.transform: {p.transform(qr)}')
    print(f'--- andersom uitgerekend ---')
    qr_P = qr * p
    print(f'tabel qr * p ({qr_P}):\n', QuaternionTable(qr, p))
    print(f'tabel qr * p * qrT ({qr_P_qrT}):\n', QuaternionTable(qr_P, qrT))
    

def opgave4():
    print(f'\n*** OPGAVE 4 ***')
    M = np.array([[3,7,-1],[4,2,0],[0,1,-2]])
    print(f'opgave 4a: {round(np.linalg.det(M),5)}')

def tentamen(select=[1,2,3,4]):
    if 1 in select: 
        opgave1()
    if 2 in select: 
        opgave2()
    if 3 in select: 
        opgave3()
    if 4 in select: 
        opgave4()

if __name__=='__main__':
    tentamen([2])