import ctypes

import sys
import numpy
from OpenGL.GL import *
import glfw
import os
import tmf

import logging

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


culling = False
def ToggleCulling(toState = None):
    global culling
    if toState is None:
        culling = not culling
    else:
        culling = toState

    if culling:
        logging.info("Culling is enabled")
        glEnable(GL_CULL_FACE)
    else:
        logging.info("Culling is disabled")
        glDisable(GL_CULL_FACE)
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


def createVAO(vertexPos, vertexColor, faces, size = 3, singleBuffer = False):

    numPos = numpy.array(vertexPos, dtype=numpy.float32)
    numColor = numpy.array(vertexColor, dtype=numpy.float32)
    numIndex = numpy.array(faces, dtype=numpy.uint32)

    # create VAO
    vertexCount = len(vertexPos)/4
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # create pos VBO
    pos = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pos)
    glBufferData(GL_ARRAY_BUFFER, numPos.nbytes, numPos, GL_STATIC_DRAW)

    index = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, index)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, numIndex.nbytes, numIndex, GL_STATIC_DRAW)

    glVertexAttribPointer(0, size, GL_FLOAT, GL_FALSE, 0, None)


    return VAO, pos, vertexCount, index
