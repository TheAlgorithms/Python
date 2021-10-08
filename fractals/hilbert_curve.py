#!/usr/bin/python

"""Author Dev Raj | github:@dev-raj-1729

    Draws (Pseudo) Hilbert Curves of specified order and size

    What is a Hilbert Curve ?
    Mathematically speaking, The Hilbert Curve is a continuous fractal space filling
    curve of infinite length that is defined as the limit of
    Pseudo Hilbert Curves as the order tends to infinity.

    More info on Hilbert Curve
    -Wikipedia article - https://en.wikipedia.org/wiki/Hilbert_curve
    -YouTube video by 3Blue1Brown - https://youtu.be/3s7h2MHQtxc

    Usage:
    - $python hilbert_curve.py <order:int> <size:int> [<speed:int(0-3 is recommended)>]

    Credits: The recursive drawing algorithm is based on the algorithm from
        https://www.geeksforgeeks.org/python-hilbert-curve-using-turtle/
"""


import sys
import turtle


def hilbert(order: int, angle: int, step: float, pen: turtle.Turtle) -> None:
    """
    Draws Hilbert curve of specified order, angle passed must be 90 or -90
    (negative for a reflected curve), step is the length of a segment of the curve
    pen is the turtle to be used in drawing the curve. color etc of the curve can be
    changed by passing a pen of appropriate color.
    """
    if order <= 0:
        return

    pen.right(angle)
    hilbert(order - 1, -angle, step, pen)

    pen.forward(step)

    pen.left(angle)
    hilbert(order - 1, angle, step, pen)

    pen.forward(step)

    hilbert(order - 1, angle, step, pen)

    pen.left(angle)
    pen.forward(step)
    hilbert(order - 1, -angle, step, pen)

    pen.right(angle)


def draw_hilbert_curve(order: int, size: int, pen=None) -> None:
    """
    Sets up the environment for drawing a hilbert curve of specified
    order and size
    """
    if pen is None:
        pen = turtle.Turtle()

    step = size / (2 ** order)
    pen.penup()
    pen.goto(-size / 2 + step, size / 2 - step)
    pen.pendown()
    hilbert(order, 90, step, pen)
    turtle.update()


if __name__ == "__main__":
    if not (3 <= len(sys.argv) <= 4):
        raise ValueError(
            "The script is used in the following way\n"
            "$python hilbert_curve.py <order:int> <size:int> "
            "[<speed:int(0-3 is recommended)>]\n"
            "if speed is not given it will be instantly drawn"
        )
    turtle.tracer(0, 0)  # turn off screen updates for faster drawing

    order = int(sys.argv[1])
    size = int(sys.argv[2])
    pen = turtle.Turtle()
    pen.pencolor((0, 0, 0))
    pen.hideturtle()
    pen.speed(0)
    if len(sys.argv) == 4:
        turtle.tracer(
            4 ** (int(sys.argv[3]))
        )  # speed is to be controlled by changing screen update rate

    draw_hilbert_curve(order, size, pen)
    turtle.mainloop()
