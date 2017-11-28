import ctypes

from . import _dll, Vec3


class Mat44:
    def __init__(self):
        self._data = (ctypes.c_float * 16)()

    def __repr__(self):
        s = ''
        for j in range(4):
            for i in range(4):
                s += ' ' + str(self._data[4 * j + i])
            s += '\n'
        return s

    @property
    def pointer(self):
        return self._data

    def copy(self):
        res = self.__class__()
        _dll.mat_copy(res._data, self._data)
        return res

    def transpose(self):
        _dll.mat_transpose(self._data)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            res = self.__class__()
            _dll.mat_mul(res._data, self._data, other._data)
            return res
        else:
            res = self.copy()
            c_z = ctypes.c_float(other)
            _dll.mat_mul_scalar(res._data, c_z)
            return res

    __rmul__ = __mul__

    def __itruediv__(self, z):
        c_z = ctypes.c_float(1.0 / z)
        _dll.mat_mul_scalar(self._data, c_z)
        return self

    def __truediv__(self, z):
        res = self.copy()
        res /= z
        return res

    def __iadd__(self, other):
        _dll.mat_add(self._data, other._data)
        return self

    def __add__(self, other):
        res = self.copy()
        res += other
        return res

    def __isub__(self, other):
        _dll.mat_sub(self._data, other._data)
        return self

    def __sub__(self, other):
        res = self.copy()
        res -= other
        return res

    def mul_pos(self, pos):
        res = Vec3()
        _dll.mat_mul_pos(res._arr, pos._arr, self._data)
        return res

    def mul_dir(self, dir):
        res = Vec3()
        _dll.mat_mul_dir(res._arr, dir._arr, self._data)
        return res

    @classmethod
    def zeros(cls):
        res = cls()
        _dll.mat_zeros(res._data)
        return res

    @classmethod
    def eye(cls):
        res = cls()
        _dll.mat_eye(res._data)
        return res

    @classmethod
    def from_3vec3(cls, v1, v2, v3):
        res = cls()
        _dll.mat_from_3vec3(res._data, v1._arr, v2._arr, v3._arr)
        return res

    @classmethod
    def translation(cls, v):
        res = cls()
        _dll.mat_translation(res._data, v._arr)
        return res

    @classmethod
    def rotate_x(cls, angle):
        c_angle = ctypes.c_float(angle)
        res = cls()
        _dll.mat_rotate_x(res._data, c_angle)
        return res

    @classmethod
    def rotate_y(cls, angle):
        c_angle = ctypes.c_float(angle)
        res = cls()
        _dll.mat_rotate_y(res._data, c_angle)
        return res

    @classmethod
    def rotate_z(cls, angle):
        c_angle = ctypes.c_float(angle)
        res = cls()
        _dll.mat_rotate_z(res._data, c_angle)
        return res

    @classmethod
    def rotate(cls, n, angle):
        c_angle = ctypes.c_float(angle)
        res = cls()
        _dll.mat_rotate(res._data, n._arr, c_angle)
        return res

    @classmethod
    def scale(cls, scl):
        c_scl = ctypes.c_float(scl)
        res = cls()
        _dll.mat_scale(res._data, c_scl)
        return res

    @classmethod
    def projection(cls, width, height, z_near, z_far):
        c_width = ctypes.c_float(width)
        c_height = ctypes.c_float(height)
        c_z_near = ctypes.c_float(z_near)
        c_z_far = ctypes.c_float(z_far)

        res = cls()
        _dll.mat_projection(res._data, c_width, c_height, c_z_near, c_z_far)
        return res

    @classmethod
    def perspective(cls, wh, tn, z_near, z_far):
        c_wh = ctypes.c_float(wh)
        c_tn = ctypes.c_float(tn)
        c_z_near = ctypes.c_float(z_near)
        c_z_far = ctypes.c_float(z_far)

        res = cls()
        _dll.mat_perspective(res._data, c_wh, c_tn, c_z_near, c_z_far)
        return res
