import tmf
import OpenGLUtils as Utils
import glfw
from OpenGL.GL import *
import ShaderManager as ShaderM
import inputHandler
import logging.config


def initLogger():
    logging.config.fileConfig('log.conf')



def KillProgram():
    global window
    glfw.set_window_should_close(window, GL_TRUE)

def Culling():
    print "culling"

def main():
    global window
    initLogger()
    Utils.init()
    window = Utils.createWindow(inputHandler.keyboardListner)
    # triangle position and color

    vertexPos, vertexColor, triangle = tmf.load("testData.tmf")

    #define input
    inputHandler.addEvent(KillProgram, "Esc")
    inputHandler.addEvent(Culling, "c")
    print vertexPos
    VAO, VertexSize = Utils.createVAO(vertexPos, vertexColor, 4)
    shaderProgram = ShaderM.compileShaderFromFile("shaders/basic.vert", "shaders/basic.frag")

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
