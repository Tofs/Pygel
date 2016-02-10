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

def main():
    global window
    initLogger()
    Utils.init()
    window = Utils.createWindow(inputHandler.keyboardListner)
    # triangle position and color

    vertexPos, vertexColor, triangle = tmf.load("testData.tmf")
    glEnable(GL_DEPTH_TEST)
    #define input
    inputHandler.addEvent(KillProgram, "Esc")
    inputHandler.addEvent(ToggleCulling, "c")

    print vertexPos
    VAO,pos, VertexSize, indexs = Utils.createVAO(vertexPos, vertexColor, triangle, 4)
    shaderProgram = ShaderM.compileShaderFromFile("shaders/basic.vert", "shaders/basic.frag")

    objectToRender = { "Indexs" : indexs,"VertexBuffer" : pos, "VAO" :  VAO, "VertexCount" : VertexSize, "ShaderProgram" : shaderProgram}

    mainLoop(objectToRender,window)
    glfw.terminate()

def mainLoop(mainLoopObject, window):
    VAO = mainLoopObject["VAO"]
    i = mainLoopObject["Indexs"]
    VertexCount = mainLoopObject["VertexCount"]
    pos = mainLoopObject["VertexBuffer"]
    shaderProgram = mainLoopObject["ShaderProgram"]

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        glClearColor(0.1, 0.1, 0.5, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(shaderProgram)
        glEnableVertexAttribArray(0)

        glBindVertexArray(VAO)
        glBindBuffer(GL_ARRAY_BUFFER, pos)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, i)
        # draw triangle using index
        glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, ctypes.c_void_p(0))

        # Swap front and back buffers
        glfw.swap_buffers(window)

        glfw.poll_events()
        glBindVertexArray(0)
        glUseProgram(0)

        # Poll for and process events

if __name__ == '__main__':
    main()
