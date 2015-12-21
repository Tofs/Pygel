
# --------------------------------------------------------------------------------
# Copyright (c) 2013 Mack Stone. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# --------------------------------------------------------------------------------

"""
Modern OpenGL with python.
render a color triangle with pyopengl using glfw.

@author: Mack Stone
"""


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
