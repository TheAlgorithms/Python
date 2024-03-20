"""Authors Bastien Capiaux & Mehdi Oudghiri

The Vicsek fractal algorithm is a recursive algorithm that creates a
pattern known as the Vicsek fractal or the Vicsek square.
It is based on the concept of self-similarity, where the pattern at each
level of recursion resembles the overall pattern.
The algorithm involves dividing a square into 9 equal smaller squares,
removing the center square, and then repeating this process on the remaining 8 squares.
This results in a pattern that exhibits self-similarity and has a
square-shaped outline with smaller squares within it.

Source: https://en.wikipedia.org/wiki/Vicsek_fractal
"""

import turtle


def draw_cross(x: float, y: float, length: float):
    """
    Draw a cross at the specified position and with the specified length.
    """
    turtle.up()
    turtle.goto(x - length / 2, y - length / 6)
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length / 3)
        turtle.right(90)
        turtle.fd(length / 3)
        turtle.left(90)
        turtle.fd(length / 3)
        turtle.left(90)
    turtle.end_fill()


def draw_fractal_recursive(x: float, y: float, length: float, depth: float):
    """
    Recursively draw the Vicsek fractal at the specified position, with the
    specified length and depth.
    """
    if depth == 0:
        draw_cross(x, y, length)
        return

    draw_fractal_recursive(x, y, length / 3, depth - 1)
    draw_fractal_recursive(x + length / 3, y, length / 3, depth - 1)
    draw_fractal_recursive(x - length / 3, y, length / 3, depth - 1)
    draw_fractal_recursive(x, y + length / 3, length / 3, depth - 1)
    draw_fractal_recursive(x, y - length / 3, length / 3, depth - 1)


def set_color(rgb: str):
    turtle.color(rgb)


def draw_vicsek_fractal(x: float, y: float, length: float, depth: float, color="blue"):
    """
    Draw the Vicsek fractal at the specified position, with the specified
    length and depth.
    """
    turtle.speed(0)
    turtle.hideturtle()
    set_color(color)
    draw_fractal_recursive(x, y, length, depth)
    turtle.Screen().update()


def main():
    draw_vicsek_fractal(0, 0, 800, 4)

    turtle.done()


if __name__ == "__main__":
    main()
