"""
Description
    The Gosper curve (also known as the flowsnake) is a fractal curve discovered
    by Bill Gosper. It is generated recursively by replacing each line segment
    with a specific pattern of smaller segments rotated by multiples of
    60 degrees.

    With each iteration, the curve becomes more complex and gradually fills
    a hexagonal region.

    (description adapted from https://en.wikipedia.org/wiki/Gosper_curve)

Requirements (pip):
    - turtle (standard library)
"""

import math
import turtle


def draw_gosper_curve(
    side_length: float, depth: int, direction: int = -1, angle: float = 60.0
) -> None:
    """
    Recursively draw a Gosper curve using turtle graphics.

    Args:
        side_length: Length of the current segment.
        depth: Recursive depth of the fractal.
        direction: Direction of the curve (1 or -1).
        angle: Turn angle in degrees.

    Note:
        Do not run this as a doctest; it uses turtle graphics.
    """
    if depth == 0:
        turtle.forward(side_length)
        return

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
    turtle.speed(0)

    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    draw_gosper_curve(200.0, 4)

    turtle.exitonclick()
