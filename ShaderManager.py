
from OpenGL.GL import shaders
from OpenGL.GL import *
import ctypes

programs = {} # <vertexProgram , fragmentProgram>, id

def programExist(vertexShader, fragmentShader):
    if (vertexShader, fragmentShader) in programs:
        return True
    else:
        return False

def listPrograms():
    return programs

def compileShaderFromFile(vertexFilePath, fragmenFilePath):
    #load files into memory
    vertexFile = open(vertexFilePath)
    fragmentFile = open(fragmenFilePath)

    vertexString = vertexFile.read()
    fragmentString = fragmentFile.read()

    return compileShader(vertexString, fragmentString)

def compileShader(vertexShader, fragmentShader):
    # compile shaders and program
    if programExist(vertexShader, fragmentShader):
        return programs[(vertexShader, fragmentShader)]
    else:
        v = vertexShader
        f = fragmentShader

        # look if the program is allready loaded to avoid multiprogram in memmory
        vs = shaders.compileShader(v, GL_VERTEX_SHADER)
        fs = shaders.compileShader(f, GL_FRAGMENT_SHADER)
        shaderProgram = shaders.compileProgram(vs, fs)

        programs[(vertexShader, fragmentShader)] = shaderProgram
        return programs[(vertexShader, fragmentShader)]
