import unittest


class Math3dTestCase(unittest.TestCase):
    def assertVec3Equal(self, v1, v2):
        prompt = "{} != {}".format(v1, v2)
        self.assertFloatEqual(v1[0], v2[0], prompt)
        self.assertFloatEqual(v1[1], v2[1], prompt)
        self.assertFloatEqual(v1[2], v2[2], prompt)

    def assertMat44Equal(self, m1, m2):
        prompt = "\n{}\n!=\n{}\n".format(m1, m2)
        for j in range(4):
            for i in range(4):
                self.assertFloatEqual(m1[i, j], m2[i, j], prompt)

    def assertFloatEqual(self, x1, x2, prompt):
        self.assertTrue(abs(x1 - x2) < 1e-6, prompt)
