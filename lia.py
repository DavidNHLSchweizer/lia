from enum import Enum, auto
import numpy as np
import math

PRECISION = 7

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
