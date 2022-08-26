import numpy as np
import math
import line
xyz = ['x', 'y', 'z']



def _opgave1(a, b, msg):
    a = np.array(a)
    b = np.array(b)
    print(msg)
    print('\t', np.add(a,b))
    print('\t', np.subtract(a,b))
    print('\t', np.inner(a,b))

def opgave1():
    _opgave1([3,-1,2,0], [-2,2,4,7], 'opgave 1')
def opgave1_extra():
    _opgave1([3,-2,0,5], [1,7,-2,2], 'extra opgave 1')

def _opgave2(l1: line.Line, lv1: line.LineVector, msg):
    angle = lv1.angle(line.LineConvertor().vector_from_line(l1))
    print(f'{msg}\t {round(angle, 1)}')    

def opgave2():
    _opgave2(line.Line(1,2), line.LineVector([-3,7], [2,-3]), 'opgave 2')           
def opgave2_extra():
    _opgave2(line.Line(3,1), line.LineVector([0,0], [4,-3]), 'extra opgave 2')        
    
def _opgave3(v, msg):
    v = np.array(v)
    print(msg)
    print('\t', round(np.linalg.norm(v), 2))
def opgave3():
    _opgave3([2,-3,0,2,-5], 'opgave 3')
def opgave3_extra():
    _opgave3([4,0,7,-4,1], 'extra opgave 3')
    
def opgave4():
    v = np.array([-1,5,7,0,5])
    print('opgave 4')
    print('\t', v / np.linalg.norm(v))

def opgave5():
    #P = np.array([7,0,-2])
    P = np.array([3,6,7])
    
    # p0 = np.array([8,-5,3])
    # p1 = np.array([3,-2,1])
    # p2 = np.array([-5,3,-2])    
    
    p0 = np.array([5,0,3])
    p1 = np.array([-1,-1,1])
    p2 = np.array([3,5,-6])    
    norm_vector = np.cross(p1,p2)
    c_value = np.inner(p0,norm_vector)
    

    # 8 * norm_vector[0] + -5 * norm_vector[1] + 3 * norm_vector[2]

    #equation: norm_vector[0].x + norm_vector[1].y + norm_vector[2].z = c_value

    print('opgave 5')
    print('\t', norm_vector, c_value)
    print(f'\tvergelijking vlak: {norm_vector[0]}.x + {norm_vector[1]}.y + {norm_vector[2]}.z = {c_value}')
    print(f'\tvergelijkingen loodlijn:')
    for i in range(3):
        print(f'\t\t{xyz[i]} = {P[i]} + {lamda}.{norm_vector[i]}')


opgave1()
opgave1_extra()
opgave2()
opgave2_extra()
opgave3()
opgave3_extra()
# opgave4()
#opgave5()

