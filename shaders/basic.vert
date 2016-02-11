#version 330

layout (location=0) in vec4 position;


uniform mat4 transMatrix;

void main()
{
    gl_Position = transMatrix * position;
}
