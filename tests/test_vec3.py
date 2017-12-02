from . import Math3dTestCase

from math3d import pi, Vec3


class TestVec3(Math3dTestCase):
    def test_dot(self):
        u = Vec3(2.0, 3.0, 5.0)
        v = Vec3(-1.0, 5.0, -2.0)
        res = Vec3.dot(u, v)
        self.assertEqual(res, 3.0)

    def test_cross(self):
        u = Vec3(2.0, 3.0, 5.0)
        v = Vec3(-1.0, 5.0, -2.0)
        res = Vec3.cross(u, v)
        self.assertVec3Equal(res, Vec3(-31.0, -1.0, 13.0))

    def test_norm2(self):
        u = Vec3(2.0, -3.0, 5.0)
        res = u.norm2()
        self.assertEqual(res, 38.0)

    def test_norm(self):
        u = Vec3(2.0, -3.0, 5.0)
        res = u.norm()
        self.assertEqual(res, 38.0**0.5)

    def test_normalize(self):
        u = Vec3(-3.0, 0.0, 4.0)
        u.normalize()
        self.assertVec3Equal(u, Vec3(-0.6, 0.0, 0.8))

    def test_copy(self):
        u = Vec3(2.0, -3.0, 5.0)
        v = u.copy()
        self.assertVec3Equal(u, v)
        v[1] = 1.0
        self.assertNotEqual(u[1], v[1])

    def test_invert(self):
        u = Vec3(2.0, -3.0, 5.0)
        u.invert()
        self.assertVec3Equal(u, Vec3(-2.0, 3.0, -5.0))

    def test_add(self):
        u = Vec3(2.0, 3.0, 5.0)
        v = Vec3(-1.0, 5.0, -2.0)
        res = u + v
        self.assertVec3Equal(res, Vec3(1.0, 8.0, 3.0))
        u += v
        self.assertVec3Equal(u, Vec3(1.0, 8.0, 3.0))

    def test_sub(self):
        u = Vec3(2.0, 3.0, 5.0)
        v = Vec3(-1.0, 5.0, -2.0)
        res = u - v
        self.assertVec3Equal(res, Vec3(3.0, -2.0, 7.0))
        u -= v
        self.assertVec3Equal(u, Vec3(3.0, -2.0, 7.0))

    def test_mul(self):
        u = Vec3(2.0, -3.0, 5.0)
        res = u * 2
        self.assertVec3Equal(res, Vec3(4.0, -6.0, 10.0))
        res = 2 * u
        self.assertVec3Equal(res, Vec3(4.0, -6.0, 10.0))
        u *= 2
        self.assertVec3Equal(u, Vec3(4.0, -6.0, 10.0))

    def test_rotate(self):
        u = Vec3(1.0, 0.0, 0.0)
        n = Vec3(1.0, 1.0, 1.0)
        n.normalize()
        u.rotate(n, 2 * pi / 3)
        self.assertVec3Equal(u, Vec3(0.0, 1.0, 0.0))
