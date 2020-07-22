"""
Find the area of various geometric shapes
"""
from math import pi
from typing import Union


def surface_area_cube(side_length: Union[int, float]) -> float:
    """
    Calculate the Surface Area of a Cube.

    >>> surface_area_cube(1)
    6
    >>> surface_area_cube(3)
    54
    """
    return 6 * pow(side_length, 2)


def surface_area_sphere(radius: float) -> float:
    """
    Calculate the Surface Area of a Sphere.
    Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
    :return 4 * pi * r^2

    >>> surface_area_sphere(5)
    314.1592653589793
    >>> surface_area_sphere(1)
    12.566370614359172
    """
    return 4 * pi * pow(radius, 2)


def area_rectangle(length, width):
    """
    Calculate the area of a rectangle

    >>> area_rectangle(10,20)
    200
    """
    return length * width


def area_square(side_length):
    """
    Calculate the area of a square

    >>> area_square(10)
    100
    """
    return pow(side_length, 2)


def area_triangle(base, height):
    """
    Calculate the area of a triangle

    >>> area_triangle(10,10)
    50.0
    """
    return (base * height) / 2


def area_parallelogram(base, height):
    """
    Calculate the area of a parallelogram

    >>> area_parallelogram(10,20)
    200
    """
    return base * height


def area_trapezium(base1, base2, height):
    """
    Calculate the area of a trapezium

    >>> area_trapezium(10,20,30)
    450.0
    """
    return 1 / 2 * (base1 + base2) * height


def area_circle(radius):
    """
    Calculate the area of a circle

    >>> area_circle(20)
    1256.6370614359173
    """
    return pi * pow(radius, 2)


def main():
    print("Areas of various geometric shapes: \n")
    print(f"Rectangle: {area_rectangle(10, 20)}")
    print(f"Square: {area_square(10)}")
    print(f"Triangle: {area_triangle(10, 10)}")
    print(f"Parallelogram: {area_parallelogram(10, 20)}")
    print(f"Trapezium: {area_trapezium(10, 20, 30)}")
    print(f"Circle: {area_circle(20)}")
    print("\nSurface Areas of various geometric shapes: \n")
    print(f"Cube: {surface_area_cube(20)}")
    print(f"Sphere: {surface_area_sphere(20)}")


if __name__ == "__main__":

    import doctest

    doctest.testmod(verbose=True)  # verbose so we can see methods missing tests

    main()
