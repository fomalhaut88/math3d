#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#include "math3d.h"


const float EPS = 1e-5;


void print_vec3(const vec3 v) {
    printf("[");
    for (int i = 0; i < 3; i++) {
        printf(" %f", v[i]);
    }
    printf("]\n");
}


void print_mat44(const mat44 m) {
    printf("[");
    for (int i = 0; i < 16; i++) {
        if ((i % 4 == 0) && (i > 0)) {
            printf("\n");
        }
        printf(" %f", m[i]);
    }
    printf("]\n");
}


int float_equal(float x1, float x2) {
    return fabs(x1 - x2) < EPS;
}


int vec3_equal(const vec3 v1, const vec3 v2) {
    for (int i = 0; i < 3; i++) {
        if (!float_equal(v1[i], v2[i])) {
            return 0;
        }
    }
    return 1;
}


int mat_equal(const mat44 m1, const mat44 m2) {
    for (int i = 0; i < 16; i++) {
        if (!float_equal(m1[i], m2[i])) {
            return 0;
        }
    }
    return 1;
}


/* vec3 */

float vec3_dot(const vec3 v1, const vec3 v2) {
    float r = 0.0f;
    for (int i = 0; i < 3; i++) {
        r += v1[i] * v2[i];
    }
    return r;
}


void vec3_cross(vec3 res, const vec3 v1, const vec3 v2) {
    res[0] = v1[1] * v2[2] - v1[2] * v2[1];
    res[1] = v1[2] * v2[0] - v1[0] * v2[2];
    res[2] = v1[0] * v2[1] - v1[1] * v2[0];
}


float vec3_norm2(const vec3 v) {
    return vec3_dot(v, v);
}


float vec3_norm(const vec3 v) {
    return sqrtf(vec3_norm2(v));
}


void vec3_normalize(vec3 v) {
    float n = vec3_norm(v);
    v[0] /= n;
    v[1] /= n;
    v[2] /= n;
}


void vec3_copy(vec3 v1, const vec3 v2) {
    memcpy(v1, v2, sizeof(float) * 3);
}


void vec3_invert(vec3 v) {
    vec3_mul(v, -1.0f);
}


void vec3_add(vec3 v1, const vec3 v2) {
    v1[0] += v2[0];
    v1[1] += v2[1];
    v1[2] += v2[2];
}


void vec3_sub(vec3 v1, const vec3 v2) {
    v1[0] -= v2[0];
    v1[1] -= v2[1];
    v1[2] -= v2[2];
}


void vec3_mul(vec3 v, float z) {
    v[0] *= z;
    v[1] *= z;
    v[2] *= z;
}


void vec3_rotate(vec3 v, const vec3 n, float a) {
    /*
    * v -> v' = v cos(a) + n dot(v, n) (1 - cos(a)) + cross(n, v) sin(a)
    */
    float d = vec3_dot(v, n);
    float ca = cosf(a);
    float sa = sinf(a);

    vec3 s2;
    vec3_copy(s2, n);
    vec3_mul(s2, d * (1.0f - ca));

    vec3 s3;
    vec3_cross(s3, n, v);
    vec3_mul(s3, sa);

    vec3_mul(v, ca);
    vec3_add(v, s2);
    vec3_add(v, s3);
}


/* mat */

void mat_copy(mat44 res, const mat44 m) {
    memcpy(res, m, sizeof(float) * 16);
}


void mat_zeros(mat44 m) {
    memset(m, 0, sizeof(float) * 16);
}


void mat_eye(mat44 m) {
    mat_zeros(m);
    m[0] = m[5] = m[10] = m[15] = 1.0f;
}


void mat_from_3vec3(mat44 m, const vec3 v1, const vec3 v2, const vec3 v3) {
    mat_zeros(m);
    vec3_copy(&m[0], v1);
    vec3_copy(&m[4], v2);
    vec3_copy(&m[8], v3);
    m[15] = 1.0f;
}


void mat_translation(mat44 m, const vec3 v) {
    mat_eye(m);

    m[3] = v[0];
    m[7] = v[1];
    m[11] = v[2];
}


void mat_rotate_x(mat44 m, float a) {
    mat_zeros(m);

    m[0] = m[15] = 1.0f;
    m[5] = m[10] = cosf(a);
    m[6] = -sinf(a);
    m[9] = sinf(a);
}


void mat_rotate_y(mat44 m, float a) {
    mat_zeros(m);

    m[5] = m[15] = 1.0f;
    m[0] = m[10] = cosf(a);
    m[2] = -sinf(a);
    m[8] = sinf(a);
}


void mat_rotate_z(mat44 m, float a) {
    mat_zeros(m);

    m[10] = m[15] = 1.0f;
    m[0] = m[5] = cosf(a);
    m[1] = -sinf(a);
    m[4] = sinf(a);
}


void mat_rotate(mat44 m, const vec3 n, float a) {
    float sa = sinf(a);
    float ca = cosf(a);
    float pca = 1.0f - ca;

    m[ 0] =         ca + n[0] * n[0] * pca;  m[ 1] = -n[2] * sa + n[1] * n[0] * pca;  m[ 2] =  n[1] * sa + n[2] * n[0] * pca;  m[ 3] = 0.0f;
    m[ 4] =  n[2] * sa + n[0] * n[1] * pca;  m[ 5] =         ca + n[1] * n[1] * pca;  m[ 6] = -n[0] * sa + n[2] * n[1] * pca;  m[ 7] = 0.0f;
    m[ 8] = -n[1] * sa + n[0] * n[2] * pca;  m[ 9] =  n[0] * sa + n[1] * n[2] * pca;  m[10] =         ca + n[2] * n[2] * pca;  m[11] = 0.0f;
    m[12] =                           0.0f;  m[13] =                           0.0f;  m[14] =                           0.0f;  m[15] = 1.0f;
}


void mat_scale(mat44 m, float scl) {
    mat_zeros(m);

    m[0] = m[5] = m[10] = scl;
    m[15] = 1.0f;
}


void mat_projection(mat44 m, float width, float height, float z_near, float z_far) {
    mat_zeros(m);

    m[0] = -2.0f / width;
    m[5] = -2.0f / height;
    m[10] = -2.0f / (z_far - z_near);
    m[11] = -(z_far + z_near) / (z_far - z_near);
    m[15] = 1.0f;
}


void mat_perspective(mat44 m, float wh, float tn, float z_near, float z_far) {
    mat_zeros(m);

    m[0] = 1.0f / (wh * tn);
    m[5] = 1.0f / tn;
    m[10] = -(z_far + z_near) / (z_far - z_near);
    m[11] = -2.0f * z_far * z_near / (z_far - z_near);
    m[14] = -1.0f;
}


void mat_add(mat44 m1, const mat44 m2) {
    for (int i = 0; i < 16; i++) {
        m1[i] += m2[i];
    }
}


void mat_sub(mat44 m1, const mat44 m2) {
    for (int i = 0; i < 16; i++) {
        m1[i] -= m2[i];
    }
}


void mat_mul_scalar(mat44 m1, float z) {
    for (int i = 0; i < 16; i++) {
        m1[i] *= z;
    }
}


void mat_mul(mat44 res, const mat44 m1, const mat44 m2) {
    for (int j = 0; j < 4; j++) {
        for (int i = 0; i < 4; i++) {
            int idx = 4 * j + i;
            res[idx] = 0.0f;
            for (int k = 0; k < 4; k++) {
                res[idx] += m1[4 * j + k] * m2[4 * k + i];
            }
        }
    }
}


void mat_mul_pos(vec3 res, const vec3 p, const mat44 m) {
    float w = vec3_dot(p, &m[12]) + m[15];

    res[0] = (vec3_dot(p, &m[0]) + m[3]) / w;
    res[1] = (vec3_dot(p, &m[4]) + m[7]) / w;
    res[2] = (vec3_dot(p, &m[8]) + m[11]) / w;
}


void mat_mul_dir(vec3 res, const vec3 p, const mat44 m) {
    res[0] = vec3_dot(p, &m[0]);
    res[1] = vec3_dot(p, &m[4]);
    res[2] = vec3_dot(p, &m[8]);
}


void mat_transpose(mat44 m) {
    for (int j = 0; j < 4; j++) {
        for (int i = 0; i < j; i++) {
            float t = m[4 * j + i];
            m[4 * j + i] = m[4 * i + j];
            m[4 * i + j] = t;
        }
    }
}
