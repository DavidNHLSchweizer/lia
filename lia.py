import numpy as np
import math

PRECISION = 7

LAMBDA  = '\u03BB' # λ
MU      = '\u00B5' # μ

class LiaException(Exception):
    pass

def angle(V1:np.array, V2:np.array, degrees = True)->float:
    if not (len(V1) == len(V2)):
        raise LiaException(f'Incompatible vectors {V1} and {V2} (angle)')
    angle_in_radians = math.acos((np.inner(V1, V2)/(np.linalg.norm(V1)*np.linalg.norm(V2))))
    return angle_in_radians if not degrees else angle_in_radians * 180 / math.pi

