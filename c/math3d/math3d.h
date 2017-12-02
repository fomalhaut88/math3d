typedef double vec3[3];
typedef double mat44[16];


void print_vec3(const vec3 v);
void print_mat44(const mat44 m);

int double_equal(double x1, double x2);
int vec3_equal(const vec3 v1, const vec3 v2);
int mat_equal(const mat44 m1, const mat44 m2);


/* vec3 */

double vec3_dot(const vec3 v1, const vec3 v2);
void vec3_cross(vec3 res, const vec3 v1, const vec3 v2);

double vec3_norm2(const vec3 v);
double vec3_norm(const vec3 v);
void vec3_normalize(vec3 v);

void vec3_copy(vec3 v1, const vec3 v2);
void vec3_invert(vec3 v);
void vec3_add(vec3 v1, const vec3 v2);
void vec3_sub(vec3 v1, const vec3 v2);
void vec3_mul(vec3 v, double z);

void vec3_rotate(vec3 v, const vec3 n, double a);


/* mat */

void mat_copy(mat44 res, const mat44 m);
void mat_zeros(mat44 m);
void mat_eye(mat44 m);
void mat_from_3vec3(mat44 m, const vec3 v1, const vec3 v2, const vec3 v3);

void mat_translation(mat44 m, const vec3 v);
void mat_rotation_x(mat44 m, double a);
void mat_rotation_y(mat44 m, double a);
void mat_rotation_z(mat44 m, double a);
void mat_rotation(mat44 m, const vec3 n, double a);
void mat_scale(mat44 m, const vec3 v);
void mat_projection(mat44 m, double width, double height, double z_near, double z_far);
void mat_perspective(mat44 m, double wh, double tn, double z_near, double z_far);

void mat_add(mat44 m1, const mat44 m2);
void mat_sub(mat44 m1, const mat44 m2);
void mat_mul_scalar(mat44 m1, double z);
void mat_mul(mat44 res, const mat44 m1, const mat44 m2);
void mat_mul_pos(vec3 res, const vec3 p, const mat44 m);
void mat_mul_dir(vec3 res, const vec3 d, const mat44 m);
void mat_transpose(mat44 m);
