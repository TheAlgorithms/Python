"""
Draws a line between two given points using the DDA algorithm.
"""
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 1.0, 0.0, 1.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)


# Function for digital differential analyzer algorithm
def draw_line_dda(x1: float, y1: float, x2: float, y2: float) -> None:
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_inc = dx / steps
    y_inc = dy / steps
    x = x1
    y = y1
    glBegin(GL_POINTS)
    for i in range(int(steps)):
        glVertex2f(round(x), round(y))
        x += x_inc
        y += y_inc
    glEnd()
    glFlush()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5)

    draw_line_dda(-55, 55, 50, -50)


def main() -> None:
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(700, 700)
    glutCreateWindow("My First OpenGL")
    init()
    glutDisplayFunc(draw)
    glutMainLoop()


main()
