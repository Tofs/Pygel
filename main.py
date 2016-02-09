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
    return
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    glFrontFace(GL_CCW) # GL_CW for clockwise and GL_CCW for counter clockwise



def createVAO(vertexPos, vertexColor, faces,size = 3, singleBuffer = False):
    if singleBuffer:
        return  singleVAO(vertexPos, vertexColor, faces, size)
    else:
        return multiVAO(vertexPos, vertexColor, faces, size)

def multiVAO(vertexPos, vertexColor, faces, size):

    return VAO, vertexCount, indexBuffer

def main():
    global window
    initLogger()
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



    window = Utils.createWindow(inputHandler.keyboardListner)
    # triangle position and color

    vertexPos, vertexColor, faces = tmf.load("testData.tmf")


    glEnable(GL_DEPTH_TEST)
    print vertexPos
    print faces

    #define input
    inputHandler.addEvent(KillProgram, "Esc")
    inputHandler.addEvent(Culling, "c")

    # VAO, VertexSize, indexs = createVAO(vertexPos, vertexColor, triangle, 4)
    size = 4

    numPos = numpy.array(vertexPos, dtype=numpy.float32)
    numColor = numpy.array(vertexColor, dtype=numpy.float32)
    numIndex = numpy.array(faces, dtype=numpy.uint32)

    # create VAO
    vertexCount = len(vertexPos)/4

    #gen buffers
    VAO = glGenVertexArrays(1)
    pos = glGenBuffers(1)
    index = glGenBuffers(1)

    glBindVertexArray(VAO)

    # create pos VBO
    glBindBuffer(GL_ARRAY_BUFFER, pos)
    glBufferData(GL_ARRAY_BUFFER, numPos.nbytes, numPos, GL_STATIC_DRAW)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, index)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, numIndex.nbytes, numIndex, GL_STATIC_DRAW)

    glBindBuffer(GL_ARRAY_BUFFER, pos)
    glVertexAttribPointer(0, size, GL_FLOAT, GL_FALSE, 0, None)




    shaderProgram = ShaderM.compileShaderFromFile("shaders/basic.vert", "shaders/basic.frag")

    mainLoopObject = { "Indexs" : index, "VAO" : VAO, "VertexCount" : vertexCount, "ShaderProgram" : shaderProgram}

    VAO = mainLoopObject["VAO"]
    i = mainLoopObject["Indexs"]
    VertexCount = mainLoopObject["VertexCount"]
    shaderProgram = mainLoopObject["ShaderProgram"]

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        glClearColor(0.5, 0.5, 0.5, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(shaderProgram)
        glEnableVertexAttribArray(0)

        glBindVertexArray(VAO)
        glBindBuffer(GL_ARRAY_BUFFER, pos)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, index)


        glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, ctypes.c_void_p(0))

        # Swap front and back buffers
        glfw.swap_buffers(window)


        # Poll for and process events
        glfw.poll_events()

        glBindVertexArray(0)
        glUseProgram(0)
    glfw.terminate()

if __name__ == '__main__':
    main()
