import tmf
import OpenGLUtils as Utils
import glfw
from OpenGL.GL import *
import ShaderManager as ShaderM
import inputHandler
import logging.config
import os
import numpy

def initLogger():
    logging.config.fileConfig('log.conf')

def KillProgram():
    global window
    glfw.set_window_should_close(window, GL_TRUE)

def Culling():
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    glFrontFace(GL_CCW) # GL_CW for clockwise and GL_CCW for counter clockwise

def init():
    version_string = glfw.get_version_string();
    cwd = os.getcwd()
    print ("Starting GLFW")
    print (version_string)
    # Initialize the library
    if not glfw.init():
        print("fail glfw")
        return
    os.chdir(cwd)
    # make a window
    # glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)


def createVAO(vertexPos, vertexColor, faces,size = 3, singleBuffer = False):
    if singleBuffer:
        return  singleVAO(vertexPos, vertexColor, faces, size)
    else:
        return multiVAO(vertexPos, vertexColor, faces, size)
        
def multiVAO(vertexPos, vertexColor, faces, size):
    numPos = numpy.array(vertexPos, dtype=numpy.float32)
    numColor = numpy.array(vertexColor, dtype=numpy.float32)
    numIndex = numpy.array(faces, dtype=numpy.uint32)

    # create VAO
    vertexCount = len(vertexPos)/4

    #gen buffers
    VAO = glGenVertexArrays(1)
    pos = glGenBuffers(1)
    color = glGenBuffers(1)
    indexBuffer = glGenBuffers(1)

    glBindVertexArray(VAO)

    # create pos VBO
    glBindBuffer(GL_ARRAY_BUFFER, pos)
    glBufferData(GL_ARRAY_BUFFER, numPos.nbytes, numPos, GL_STATIC_DRAW)

    # create color VBO
    glBindBuffer(GL_ARRAY_BUFFER, color)
    glBufferData(GL_ARRAY_BUFFER, numColor.nbytes, numColor, GL_STATIC_DRAW)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexBuffer)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, numIndex.nbytes, numIndex, GL_STATIC_DRAW)

    # enable array and set up data
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)
    glBindBuffer(GL_ARRAY_BUFFER, pos)
    glVertexAttribPointer(0, size, GL_FLOAT, GL_FALSE, 0, None)
    # the last parameter is a pointer to tell the offset between
    # python donot have pointer, have to using ctypes
    glBindBuffer(GL_ARRAY_BUFFER, color)
    glVertexAttribPointer(1, size, GL_FLOAT, GL_FALSE, 0, None)


    return VAO, vertexCount, indexBuffer

def main():
    global window
    initLogger()
    init()
    window = Utils.createWindow(inputHandler.keyboardListner)
    # triangle position and color

    vertexPos, vertexColor, triangle = tmf.load("testData.tmf")

    #define input
    inputHandler.addEvent(KillProgram, "Esc")
    inputHandler.addEvent(Culling, "c")

    print vertexPos
    VAO, VertexSize, indexs = createVAO(vertexPos, vertexColor, triangle, 4)
    shaderProgram = ShaderM.compileShaderFromFile("shaders/basic.vert", "shaders/basic.frag")

    objectToRender = { "Indexs" : indexs, "VAO" : VAO, "VertexCount" : VertexSize, "ShaderProgram" : shaderProgram}

    mainLoop(objectToRender,window)
    glfw.terminate()

def mainLoop(mainLoopObject, window):
    VAO = mainLoopObject["VAO"]
    i = mainLoopObject["Indexs"]
    VertexCount = mainLoopObject["VertexCount"]
    shaderProgram = mainLoopObject["ShaderProgram"]

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        glClearColor(0.1, 0.1, 0.1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(shaderProgram)

        glBindVertexArray(VAO)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, i)
        # draw triangle using index
        glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, ctypes.c_void_p(0))

        glBindVertexArray(0)
        glUseProgram(0)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

if __name__ == '__main__':
    main()
