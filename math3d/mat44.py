import ctypes

from . import _dll, item_type, Vec3


class Mat44:
    def __init__(self, arr=None):
        self._data = (item_type * 16)()

        if arr is not None:
            for i in range(4):
                for j in range(4):
                    self[i, j] = arr[i][j]

    def __repr__(self):
        s = '['
        for i in range(4):
            for j in range(4):
                s += str(self[i, j]) + ' '
            s += '\n'
        s = s[:-1] + ']'
        return s

    def __getitem__(self, ij):
        return self._data[4 * ij[0] + ij[1]]

    def __setitem__(self, ij, value):
        self._data[4 * ij[0] + ij[1]] = value

    @property
    def data(self):
        return self._data

    def copy(self, target=None):
        if target is None:
            res = self.__class__()
            _dll.mat_copy(res._data, self._data)
            return res
        else:
            _dll.mat_copy(target._data, self._data)

    def transpose(self):
        _dll.mat_transpose(self._data)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            res = self.__class__()
            _dll.mat_mul(res._data, self._data, other._data)
            return res
        else:
            res = self.copy()
            c_z = item_type(other)
            _dll.mat_mul_scalar(res._data, c_z)
            return res

    __rmul__ = __mul__

    def __itruediv__(self, z):
        c_z = item_type(1.0 / z)
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
        _dll.mat_mul_pos(res.data, pos.data, self._data)
        return res

    def mul_dir(self, dir):
        res = Vec3()
        _dll.mat_mul_dir(res.data, dir.data, self._data)
        return res

    def set_zeros(self):
        _dll.mat_zeros(self._data)

    @classmethod
    def zeros(cls):
        m = cls()
        m.set_zeros()
        return m

    def set_eye(self):
        _dll.mat_eye(self._data)

    @classmethod
    def eye(cls):
        m = cls()
        m.set_eye()
        return m

    def set_from_3vec3(self, v1, v2, v3):
        _dll.mat_from_3vec3(self._data, v1.data, v2.data, v3.data)

    @classmethod
    def from_3vec3(cls, v1, v2, v3):
        m = cls()
        m.set_from_3vec3(v1, v2, v3)
        return m

    def set_translation(self, v):
        _dll.mat_translation(self._data, v.data)

    @classmethod
    def translation(cls, v):
        m = cls()
        m.set_translation(v)
        return m

    def set_rotation_x(self, angle):
        c_angle = item_type(angle)
        _dll.mat_rotation_x(self._data, c_angle)

    @classmethod
    def rotation_x(cls, angle):
        m = cls()
        m.set_rotation_x(angle)
        return m

    def set_rotation_y(self, angle):
        c_angle = item_type(angle)
        _dll.mat_rotation_y(self._data, c_angle)

    @classmethod
    def rotation_y(cls, angle):
        m = cls()
        m.set_rotation_y(angle)
        return m

    def set_rotation_z(self, angle):
        c_angle = item_type(angle)
        _dll.mat_rotation_z(self._data, c_angle)

    @classmethod
    def rotation_z(cls, angle):
        m = cls()
        m.set_rotation_z(angle)
        return m

    def set_rotation(self, n, angle):
        c_angle = item_type(angle)
        _dll.mat_rotation(self._data, n.data, c_angle)

    @classmethod
    def rotation(cls, n, angle):
        m = cls()
        m.set_rotation(n, angle)
        return m

    def set_scale(self, vec3_or_scalar):
        if not isinstance(vec3_or_scalar, Vec3):
            vec3_or_scalar = Vec3(vec3_or_scalar, vec3_or_scalar, vec3_or_scalar)
        _dll.mat_scale(self._data, vec3_or_scalar.data)

    @classmethod
    def scale(cls, vec3_or_scalar):
        m = cls()
        m.set_scale(vec3_or_scalar)
        return m

    def set_projection(self, width, height, z_near, z_far):
        c_width = item_type(width)
        c_height = item_type(height)
        c_z_near = item_type(z_near)
        c_z_far = item_type(z_far)

        _dll.mat_projection(self._data, c_width, c_height, c_z_near, c_z_far)

    @classmethod
    def projection(cls, width, height, z_near, z_far):
        m = cls()
        m.set_projection(width, height, z_near, z_far)
        return m

    def set_perspective(self, wh, tn, z_near, z_far):
        c_wh = item_type(wh)
        c_tn = item_type(tn)
        c_z_near = item_type(z_near)
        c_z_far = item_type(z_far)

        _dll.mat_perspective(self._data, c_wh, c_tn, c_z_near, c_z_far)

    @classmethod
    def perspective(cls, wh, tn, z_near, z_far):
        m = cls()
        m.set_perspective(wh, tn, z_near, z_far)
        return m
