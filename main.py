import sys
import tmf
import OpenGLUtils as Utils
import glfw
from OpenGL.GL import *

def main():
    Utils.init()
    window = Utils.createWindow()
    # triangle position and color

    vertexPos, vertexColor, triangle = tmf.load("testData.tmf")

    print vertexPos
    VAO, VertexSize = Utils.createVAO(vertexPos, vertexColor)
    shaderProgram = Utils.compileShaderFromFile("shaders/basic.vert", "shaders/basic.frag")

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
