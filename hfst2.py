import numpy as np
import math
from line import Line, LineConvertor, LineVector
from plane import Plane, PlaneConvertor, PlaneVector
xyz = ['x', 'y', 'z']



def _opgave1(a, b, msg):
    a = np.array(a)
    b = np.array(b)
    print(msg)
    print('\t', np.add(a,b))
    print('\t', np.subtract(a,b))
    print('\t', np.inner(a,b))


def _opgave2(l1: Line, lv1: LineVector, msg):
    angle = lv1.angle(LineConvertor().vector_from_line(l1))
    print(f'{msg}\t {round(angle, 1)}')    
  
def _opgave3(v, msg):
    v = np.array(v)
    print(msg)
    print('\t', round(np.linalg.norm(v), 2))
    

def _bereken_afstand_punt_vlak(point, plane: PlaneVector, msg):
    line = LineVector(point, plane.normal_vector())
    intersection = plane.line_intersection(line)
    print(msg)
    print(f'\tdistance:{np.linalg.norm(intersection-point):.2f}')

def voorbeeld1():
    _bereken_afstand_punt_vlak(np.array([3,6,7]), PlaneVector([5,0,3], [-1,-1,1], [3,5,-6]), 'voorbeeld blz 20')
def voorbeeld2():
    _bereken_afstand_punt_vlak(np.array([-3,1,7]), PlaneVector([-1,-2,0], [-5,-8,3], [2,3,-1]), 'voorbeeld blz 22')

def opgave1():
    _opgave1([3,-1,2,0], [-2,2,4,7], 'opgave 1')
def opgave2():
    _opgave2(Line(1,2), LineVector([-3,7], [2,-3]), 'opgave 2')           
def opgave3():
    _opgave3([2,-3,0,2,-5], 'opgave 3')
def opgave4():
    v = np.array([-1,5,7,0,5])
    print('opgave 4')
    print('\t', v / np.linalg.norm(v))
def opgave5():
    _bereken_afstand_punt_vlak(np.array([7,0,-2]), PlaneVector([8,-5,3], [3,-2,1], [-5,3,-2]), 'opgave 5')
def opgave6():
    _bereken_afstand_punt_vlak(np.array([7,1,2]), PlaneConvertor().plane_vector_from_plane(Plane(2,-4,2,-2)), 'opgave 6')


def opgave1_extra():
    _opgave1([3,-2,0,5], [1,7,-2,2], 'extra opgave 1')
def opgave2_extra():
    _opgave2(Line(3,1), LineVector([0,0], [4,-3]), 'extra opgave 2')        
def opgave3_extra():
    _opgave3([4,0,7,-4,1], 'extra opgave 3')
def opgave4_extra():
    _bereken_afstand_punt_vlak(np.array([-3,9,-3]), PlaneVector([0,0,0], [4,2,4], [7,-1,-3]), 'extra opgave 4')
def opgave5_extra():
    _bereken_afstand_punt_vlak(np.array([-1,-4,-1]), PlaneConvertor().plane_vector_from_plane(Plane(-2,9,6,1/3.0)), 'extra opgave 6')

def hfst2():
    print('HOOFDSTUK 2\n')
    
    print('VOORBEELDEN berekening afstand punt/vlak')
    voorbeeld1()
    voorbeeld2()

    print('OPGAVEN')
    opgave1()
    opgave2()
    opgave3()
    opgave4()
    opgave5()
    opgave6()
    print('EXTRA OPGAVEN')

    opgave1_extra()
    opgave2_extra()
    opgave3_extra()
    opgave4_extra()
    opgave5_extra()

hfst2()