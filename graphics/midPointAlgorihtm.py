"""
Draw a line between two points using Mid point algorithm (Bresenham's Agorithm)
"""
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)


# Function for mid point algorithm
def mid_point_algo(x1, y1, x2, y2):
    glBegin(GL_POINTS)
    dx = x2 - x1
    dy = y2 - y1
    y = y1

    p = 2 * dy - dx
    x = x1
    while x < x2:
        x = x + 1
        if p <= 0:
            y = y + 1
            glVertex2f(x, y)
            p = p + 2 * dy - 2 * dx
        else:
            p = p + 2 * dy
            glVertex2f(x, y)
    glEnd()
    glFlush()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5)

    mid_point_algo(-40, 0, 40, 0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(700, 700)
    glutCreateWindow("My First OpenGL")
    init()
    glutDisplayFunc(draw)
    glutMainLoop()


main()
