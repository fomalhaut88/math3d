typedef float vec3[3];
typedef float vec4[4];
typedef float mat44[16];


void print_vec3(const vec3 v);
void print_mat44(const mat44 m);

int float_equal(float x1, float x2);
int vec3_equal(const vec3 v1, const vec3 v2);
int mat_equal(const mat44 m1, const mat44 m2);


/* vec3 */

float vec3_dot(const vec3 v1, const vec3 v2);
void vec3_cross(vec3 res, const vec3 v1, const vec3 v2);

float vec3_norm2(const vec3 v);
float vec3_norm(const vec3 v);
void vec3_normalize(vec3 v);

void vec3_copy(vec3 v1, const vec3 v2);
void vec3_invert(vec3 v);
void vec3_add(vec3 v1, const vec3 v2);
void vec3_sub(vec3 v1, const vec3 v2);
void vec3_mul(vec3 v, float z);

void vec3_rotate(vec3 v, const vec3 n, float a);


/* mat */

void mat_copy(mat44 res, const mat44 m);
void mat_zeros(mat44 m);
void mat_eye(mat44 m);
void mat_from_3vec3(mat44 m, const vec3 v1, const vec3 v2, const vec3 v3);

void mat_translation(mat44 m, const vec3 v);
void mat_rotate_x(mat44 m, float a);
void mat_rotate_y(mat44 m, float a);
void mat_rotate_z(mat44 m, float a);
void mat_rotate(mat44 m, const vec3 n, float a);
void mat_scale(mat44 m, float scl);
void mat_projection(mat44 m, float width, float height, float z_near, float z_far);
void mat_perspective(mat44 m, float wh, float tn, float z_near, float z_far);

void mat_add(mat44 m1, const mat44 m2);
void mat_sub(mat44 m1, const mat44 m2);
void mat_mul_scalar(mat44 m1, float z);
void mat_mul(mat44 res, const mat44 m1, const mat44 m2);
void mat_mul_pos(vec3 res, const vec3 p, const mat44 m);
void mat_mul_dir(vec3 res, const vec3 d, const mat44 m);
void mat_transpose(mat44 m);
