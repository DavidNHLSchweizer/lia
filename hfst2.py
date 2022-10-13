import numpy as np
import math
from lia import DEGREES, angle

from line import Line, LineConvertor, VectorLine
from plane import Plane, PlaneConvertor, VectorPlane
xyz = ['x', 'y', 'z']

def _opgave1(a, b, msg):
    a = np.array(a)
    b = np.array(b)
    print(f'{msg}\n\ta+b={np.add(a,b)}  a-b={np.subtract(a,b)}   (a,b)={np.inner(a,b)}')


def _opgave2(l1: Line, lv1: VectorLine, msg):
    angle = lv1.angle(LineConvertor().vector_line_from_line(l1))
    print(f'{msg}\n\tangle={round(angle, 1)}{DEGREES}')    
  
def _opgave3(v, msg):
    v = np.array(v)
    print(f'{msg}\n\tlength={round(np.linalg.norm(v), 2)}')
    
def _opgave4(v, msg):
    print(f'{msg}\n\tvector: {v}  scaled: {v / np.linalg.norm(v)}')

def _bereken_afstand_punt_vlak(point, plane: VectorPlane, msg):
    line = VectorLine(point, plane.normal_vector())
    intersection = plane.line_intersection(line)
    print(f'{msg}\n\tdistance:{np.linalg.norm(intersection-point):.2f}')

def vb_2_1():
    print(f'hoofdstuk 2.1:\n\tsom in R3: {np.array([3,-1,2])+np.array([0,6,-4])}\n\tsom in R2: {np.array([-3,6])+np.array([7,2])}')
    print(f'\tscalair product: {-2*np.array([-4,-3])}')
    print(f'\tverschil in R3: {np.array([3,-1,2])-np.array([0,6,-4])}\n\tverschil in R2: {np.array([-3,6])-np.array([7,2])}')
    print(f'\t inproduct: {np.dot([3,-2,2],[0,6,-4])}')
    a = [-1,2,4]
    b = [3,-2,1]
    aXb=np.cross(a,b)
    print(f'\tuitproduct: {aXb} [check: (a,c)={np.dot(a,aXb)} en (b,c)={np.dot(b,aXb)}]')

def vb_2_2():
    v = [3,1,-3,4,-1]
    l_v = np.linalg.norm(v)
    print(f'hoofdstuk 2.2:\n\tnorm([3,4]) is {np.linalg.norm([3,4])} en norm({v}) is {l_v}')
    print(f'eenheidsvector: lengte is {l_v} dus unit vector wordt {v/l_v}')
    print(f'\thoek vectoren: {angle([2,-2,1],[-3,0,4]):.1f}{DEGREES}')
def vb_2_3_3():    
    print(f'hoofdstuk 2.3.3:\n\tvectorlijn->vergelijking {LineConvertor().line_from_vector_line(VectorLine([1,2],[-2,1]))}')
    vl = LineConvertor().vector_line_from_line(Line(3,-2))
    print(f'\tvergelijking->vectorlijn {vl}. Punt (0,-2) (steunvector in dictaat) ligt op die lijn: {vl.is_on_line([0,-2])}')
def vb_2_3_4():
    print(f'hoofdstuk 2.3.4:\n\tvergelijking->vectorvlak {PlaneConvertor().vector_plane_from_plane(Plane(-1,2,-2,6))}')
    print(f'\tvectorvlak->vergelijking {PlaneConvertor().plane_from_vector_plane(VectorPlane([1,3,6],[0,2,1],[1,1,2]))}')
def vb_2_5():
    _bereken_afstand_punt_vlak(np.array([3,6,7]), VectorPlane([5,0,3], [-1,-1,1], [3,5,-6]), 'voorbeeld 2.5 (berekening afstand punt/vlak)')
def vb_2_5_1():
    _bereken_afstand_punt_vlak(np.array([-3,1,7]), VectorPlane([-1,-2,0], [-5,-8,3], [2,3,-1]), 'extra voorbeeld 2.5.1 (berekening afstand punt/vlak)')

def hfst2_voorbeelden():
    vb_2_1()
    vb_2_2()
    vb_2_3_3()
    vb_2_3_4()
    vb_2_5()
    vb_2_5_1()

def opgave1():
    _opgave1([3,-1,2,0], [-2,2,4,7], 'opgave 1')
def opgave2():
    _opgave2(Line(2,7), VectorLine([-3,7], [2,-3]), 'opgave 2')           
def opgave3():
    _opgave3([2,-3,0,2,-5], 'opgave 3')
def opgave4():
    _opgave4([-1,5,7,0,5], 'opgave 4')
def opgave5():
    _bereken_afstand_punt_vlak(np.array([7,1,2]), PlaneConvertor().vector_plane_from_plane(Plane(2,-4,2,-2)), 'opgave 5')
def opgave6():    
    _bereken_afstand_punt_vlak(np.array([7,0,-2]), VectorPlane([8,-5,3], [3,-2,1], [-5,3,-2]), 'opgave 6')

def hfst2_opgaven():
    opgave1()
    opgave2()
    opgave3()
    opgave4()
    opgave5()
    opgave6()
    

def opgave1_extra():
    _opgave1([3,-2,0,5], [1,7,-2,2], 'extra opgave 1')
def opgave2_extra():
    _opgave2(Line(3,1), VectorLine([0,0], [4,-3]), 'extra opgave 2')        
def opgave3_extra():
    _opgave3([4,0,7,-4,1], 'extra opgave 3')
def opgave4_extra():
    _bereken_afstand_punt_vlak(np.array([-1,-4,-1]), PlaneConvertor().vector_plane_from_plane(Plane(-2,9,6,1/3.0)), 'extra opgave 4')
def opgave5_extra():
    _bereken_afstand_punt_vlak(np.array([-3,9,-3]), VectorPlane([0,0,0], [4,2,4], [7,-1,-3]), 'extra opgave 5')

def hfst2_extra():
    opgave1_extra()
    opgave2_extra()
    opgave3_extra()
    opgave4_extra()
    opgave5_extra()

def hfst2():
    print('HOOFDSTUK 2\n')  
    print('VOORBEELDEN')
    hfst2_voorbeelden()
    print('OPGAVEN')
    hfst2_opgaven()
    print('EXTRA OPGAVEN')
    hfst2_extra()
    print('*** EINDE ***')
    
if __name__ == '__main__':
    hfst2()

