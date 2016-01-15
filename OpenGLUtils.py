import ctypes

import sys
import numpy
from OpenGL.GL import *
import glfw
import os
import tmf


def createWindow(keyboardCallBackFunction = None):
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        print("fail Window")
        return
    # Make the window's context current
    glfw.make_context_current(window)

    if not keyboardCallBackFunction == None:
        # keyboard callback function
        glfw.set_key_callback(window, keyboardCallBackFunction)

    return window

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


def createVAO(vertexPos, vertexColor, size = 3, singleBuffer = False):
    if singleBuffer:
        return  singleVAO(vertexPos, vertexColor, size)
    else:
        return multiVAO(vertexPos, vertexColor, size)

def singleVAO(vertexPos, vertexColor, size):
    vertexData = numpy.array(vertexPos+vertexColor, dtype=numpy.float32)
    # Append data arrays for glBufferData
    # create VAO
    vertexCount = len(vertexPos)/4
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # create VBO
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertexData.nbytes, vertexData, GL_STATIC_DRAW)

    # enable array and set up data
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 0, None)
    # the last parameter is a pointer to tell the offset between
    # python donot have pointer, have to using ctypes
    glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(vertexCount * 16))

    return VAO, vertexCount

def multiVAO(vertexPos, vertexColor, size):
    numPos = numpy.array(vertexPos, dtype=numpy.float32)
    numColor = numpy.array(vertexColor, dtype=numpy.float32)

    # create VAO
    vertexCount = len(vertexPos)/4
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # create pos VBO
    pos = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pos)
    glBufferData(GL_ARRAY_BUFFER, numPos.nbytes, numPos, GL_STATIC_DRAW)

    # create color VBO
    color = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, color)
    glBufferData(GL_ARRAY_BUFFER, numColor.nbytes, numColor, GL_STATIC_DRAW)

    # enable array and set up data
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)
    glBindBuffer(GL_ARRAY_BUFFER, pos)
    glVertexAttribPointer(0, size, GL_FLOAT, GL_FALSE, 0, None)
    # the last parameter is a pointer to tell the offset between
    # python donot have pointer, have to using ctypes
    glBindBuffer(GL_ARRAY_BUFFER, color)
    glVertexAttribPointer(1, size, GL_FLOAT, GL_FALSE, 0, None)


    return VAO, vertexCount
