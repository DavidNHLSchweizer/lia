import math
import numpy as np

from lia import LAMBDA, PRECISION, angle, normal_vector
from line import Line, LineConvertor, VectorLine
from plane import Plane, PlaneConvertor, VectorPlane


def vb_2_1_1():
    a = np.array([3,-1,2,0])
    b = np.array([-2,2,4,7])
    print(f'Voorbeeld 2.1.1: a+b={a+b}  a-b={a-b}')

def vb_2_2_1_1():
    a = np.array([3,-1,2,0])
    print(f'Voorbeelden 2.2.1 en 2.2.2: a*3={a*3}\ta/2={a/2}')

def vb_2_3_1():
    a = np.array([3,-1,2,0])
    b = np.array([-2,2,4,7])    
    print(f'Voorbeeld 2.3.1: (a,b)={np.dot(a,b)}')

def vb_2_4_2():
    a = np.array([3,-1,2])
    b = np.array([0,2,-3])    
    result = np.cross(a,b)
    print(f'Voorbeeld 2.4.2: (aXb)={result} check: (a,aXb)={np.inner(a,result)} (b,aXb)={np.inner(b,result)}')
 
def vb_2_5_1():
    a = np.array([3,-1,2,0])
    len = np.linalg.norm(a)
    print(f'Voorbeeld 2.5.1: lengte={len:.3f} (check: sqrt(14)={math.sqrt(14):.3f})')

def vb_2_6_1():
    a = np.array([4,0,7,-4,1])
    len = np.linalg.norm(a)
    print(f'Voorbeeld 2.6.1: lengte={len:.3f} (check: sqrt(82)={math.sqrt(82):.3f})   w_unit={a/len}   check:sqrt(82)*w_unit={math.sqrt(82)*a/len}')

def _print_angle(v1, v2, msg):
    print(f'{msg}: hoek={angle(v1, v2):.1f}')

def vb_2_7_1():
    _print_angle([1,2], [2,-3], 'Voorbeeld 2.7.1')

def vb_2_7_2():
    _print_angle([3,-1,2], [0, 2,-3], 'Voorbeeld 2.7.2')

def vb_2_8_2():
    VL = VectorLine([0,7], [1,2])
    L = LineConvertor().line_from_vector_line(VL)
    print(f'Voorbeeld 2.8.2: vergelijkingsvorm={L}')

def vb_2_9_2():
    L = Line(2, 7)
    VL = LineConvertor().vector_line_from_line(L)    
    print(f'Voorbeeld 2.9.2: vector={VL}')

def vb_2_10_2():
    l = Line(-1,4)
    m = VectorLine([0,7],[-1,3])
    angle = m.angle(LineConvertor().vector_line_from_line(l))
    print(f'Voorbeeld 2.10.2: angle={angle:.1f}')
def vb_2_10_3():
    l = Line(-1,4)
    m = Line(.5,-2)
    angle = LineConvertor().vector_line_from_line(m).angle(LineConvertor().vector_line_from_line(l))
    print(f'Voorbeeld 2.10.3: angle={angle:.1f}')
def vb_2_10_4():
    l = VectorLine([0,7,-1], [1,2,0])
    m = VectorLine([3,7,0],[-1,3,1])
    print(f'Voorbeeld 2.10.4: angle={m.angle(l):.1f} inner: {np.inner(l.R, m.R)}  len1*len1={math.pow(np.linalg.norm(l.R),2):.3f}  len2*len2={math.pow(np.linalg.norm(m.R),2):.3f}')

def vb_2_11_2():
    P = Plane(-2,4,3,1)
    VP = PlaneConvertor().vector_plane_from_plane(P)
    print(f'Voorbeeld 2.11.2: vectorvorm={VP}')
    VP2 = VectorPlane([-.5,0,0], [2,1,0], [1.5,0,1])
    print(f'controle met oplossing uit boek (is anders): PlaneConvertor berekening: {VP}   receptenboek berekening {VP2}   equivalent: {VP.equivalent(VP2)}')

def vb_2_12_2():
    VP = VectorPlane([-.5,0,0], [2,1,0], [1.5,0,1])
    P = PlaneConvertor().plane_from_vector_plane(VP)
    print(f'Voorbeeld 2.12.2: vergelijkingsvorm={P}')

def vb_2_13_2():
    r = np.array([2,-3])
    n = normal_vector(r)
    print(f'Voorbeeld 2.13.2: r: {r}  normaal: {n}   controle: {round(np.inner(r,n),PRECISION)}')

def vb_2_14_1():
    L = Line(5, -3)
    VL = LineConvertor().vector_line_from_line(L)
    n = VL.normal_vector()
    print(f'Voorbeeld 2.14.1: vector line: {VL} normaal: {n}   controle: {round(np.inner(VL.R,n),PRECISION)}')

def vb_2_14_2():
    VL =VectorLine([0,-3], [1,5])
    n = VL.normal_vector()
    print(f'Voorbeeld 2.14.2: vector line: {VL} normaal: {n}   controle: {round(np.inner(VL.R,n),PRECISION)}')

def vb_2_15():
    L = Line(2, -1)
    VL = LineConvertor().vector_line_from_line(L)
    n = VL.normal_vector()
    LL = VectorLine([3,2], n)
    LL_L = LineConvertor().line_from_vector_line(LL)
    print(f'Voorbeeld 2.15  : loodlijn is {LL_L}.   controle: {L.a * LL_L.a}')

def vb_2_16():
    L1 = Line(2, -1)
    L2 = Line(-1,3)
    intersection = LineConvertor().vector_line_from_line(L1).line_intersection(LineConvertor().vector_line_from_line(L2))
    print(f'Voorbeeld 2.16  : snijpunt {L1} en {L2} is {intersection}')
   
def vb_2_17_3():
    P = Plane(3,2,-4,8)
    print(f'Voorbeeld 2.17.3  : normaalvector is {P.normal_vector()}')  
def vb_2_17_4():
    P = Plane(3,2,4,-8)
    print(f'Voorbeeld 2.17.4  : normaalvector is {P.normal_vector()}')  
def vb_2_17_5():
    VP = VectorPlane([4,1,0], [2,0,-1], [3,1,3])
    print(f'Voorbeeld 2.17.5  : normaalvector is {VP.normal_vector()}')  

def vb_2_18_1():
    P = Plane(1,-1,2,3)
    n = P.normal_vector()
    L = VectorLine([2,0,-1], n)
    print(f'Voorbeeld 2.18.1  : loodlijn is {L}')  

def vb_2_19_2():
    L = VectorLine([1,0,2],[-1,2,1])
    P = Plane(1,2,-2,4)
    VP = PlaneConvertor().vector_plane_from_plane(P)
    snijpunt = VP.line_intersection(L)
    print(f'Voorbeeld 2.19.2  : vector plane = {VP}  {LAMBDA}={L.labda(snijpunt)}  snijpunt is {snijpunt}')  

def _vb_2_20(msg, p, VP):
    P = PlaneConvertor().plane_from_vector_plane(VP)
    L = VectorLine(p,VP.normal_vector())
    snijpunt = VP.line_intersection(L)
    distance=np.linalg.norm(p-snijpunt)
    print(f'{msg}: Plane= {P} Loodlijn= {L} {LAMBDA}={L.labda(snijpunt):.3f}  snijpunt is {snijpunt}   afstand={distance:.3f} (squared: {distance*distance:.3f})')  

def vb_2_20_1():
    _vb_2_20('Voorbeeld 2.20.1',[3,6,7], VectorPlane([5,0,3], [-1,-1,1], [3,5,-6]))
def vb_2_20_2():
    _vb_2_20('Voorbeeld 2.20.2',[-3,1,7], VectorPlane([-1,-2,0], [-5,-8,3], [2,3,-1]))

def vb_hfst_2():
    vb_2_1_1()
    vb_2_2_1_1()
    vb_2_3_1()
    vb_2_4_2()
    vb_2_5_1()
    vb_2_6_1()
    vb_2_7_1()
    vb_2_7_2()
    vb_2_8_2()
    vb_2_9_2()
    vb_2_10_2()
    vb_2_10_3()
    vb_2_10_4()
    vb_2_11_2()
    vb_2_12_2()
    vb_2_13_2()
    vb_2_14_1()
    vb_2_14_2()
    vb_2_15()
    vb_2_16()
    vb_2_17_3()
    vb_2_17_4()
    vb_2_17_5()
    vb_2_18_1()
    vb_2_19_2()
    vb_2_20_1()
    vb_2_20_2()


if __name__ == '__main__':
    print('*** VOORBEELDEN HOOFDSTUK 2 ***')
    vb_hfst_2()
    print('*** EINDE ***')
