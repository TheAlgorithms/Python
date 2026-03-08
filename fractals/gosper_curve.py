"""
A Python implementation of the Gosper curve using the turtle module.
Reference: https://en.wikipedia.org/wiki/Gosper_curve
"""

import math
import turtle


def draw_gosper_curve(
    side_length: float, depth: int, direction: int = -1, angle: float = 60.0
) -> None:
    """
    Recursively draws a Gosper curve fractal.

    Args:
        side_length: The length of the current segment.
        depth: The recursive depth of the curve.
        direction: The direction of the drawing (1 or -1).
        angle: The angle of the turns in degrees.
    """
    if depth == 0:
        turtle.forward(side_length)
    else:
        side_length /= math.sqrt(7)
        depth -= 1
        if direction == -1:
            draw_gosper_curve(side_length, depth, -1, angle)
            turtle.left(angle)
            draw_gosper_curve(side_length, depth, 1, angle)
            turtle.left(2 * angle)
            draw_gosper_curve(side_length, depth, 1, angle)
            turtle.right(angle)
            draw_gosper_curve(side_length, depth, -1, angle)
            turtle.right(2 * angle)
            draw_gosper_curve(side_length, depth, -1, angle)
            draw_gosper_curve(side_length, depth, -1, angle)
            turtle.right(angle)
            draw_gosper_curve(side_length, depth, 1, angle)
            turtle.left(angle)
        else:
            turtle.right(angle)
            draw_gosper_curve(side_length, depth, -1, angle)
            turtle.left(angle)
            draw_gosper_curve(side_length, depth, 1, angle)
            draw_gosper_curve(side_length, depth, 1, angle)
            turtle.left(2 * angle)
            draw_gosper_curve(side_length, depth, 1, angle)
            turtle.left(angle)
            draw_gosper_curve(side_length, depth, -1, angle)
            turtle.right(2 * angle)
            draw_gosper_curve(side_length, depth, -1, angle)
            turtle.right(angle)
            draw_gosper_curve(side_length, depth, 1, angle)


if __name__ == "__main__":
    turtle.title("Gosper Curve")
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.speed(0)
    turtle.width(1)

    draw_gosper_curve(side_length=200.0, depth=4, direction=-1, angle=60.0)

    turtle.exitonclick()
