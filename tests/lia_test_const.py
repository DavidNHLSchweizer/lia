import random
import itertools
import math

_TEST_VALUES = [#-1000, 
                -100, -50, -42, -10, -5, -math.pi, -3, -2.5, -2, -1, -.75, -.66666, -.5, -.3, -.2, -.1, -.01, -.0001, 
                0, 
                .0001, .01, .1, .2, .3, .5, .66666, .75, 1, 2, 2.5, 3, math.pi, 5, 10, 42, 50, 100
                #, 1000                 
                ]

def _TEST_VECTORS_2D(n):
    return random.sample([[a,b] for (a,b) in itertools.combinations(_TEST_VALUES, 2)], n)
def _TEST_VECTORS_3D(n):
    return random.sample([[a,b,c] for (a,b,c) in itertools.combinations(_TEST_VALUES, 3)], n)

ABCD_VALUES = [
            (1,2,3,4),    
            (1,-2,3,0),
            (0,2,0,2),    
            (42,0,0,42),    
            (0,0,42,0),    
        ]
LABDA_MU_VALUES = [-42, -math.pi, -2, -1.5, -1, -0.5, -0.1, 0, 0.1, 0.5, 1, 1.5, 2, math.pi, 42]

TEST_PLANES = [ {'a':1, 'b':2, 'c':3, 'd':4, 'P':[0, 0, 1.3333333333333333], 'R1':[1, 0, -0.3333333333333333], 'R2':[0, 1, -0.6666666666666666], 'px':False, 'py':False, 'pz':False},
                {'a':0, 'b':2, 'c':3, 'd':4, 'P':[0, 0, 1.3333333333333333], 'R1':[1, 0, 0.0], 'R2':[0, 1, -0.6666666666666666], 'px':True, 'py':False, 'pz':False},
                {'a':1, 'b':0, 'c':3, 'd':4, 'P':[0, 0, 1.3333333333333333], 'R1':[1, 0, -0.3333333333333333], 'R2':[0, 1, 0.0],'px':False, 'py':True, 'pz':False},
                {'a':1, 'b':2, 'c':0, 'd':4, 'P':[0, 2.0, 0], 'R1':[1, -0.5, 0], 'R2':[0, 0, 1], 'px':False, 'py':False, 'pz':True},
                {'a':0, 'b':0, 'c':1, 'd':4, 'P':[0, 0, 4.0], 'R1':[1, 0, 0.0], 'R2':[0, 1, 0.0], 'px':True, 'py':True, 'pz':False},
                {'a':0, 'b':1, 'c':0, 'd':4, 'P':[0, 4.0, 0], 'R1':[1, 0.0, 0], 'R2':[0, 0, 1], 'px':True, 'py':False, 'pz':True},
                {'a':1, 'b':0, 'c':0, 'd':4, 'P':[4.0, 0, 0], 'R1':[0, 1, 0], 'R2':[0, 0, 1], 'px':False, 'py':True, 'pz':True},
                {'a':1, 'b':2, 'c':3, 'd':0, 'P':[0, 0, 0.0], 'R1':[1, 0, -0.3333333333333333], 'R2':[0, 1, -0.6666666666666666], 'px':False, 'py':False, 'pz':False},
                {'a':1,'b':0,'c':0, 'd':1, 'P':[1,2,3], 'R1':[0,1,1], 'R2':[0,1,2], 'px':False, 'py':True, 'pz':True}, 
                {'a':0,'b':0,'c':1, 'd':-1, 'P':[1,0,-1], 'R1':[1,0,0], 'R2':[0,1,0], 'px':True, 'py':True, 'pz':False}, 
                {'a':-2,'b':4,'c':-2, 'd':0, 'P':[1,2,3], 'R1':[1,2,3], 'R2':[3,4,5], 'px':False, 'py':False, 'pz':False}, 
                {'a':1,'b':-2,'c':1, 'd':0, 'P':[1,0,-1], 'R1':[1,1,1], 'R2':[0,1,2], 'px':False, 'py':False, 'pz':False}, 
              ]                    
