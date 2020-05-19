"""
Find the area of various geometric shapes
"""

import math


def area_rectangle(base, height):
    """
    Calculate the area of a rectangle

    >> area_rectangle(10,20)
    200
    """
    return base * height


def area_square(side_length):
    """
    Calculate the area of a square

    >>> area_square(10)
    100
    """
    return side_length * side_length


def area_triangle(length, breadth):
    """
    Calculate the area of a triangle

    >>> area_triangle(10,10)
    50.0
    """
    return 1 / 2 * length * breadth


def area_parallelogram(base, height):
    """
    Calculate the area of a parallelogram

    >> area_parallelogram(10,20)
    200
    """
    return base * height


def area_trapezium(base1, base2, height):
    """
    Calculate the area of a trapezium

    >> area_trapezium(10,20,30)
    450
    """
    return 1 / 2 * (base1 + base2) * height


def area_circle(radius):
    """
    Calculate the area of a circle

    >> area_circle(20)
    1256.6370614359173
    """
    return math.pi * radius * radius


def main():
    print("Areas of various geometric shapes: \n")
    print(f"Rectangle: {area_rectangle(10, 20)=}")
    print(f"Square: {area_square(10)=}")
    print(f"Triangle: {area_triangle(10, 10)=}")
    print(f"Parallelogram: {area_parallelogram(10, 20)=}")
    print(f"Trapezium: {area_trapezium(10, 20, 30)=}")
    print(f"Circle: {area_circle(20)=}")


if __name__ == "__main__":
    main()
