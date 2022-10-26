from enum import Enum, auto
import numpy as np
import math

PRECISION = 5
EPSILON   = 1*math.pow(10,-PRECISION)

LAMBDA  = '\u03BB' # λ
MU      = '\u00B5' # μ
DEGREES = '\u00B0' # °
ROOT    = '\u221A' # √
class LiaException(Exception):
    pass

def angle(V1:np.array, V2:np.array, degrees = True)->float:
    if not (len(V1) == len(V2)):
        raise LiaException(f'Incompatible vectors {V1} and {V2} (angle)')
    angle_in_radians = math.acos((np.inner(V1, V2)/(np.linalg.norm(V1)*np.linalg.norm(V2))))
    return angle_in_radians if not degrees else angle_in_radians * 180 / math.pi

def normal_vector(V:np.array)->np.array:
    dim_1 = len(V)-1
    result = []
    if V[dim_1] == 0:
        for i in range(dim_1):
            result.append(0)
        result.append(1)
    else:
        sum = 0
        i = 0
        for i in range(dim_1):        
            result.append(1)
            sum+=V[i]*result[i]
        result.append(-sum/V[dim_1])
    return np.array(result)    

def vector_equivalent(V1: np.array, V2: np.array):
    if np.allclose(V1, V2):
        return True
    scale = None
    for i in range(len(V2)):
        if round(V2[i],PRECISION) == 0:
            if round(V1[i], PRECISION) != 0:
                return False
            else:
                continue
        elif round(V1[i],PRECISION) == 0:
            return False
        if not scale:
            scale = V1[i]/V2[i]
        elif abs(scale - V1[i]/V2[i]) > EPSILON:
            return False
    return True

class Axis(Enum):
    x=auto()
    y=auto()
    z=auto()

def BaseVector(axis:Axis, dim=3)->np.array:
    def _BaseVector2d(axis:Axis)->np.array:
        match axis:
            case Axis.x: return [1,0]
            case Axis.y: return [0,1]
            case Axis.z: raise LiaException('no z axis in 2 dimensions')
        return None
    def _BaseVector3d(axis:Axis)->np.array:
        match axis:
            case Axis.x: return [1,0,0]
            case Axis.y: return [0,1,0]
            case Axis.z: return [0,0,1]
        return None    
    match dim:
        case 2: return _BaseVector2d(axis)
        case 3: return _BaseVector3d(axis)
        case _: raise LiaException(f'unsupported dimension: {dim}')    
