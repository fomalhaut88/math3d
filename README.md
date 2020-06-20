# math3d

**math3d** is a Python library written in C that is designed and optimized to work with 3D geometry. Inside it contains two classes: **Vec3** (3-dimensional vector) and **Mat44** (matrix 4x4). There are many standard functions to manipulate with 3 dimensional vectors, including their transformations by linear operators (that can be represented as matrices 4x4). Alternatively, for the same purposes **numpy** can be used as well, but in some cases this approach can produce too many extra objects that are not deleted properly and in time in Python, so it could be impossible to use as uniform variables in Open GL shaders, for example. math3d solves this issue, so that is what it is developed for mainly.

## Supported functions

### Vec3 (3-dimensional operations)

1. Normalization
2. Invertion
3. Rotation around another vector on a fixed angle
4. Addition
5. Subtraction
6. Multiplication and division on a number
7. Scalar product (dot)
8. Vector product (cross)

### Mat44 (matrix 4x4)

1. Transpose
2. Addition
3. Subtraction
4. Multiplication on another matrix
5. Multiplication and division on a number
6. Translation of a vector
7. Rotation on a vector
8. Setting matrix as a translation operator
9. Setting matrix as a rotation operator (around X, Y or Z or an arbitrary axis)
10. Setting matrix as a scale operator
11. Setting matrix as a projection operator
12. Setting matrix as a perspective operator

## Installation

Make sure you have `pycdll` installed. If not:

    pip install git+https://github.com/fomalhaut88/pycdll.git

After that you can install `math3d`:

    pip install git+https://github.com/fomalhaut88/math3d.git

## Example

```python
    from math3d import Vec3, Mat44

    p = Vec3(1, -2, 3)
    n = Vec3(1, 1, 1).normalized
    mat = Mat44.eye()
    mat.set_rotation(n, angle=0.5)
    p2 = mat.mul_pos(p)
    print(p2)  # [2.3431765061443803, -2.227146425913363, 1.8839699197689825]
```
