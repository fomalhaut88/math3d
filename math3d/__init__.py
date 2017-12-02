import os
import ctypes
from math import pi

from pycdll.compiler import Compiler


dll_dir = os.path.join(os.path.dirname(__file__), 'dll')
dll_path = Compiler.get_dllpath(dll_dir, 'math3d')

_dll = ctypes.CDLL(dll_path)

item_type = ctypes.c_double

from .vec3 import Vec3
from .mat44 import Mat44
