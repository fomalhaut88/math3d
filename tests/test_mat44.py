from . import Math3dTestCase

from math3d import pi, Vec3, Mat44


class TestMat44(Math3dTestCase):
    def test_copy(self):
        m = Mat44([
            [1.0, 2.0, -1.0, 5.0],
            [-3.0, 4.0, 2.0, 0.0],
            [7.0, 3.0, 3.0, -5.0],
            [0.0, -4.0, 1.0, -2.0]
        ])
        res = m.copy()
        self.assertMat44Equal(m, res)
        res[1, 2] = 10.0
        self.assertNotEqual(m[1, 2], res[1, 2])

    def test_zeros(self):
        m = Mat44()
        m.set_zeros()
        self.assertMat44Equal(m, Mat44([
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0]
        ]))

    def test_eye(self):
        m = Mat44()
        m.set_eye()
        self.assertMat44Equal(m, Mat44([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ]))

    def test_transpose(self):
        m = Mat44([
            [1.0, 2.0, -1.0, 5.0],
            [-3.0, 4.0, 2.0, 0.0],
            [7.0, 3.0, 3.0, -5.0],
            [0.0, -4.0, 1.0, -2.0]
        ])
        m.transpose()
        self.assertMat44Equal(m, Mat44([
            [1.0, -3.0, 7.0, 0.0],
            [2.0, 4.0, 3.0, -4.0],
            [-1.0, 2.0, 3.0, 1.0],
            [5.0, 0.0, -5.0, -2.0]
        ]))

    def test_from_3vec3(self):
        v1 = Vec3(1.0, 2.0, -1.0)
        v2 = Vec3(-3.0, 4.0, 2.0)
        v3 = Vec3(7.0, 3.0, 3.0)

        m = Mat44()
        m.set_from_3vec3(v1, v2, v3)

        self.assertMat44Equal(m, Mat44([
            [1.0, 2.0, -1.0, 0.0],
            [-3.0, 4.0, 2.0, 0.0],
            [7.0, 3.0, 3.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ]))

    def test_translation(self):
        v = Vec3(-3.0, 4.0, 2.0)
        m = Mat44()
        m.set_translation(v)
        self.assertMat44Equal(m, Mat44([
            [1.0, 0.0, 0.0, -3.0],
            [0.0, 1.0, 0.0, 4.0],
            [0.0, 0.0, 1.0, 2.0],
            [0.0, 0.0, 0.0, 1.0]
        ]))

    def test_rotation_x(self):
        m = Mat44()
        m.set_rotation_x(0.5 * pi)
        self.assertMat44Equal(m, Mat44([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, -1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ]))

    def test_rotation_y(self):
        m = Mat44()
        m.set_rotation_y(0.5 * pi)
        self.assertMat44Equal(m, Mat44([
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [-1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ]))

    def test_rotation_z(self):
        m = Mat44()
        m.set_rotation_z(0.5 * pi)
        self.assertMat44Equal(m, Mat44([
            [0.0, -1.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ]))

    def test_rotation(self):
        n = Vec3(1.0, 1.0, 1.0)
        n.normalize()
        m = Mat44()
        m.set_rotation(n, 2 * pi / 3)
        self.assertMat44Equal(m, Mat44([
            [0.0, 0.0, 1.0, 0.0],
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ]))

    def test_scale(self):
        m = Mat44()
        m.set_scale(1.5)
        self.assertMat44Equal(m, Mat44([
            [1.5, 0.0, 0.0, 0.0],
            [0.0, 1.5, 0.0, 0.0],
            [0.0, 0.0, 1.5, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ]))
        m.set_scale(Vec3(1.5, 2.0, 2.5))
        self.assertMat44Equal(m, Mat44([
            [1.5, 0.0, 0.0, 0.0],
            [0.0, 2.0, 0.0, 0.0],
            [0.0, 0.0, 2.5, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ]))

    def test_add(self):
        m1 = Mat44([
            [1.0, 2.0, -1.0, 5.0],
            [-3.0, 4.0, 2.0, 0.0],
            [7.0, 3.0, 3.0, -5.0],
            [0.0, -4.0, 1.0, -2.0]
        ])
        m2 = Mat44([
            [5.0, -1.0, 4.0, 8.0],
            [2.0, 2.0, 0.0, -3.0],
            [-7.0, -6.0, 1.0, 4.0],
            [1.0, 6.0, -2.0, -4.0]
        ])
        res = m1 + m2
        self.assertMat44Equal(res, Mat44([
            [6.0, 1.0, 3.0, 13.0],
            [-1.0, 6.0, 2.0, -3.0],
            [0.0, -3.0, 4.0, -1.0],
            [1.0, 2.0, -1.0, -6.0]
        ]))
        m1 += m2
        self.assertMat44Equal(m1, Mat44([
            [6.0, 1.0, 3.0, 13.0],
            [-1.0, 6.0, 2.0, -3.0],
            [0.0, -3.0, 4.0, -1.0],
            [1.0, 2.0, -1.0, -6.0]
        ]))

    def test_sub(self):
        m1 = Mat44([
            [1.0, 2.0, -1.0, 5.0],
            [-3.0, 4.0, 2.0, 0.0],
            [7.0, 3.0, 3.0, -5.0],
            [0.0, -4.0, 1.0, -2.0]
        ])
        m2 = Mat44([
            [5.0, -1.0, 4.0, 8.0],
            [2.0, 2.0, 0.0, -3.0],
            [-7.0, -6.0, 1.0, 4.0],
            [1.0, 6.0, -2.0, -4.0]
        ])
        res = m1 - m2
        self.assertMat44Equal(res, Mat44([
            [-4.0, 3.0, -5.0, -3.0],
            [-5.0, 2.0, 2.0, 3.0],
            [14.0, 9.0, 2.0, -9.0],
            [-1.0, -10.0, 3.0, 2.0]
        ]))
        m1 -= m2
        self.assertMat44Equal(m1, Mat44([
            [-4.0, 3.0, -5.0, -3.0],
            [-5.0, 2.0, 2.0, 3.0],
            [14.0, 9.0, 2.0, -9.0],
            [-1.0, -10.0, 3.0, 2.0]
        ]))

    def test_mul(self):
        m1 = Mat44([
            [1.0, 2.0, -1.0, 5.0],
            [-3.0, 4.0, 2.0, 0.0],
            [7.0, 3.0, 3.0, -5.0],
            [0.0, -4.0, 1.0, -2.0]
        ])
        m2 = Mat44([
            [5.0, -1.0, 4.0, 8.0],
            [2.0, 2.0, 0.0, -3.0],
            [-7.0, -6.0, 1.0, 4.0],
            [1.0, 6.0, -2.0, -4.0]
        ])
        res = m1 * m2
        self.assertMat44Equal(res, Mat44([
            [ 21.0,  39.0,  -7.0, -22.0],
            [-21.0,  -1.0, -10.0, -28.0],
            [ 15.0, -49.0,  41.0,  79.0],
            [-17.0, -26.0,   5.0,  24.0]
        ]))
        m1 *= m2
        self.assertMat44Equal(res, Mat44([
            [ 21.0,  39.0,  -7.0, -22.0],
            [-21.0,  -1.0, -10.0, -28.0],
            [ 15.0, -49.0,  41.0,  79.0],
            [-17.0, -26.0,   5.0,  24.0]
        ]))
        res = m2 * 2
        self.assertMat44Equal(res, Mat44([
            [ 10.0,  -2.0,   8.0,  16.0],
            [  4.0,   4.0,   0.0,  -6.0],
            [-14.0, -12.0,   2.0,   8.0],
            [  2.0,  12.0,  -4.0,  -8.0]
        ]))
        m2 *= 2
        self.assertMat44Equal(res, Mat44([
            [ 10.0,  -2.0,   8.0,  16.0],
            [  4.0,   4.0,   0.0,  -6.0],
            [-14.0, -12.0,   2.0,   8.0],
            [  2.0,  12.0,  -4.0,  -8.0]
        ]))

    def test_mul_pos(self):
        v = Vec3(-3.0, 4.0, 2.0)
        m = Mat44([
            [1.0, 2.0, -1.0, 5.0],
            [-3.0, 4.0, 2.0, 0.0],
            [7.0, 3.0, 3.0, -5.0],
            [0.0, -4.0, 1.0, -2.0]
        ])
        res = m.mul_pos(v)
        self.assertVec3Equal(res, Vec3(-0.5, -1.8125, 0.5))

    def test_mul_dir(self):
        v = Vec3(-0.6, 0.0, 0.8)
        m = Mat44([
            [1.0, 2.0, -1.0, 5.0],
            [-3.0, 4.0, 2.0, 0.0],
            [7.0, 3.0, 3.0, -5.0],
            [0.0, -4.0, 1.0, -2.0]
        ])
        res = m.mul_dir(v)
        self.assertVec3Equal(res, Vec3(-1.4, 3.4, -1.8))
