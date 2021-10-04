"""
This program aims at drawing a line using Bresenham's Line Drawing Algorithm
with OpenGL.
Reference: https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
"""
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
import math
from typing import Any

from OpenGL.GL.exceptional import glBegin, glEnd
from OpenGL.GLU import gluOrtho2D
from OpenGL.GLUT import (
    glutCreateWindow,
    glutDisplayFunc,
    glutInit,
    glutInitDisplayMode,
    glutInitWindowSize,
    glutMainLoop,
)
from OpenGL.raw.GL.VERSION.GL_1_0 import (
    GL_POINTS,
    GL_PROJECTION,
    glClearColor,
    glColor3f,
    glFlush,
    glMatrixMode,
    glVertex2i,
)
from OpenGL.raw.GLUT.constants import GLUT_RGB, GLUT_SINGLE

WIDTH, HEIGHT = 500, 500


"""
This function is used to plot points on the display.
x: x-coordinate to be plotted
y: y-coordinate to be plotted
>>> x = 10
>>> y = 15
"""
def plot_point(x: int, y: int) -> None:
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


def swap(a: Any, b: Any):
    """
    Swap any immutable variables using this function.
    """
    t = a
    a = b
    b = t
    return (a, b)


def bresenham_line(x1: int, y1: int, x2: int, y2: int):
    """
    This function draws a line using Bresenham's Line Drawing Algorithm.
    This is a very efficient algorithm as it only uses integer operations
    to compute the points of the line.
    """

    if x1 == x2:
        # This is the case where slope is infinity. Since the if condition
        # only checks if slope is greater than 1, we set slope to 2.
        m = 2
    else:
        m = (y2 - y1) / (x2 - x1)

    if abs(m) <= 1:
        if x1 > x2:
            x1, x2 = swap(x1, x2)
            y1, y2 = swap(y1, y2)

        if y1 <= y2:
            del_x = x2 - x1
            del_y = y2 - y1
            del_x2 = 2 * del_x
            del_y2 = 2 * del_y
            x = x1
            y = y1

            plot_point(x, y)
            pk = del_y2 - del_x
            while x < x2:
                x += 1
                if pk < 0:
                    pk += del_y2

                else:
                    y += 1
                    pk += del_y2 - del_x2

                plot_point(x, y)

        else:
            y1 = -y1
            y2 = -y2
            del_x = x2 - x1
            del_y = y2 - y1
            del_x2 = 2 * del_x
            del_y2 = 2 * del_y
            diff = del_y2 - del_x2
            x = x1
            y = y1

            pk = del_y2 - del_x
            while x < x2:

                x += 1
                if pk < 0:
                    pk += del_y2

                else:
                    y += 1
                    pk += diff

                plot_point(x, -y)
    else:
        if y1 > y2:
            x1, x2 = swap(x1, x2)
            y1, y2 = swap(y1, y2)

        if x1 <= x2:

            del_y = y2 - y1
            del_x = x2 - x1
            del_y2 = 2 * del_y
            del_x2 = 2 * (del_x)
            y = y1
            x = x1

            pk = del_x2 - del_y
            while y < y2:
                y += 1
                if pk < 0:
                    pk += del_x2

                else:
                    x += 1
                    pk += del_x2 - del_y2

                plot_point(x, y)

        else:

            x1 = -x1
            x2 = -x2
            del_y = y2 - y1
            del_x = x2 - x1
            del_y2 = 2 * del_y
            del_x2 = 2 * del_x
            y = y1
            x = x1

            plot_point(-x, y)
            pk = del_x2 - del_y
            while y < y2:

                y += 1
                if pk < 0:
                    pk += del_x2

                else:
                    x += 1
                    pk += del_x2 - del_y2

                plot_point(-x, y)


if __name__ == "__main__":

    def draw():
        """
        To test the working of Bresenham's Line Drawing Algorithm, we
        draw lines with angles ranging from [0, 360] from the x-axis.
        """
        glColor3f(1, 1, 1)
        for i in range(0, 360, 5):
            angle = i * 3.14 / 180
            bresenham_line(
                WIDTH // 2,
                HEIGHT // 2,
                int(WIDTH // 2 + 100 * math.cos(angle)),
                int(HEIGHT // 2 + 100 * math.sin(angle)),
            )
        glFlush()

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow("Bresenham's Line Drawing Algorithm")

    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, WIDTH, 0.0, HEIGHT)

    glutDisplayFunc(draw)
    glutMainLoop()
