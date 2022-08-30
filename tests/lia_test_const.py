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
