

import sys
import tmf
import OpenGLUtils as Utils
import glfw
from OpenGL.GL import *

VERTEX_SHADER = """
#version 330

layout (location=0) in vec4 position;
layout (location=1) in vec4 color;

smooth out vec4 theColor;

void main()
{
    gl_Position = position;
    theColor = color;
}
"""

FRAGMENT_SHADER = """
#version 330

smooth in vec4 theColor;
out vec4 outputColor;

void main()
{
    outputColor = theColor;
}
"""




def main():
    Utils.init()
    window = Utils.createWindow()
    # triangle position and color

    vertexPos, vertexColor, triangle = tmf.load("testData.tmf")
    stuff = [0.0, 0.5, 0.0, 1.0,
		0.5, -0.366, 0.0, 1.0,
	         -0.5, -0.366, 0.0, 1.0]
    stuff2 = [1.0, 0.0, 0.0, 1.0,
		0.0, 1.0, 0.0, 1.0,
		0.0, 0.0, 1.0, 1.0,]

    print vertexPos
    VAO, VertexSize = Utils.createVAO(vertexPos, vertexColor)
    shaderProgram = Utils.compileShader(VERTEX_SHADER, FRAGMENT_SHADER)

    objectToRender = { "VAO" : VAO, "VertexCount" : VertexSize, "ShaderProgram" : shaderProgram}

    mainLoop(objectToRender,window)
    glfw.terminate()

def mainLoop(mainLoopObject, window):
    VAO = mainLoopObject["VAO"]
    VertexCount = mainLoopObject["VertexCount"]
    shaderProgram = mainLoopObject["ShaderProgram"]

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(shaderProgram)
        glBindVertexArray(VAO)

        # draw triangle
        glDrawArrays(GL_TRIANGLES, 0, VertexCount)

        glBindVertexArray(0)
        glUseProgram(0)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

if __name__ == '__main__':
    main()
