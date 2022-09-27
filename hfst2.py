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

def voorbeeld1():
    _bereken_afstand_punt_vlak(np.array([3,6,7]), VectorPlane([5,0,3], [-1,-1,1], [3,5,-6]), 'voorbeeld blz 20')
def voorbeeld2():
    _bereken_afstand_punt_vlak(np.array([-3,1,7]), VectorPlane([-1,-2,0], [-5,-8,3], [2,3,-1]), 'voorbeeld blz 22')

def opgave1():
    _opgave1([3,-1,2,0], [-2,2,4,7], 'opgave 1')
def opgave2():
    _opgave2(Line(2,7), VectorLine([-3,7], [2,-3]), 'opgave 2')           
def opgave3():
    _opgave3([2,-3,0,2,-5], 'opgave 3')
def opgave4():
    _opgave4([-1,5,7,0,5], 'opgave 4')
def opgave5():
    _bereken_afstand_punt_vlak(np.array([7,0,-2]), VectorPlane([8,-5,3], [3,-2,1], [-5,3,-2]), 'opgave 5')
def opgave6():
    _bereken_afstand_punt_vlak(np.array([7,1,2]), PlaneConvertor().vector_plane_from_plane(Plane(2,-4,2,-2)), 'opgave 6')


def opgave1_extra():
    _opgave1([3,-2,0,5], [1,7,-2,2], 'extra opgave 1')
def opgave2_extra():
    _opgave2(Line(3,1), VectorLine([0,0], [4,-3]), 'extra opgave 2')        
def opgave3_extra():
    _opgave3([4,0,7,-4,1], 'extra opgave 3')
def opgave4_extra():
    _bereken_afstand_punt_vlak(np.array([-3,9,-3]), VectorPlane([0,0,0], [4,2,4], [7,-1,-3]), 'extra opgave 4')
def opgave5_extra():
    _bereken_afstand_punt_vlak(np.array([-1,-4,-1]), PlaneConvertor().vector_plane_from_plane(Plane(-2,9,6,1/3.0)), 'extra opgave 6')

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
    print('*** EINDE ***')
    
if __name__ == '__main__':
    hfst2()

ang1 = angle(np.array([-1,9,6]), np.array([3,-1,2]))
ang2 = angle(np.array([-1,9,6]), np.array([0,2,-3]))
print(f'{ang1}  {ang2}')

print(np.cross([2,0,-1], [3,1,3]))
print(np.cross([2,1,0], [1.5,0,1]))
print(np.cross([-1,-1,1], [3,5,-6]))

V = VectorPlane([5,0,3],[-1,-1,1],[3,5,-6])
L = VectorLine([3,6,7],[1,-3,-2])
print(V.line_intersection(L))

print(np.cross([-5,-8,3], [2,3,-1]))
V = VectorPlane([-1,-2,0],[-5,-8,3],[2,3,-1])
L = VectorLine([-3,1,7],[-1,1,1])
print(V.line_intersection(L))


# for labda in [-1,0,1]:
#     for mu in [-1,0,1]:
#         x = -.5 + 2 * labda + 1.5*mu
#         y = labda
#         z = mu
#         print(f'labda {labda}, mu {mu}: x={x}, y = {y}, z = {z},   equation={-2*x+4*y+3*z}')
