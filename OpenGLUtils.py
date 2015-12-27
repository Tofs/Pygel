import ctypes

import sys
import numpy
from OpenGL.GL import *
from OpenGL.GL import shaders
import glfw
import os
import tmf

def compileShaderFromFile(vertexFilePath, fragmenFilePath):
    #load files into memory
    vertexFile = open(vertexFilePath)
    fragmentFile = open(fragmenFilePath)

    vertexString = vertexFile.read()
    fragmentString = fragmentFile.read()

    return compileShader(vertexString, fragmentString)

def compileShader(vertexShader, fragmentShader):
    # compile shaders and program
    v = vertexShader
    f = fragmentShader
    vs = shaders.compileShader(v, GL_VERTEX_SHADER)
    fs = shaders.compileShader(f, GL_FRAGMENT_SHADER)
    shaderProgram = shaders.compileProgram(vs, fs)

    return shaderProgram

def createWindow():
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        print("fail Window")
        return
    # Make the window's context current
    glfw.make_context_current(window)
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


def createVAO(vertexPos, vertexColor):
    vertexData = numpy.array(vertexPos+vertexColor, dtype=numpy.float32)
    # Append data arrays for glBufferData
    # create VAO
    vertexCount = len(vertexPos)/4
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    #GLuint elementbuffer;
    #glGenBuffers(1, &elementbuffer);
    #glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, elementbuffer);
    #glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.size() * sizeof(unsigned int), &indices[0], GL_STATIC_DRAW);




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

def createVAO(vertexPos, vertexColor):
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
