import ctypes

from . import _dll


_dll.vec3_norm2.restype = ctypes.c_float
_dll.vec3_norm.restype = ctypes.c_float
_dll.vec3_dot.restype = ctypes.c_float


class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._arr = (ctypes.c_float * 3)(x, y, z)

    def __repr__(self):
        return str(list(self._arr))

    def __getitem__(self, index):
        return self._arr[index]

    def __setitem__(self, index, value):
        self._arr[index] = value

    @property
    def pointer(self):
        return self._arr

    def copy(self):
        res = self.__class__()
        _dll.vec3_copy(res._arr, self._arr)
        return res

    def norm2(self):
        return _dll.vec3_norm2(self._arr)

    def norm(self):
        return _dll.vec3_norm(self._arr)

    def normalize(self):
        _dll.vec3_normalize(self._arr)

    def rotate(self, n, alpha):
        c_alpha = ctypes.c_float(alpha)
        _dll.vec3_rotate(self._arr, n._arr, c_alpha)

    def __iadd__(self, other):
        _dll.vec3_add(self._arr, other._arr)
        return self

    def __isub__(self, other):
        _dll.vec3_sub(self._arr, other._arr)
        return self

    def __imul__(self, z):
        c_z = ctypes.c_float(z)
        _dll.vec3_mul(self._arr, c_z)
        return self

    def __itruediv__(self, z):
        c_z = ctypes.c_float(1 / z)
        _dll.vec3_mul(self._arr, c_z)
        return self

    def __add__(self, other):
        res = self.copy()
        res += other
        return res

    def __sub__(self, other):
        res = self.copy()
        res -= other
        return res

    def __mul__(self, z):
        res = self.copy()
        res *= z
        return res

    def __truediv__(self, z):
        res = self.copy()
        res /= z
        return res

    __rmul__ = __mul__

    @classmethod
    def dot(cls, v1, v2):
        return _dll.vec3_dot(v1._arr, v2._arr)

    @classmethod
    def cross(cls, v1, v2):
        res = cls()
        _dll.vec3_cross(res._arr, v1._arr, v2._arr)
        return res
