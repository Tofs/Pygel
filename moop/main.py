import tmf
import OpenGLUtils as Utils
import glfw
from OpenGL.GL import *
import ShaderManager as ShaderM
import inputHandler
import logging.config

def main():
    global window
    initLogger()
    Utils.init()

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        print("fail Window")
        return
    # Make the window's context current
    glfw.make_context_current(window)

    vertexPos, vertexColor, triangle = tmf.load("testData.tmf")

    #define input
    inputHandler.addEvent(KillProgram, "Esc")
    inputHandler.addEvent(Culling, "c")

    print vertexPos
    VAO, VertexSize, indexs = Utils.createVAO(vertexPos, vertexColor, triangle, 4)
    shaderProgram = ShaderM.compileShaderFromFile("shaders/basic.vert", "shaders/basic.frag")

    objectToRender = { "Indexs" : indexs, "VAO" : VAO, "VertexCount" : VertexSize, "ShaderProgram" : shaderProgram}

    mainLoop(objectToRender,window)
    glfw.terminate()
