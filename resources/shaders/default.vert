#version 330

in vec3 in_vert;

uniform mat4 model;
uniform mat4 view;
uniform mat4 perspective;

void main() {
    gl_Position = perspective * view * model * vec4(in_vert, 1.0);
}
