from time import time

from math3d import Vec3, Mat44


def benchmark_cross():
    import numpy as np

    count = 10000

    # math3d
    u = Vec3(2, 3, 5)
    v = Vec3(-1, 2, -3)

    b = time()
    for _ in range(count):
        Vec3.cross(u, v)
    e = time()
    print("Time math3d:", e - b)

    # numpy
    u = np.array([2, 3, 5])
    v = np.array([-1, 2, -3])

    b = time()
    for _ in range(count):
        np.cross(u, v)
    e = time()
    print("Time numpy:", e - b)


if __name__ == "__main__":
    # benchmark_cross()

    n = Vec3(1, -2, 3)
    n.normalize()
    m = Mat44.rotate(n, 0.75)
    m0 = m.copy()
    m.transpose()
    print(m * m0)
