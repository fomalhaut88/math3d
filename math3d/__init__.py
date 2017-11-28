import os
import ctypes


_dllpath = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'dll/math3d.so'
)
_dll = ctypes.CDLL(_dllpath)

from .vec3 import Vec3
from .mat44 import Mat44
