from __future__ import division
from __future__ import print_function

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from math import floor


def key_callback(window, key, scancode, action, mode):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        print("closed window for pressing Escape key")
        glfw.set_window_should_close(window, True)
def reshape_callback(window, width, height):
    glViewport(0,0,width, height)


def setpixel(x,y,color):
    glColor3fv(color)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()


def DDALine(x1,y1,x2,y2, colour):
    if abs(x2-x1) >= abs(y2-y1):
        l=abs(x2-x1)
    else:
        l=abs(y2-y1)

    dx=(x2-x1)/l
    dy=(y2-y1)/l

    x=x1+0.5
    y=y1+0.5
    setpixel(floor(x), floor(y), [0,0,0])

    for i in range(1, l+1):
        x=x+dx
        y=y+dy
        setpixel(floor(x), floor(y), colour)


def main():
    if not glfw.init():
        raise Exception("glfw nt initialized")

    window=glfw.create_window(640,480, "DDA Line Drawing",None,None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window not created")

    w,h = glfw.get_framebuffer_size(window)
    print("width: {}, height:{}".format(w,h))

    glfw.set_window_pos(window, 400,200)

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    glfw.set_window_size_callback(window, reshape_callback)

    gluOrtho2D(-200.0, 200.0,-200.0,200.0)

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.0,0.76,0.56,1.0)

        DDALine(-150,-150,150,150, [1,0,1])#L2  pink correct
        DDALine(-150,-50,150,50,[1,1,0])#L1   yellow correct
        DDALine(-50,-150,50,150, [1,0,0]) #L3  red correct
        DDALine(-50,150,50,-150, [0,1,0])#L4   green corect
        DDALine(-150,150,150,-150,[0,0,1])#L5  blue correct
        DDALine(-150,50,150,-50,[0,1,1]) #L6   cyan/ sky blue correct
        

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ =="__main__":
    main()
