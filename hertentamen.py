import math
import numpy as np
from determinant import Determinant, simplify_determinant
from lia import LAMBDA
from line import VectorLine
from plane import Plane, PlaneConvertor, VectorPlane
from transformations import AffineMatrix, TranslationMatrix, plane_mirror_matrix, plane_projection_matrix
from quaternion import QU, PointQuaternion, Quaternion, QuaternionTable, RotationQuaternion

#tentamen toetsweek T2b 2022 (ergens in januari 2023)
def opgave1():
    print(f'*** OPGAVE 1 ***')
    a = [4,-3,5]
    b = [4,-2,3]
    c = np.cross(a, b)
    print(f'opgave1a: {c}')
    print(f'opgave1b: inproduct van c en a is {np.dot(c,a)}')
    vlak_c = VectorPlane([1,-1,4], [4,-3,5], [4,-2,3])
    P = np.array([0,2,2])
    L = VectorLine(P, c)
    print(f'opgave 1c:\n\tvlak: {PlaneConvertor().plane_from_vector_plane(vlak_c)}    lijn: {L}')
    snijpunt=vlak_c.line_intersection(L)
    print(f'\tsnijpunt: {np.around(snijpunt, 3)} ({LAMBDA} (factor: 29): {29*L.labda(snijpunt):.3f})')

    distance=np.linalg.norm(snijpunt-P)
    print(f'\tafstand: {distance:.3f}')

def opgave2():
    print(f'\n*** OPGAVE 2 ***')
    P = np.array([[2,4,0],[3,7,0],[0,0,1]])
    print(f'opgave 2a: spiegelingsmatrix:')
    S = 2*P-np.eye(3)
    print(S)
    t = np.array([1,-1,5]) - np.array([-1,2,4])
    print(f'\nopgave 2b: {t}')

    Ta = TranslationMatrix(t)
    print(f'\nopgave 2c:\n{Ta}')
    print(f'\nopgave 2d:')
    Sa = AffineMatrix(S)
    Pa = AffineMatrix(P)
    print (f'affiene matrix Sa: \n{Sa}\naffiene matrix Pa: \n{Pa}')
    print (f'Ta*Sa\n{np.dot(Ta,Sa)}')
    g = np.dot(Ta,Sa)
    C = np.dot(Pa,g)
    print (f'C=Pa*Sa*Ta\n{C}')
    d = AffineMatrix(C, True).transform([2,-1,3])
    print(d)

def opgave3():
    print(f'\n*** OPGAVE 3 ***')
    M = np.array([[1,4,3,-7],[4,-5,1,0],[-3,-12,-9,21],[2,-1,0,8]])
    print(f'opgave 3a: {round(np.linalg.det(M),5)}')
    print('met eerst vereenvoudiging matrix:')
    simplify_determinant(Determinant(M))

 

def opgave4():
    print(f'\n*** OPGAVE 4 ***')
    p = PointQuaternion([0, 1,-2])    
    print(f'opgave 4a: {p}')
    v = [1,0,2]
    qr = RotationQuaternion(180, v)
    sin90 = math.sin(math.radians(90))
    print(f'opgave 3b: {qr} (unit vector: {qr.unit_vector}   ... sin 90  * unit: {np.around(sin90 * qr.unit_vector,3)})')
    qrT = qr.conjugate()
    print(f'opgave 3c: {qrT}')
    P_qrT = p*qrT
    print(f'opgave 3d(1):')
    print(f'tabel p * qrT ({P_qrT}):\n', QuaternionTable(p,qrT))
    qr_P_qrT=qr*P_qrT   
    print(f'tabel qr * p * qrT ({qr_P_qrT}):\n', QuaternionTable(qr, P_qrT))    
    print(f'de afbeelding van P wordt dus {[round(qr_P_qrT[qu],6) for qu in QU if qu is not qu.R]}')
    print(f'controle via PointQuaternion.transform: {np.around(p.transform(qr),3)}')
    print(f'--- andersom uitgerekend ---')
    qr_P = qr * p
    print(f'tabel qr * p ({qr_P}):\n', QuaternionTable(qr, p))
    print(f'tabel qr * p * qrT ({qr_P_qrT}):\n', QuaternionTable(qr_P, qrT))
   
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