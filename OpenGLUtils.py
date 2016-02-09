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
