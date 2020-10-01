"""
Find the area of various geometric shapes
"""
from math import pi


def surface_area_cube(side_length: float) -> float:
    """
    Calculate the Surface Area of a Cube.

    >>> surface_area_cube(1)
    6
    >>> surface_area_cube(3)
    54
    >>> surface_area_cube(-1)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cube() only accepts non-negative values
    """
    if side_length < 0:
        raise ValueError("surface_area_cube() only accepts non-negative values")
    return 6 * side_length ** 2


def surface_area_sphere(radius: float) -> float:
    """
    Calculate the Surface Area of a Sphere.
    Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
    :return 4 * pi * r^2

    >>> surface_area_sphere(5)
    314.1592653589793
    >>> surface_area_sphere(1)
    12.566370614359172
    >>> surface_area_sphere(-1)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_sphere() only accepts non-negative values
    """
    if radius < 0:
        raise ValueError("surface_area_sphere() only accepts non-negative values")
    return 4 * pi * radius ** 2


def area_rectangle(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle

    >>> area_rectangle(10, 20)
    200
    >>> area_rectangle(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_rectangle() only accepts non-negative values
    >>> area_rectangle(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_rectangle() only accepts non-negative values
    >>> area_rectangle(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: area_rectangle() only accepts non-negative values
    """
    if length < 0 or width < 0:
        raise ValueError("area_rectangle() only accepts non-negative values")
    return length * width


def area_square(side_length: float) -> float:
    """
    Calculate the area of a square

    >>> area_square(10)
    100
    >>> area_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: area_square() only accepts non-negative values
    """
    if side_length < 0:
        raise ValueError("area_square() only accepts non-negative values")
    return side_length ** 2


def area_triangle(base: float, height: float) -> float:
    """
    Calculate the area of a triangle

    >>> area_triangle(10, 10)
    50.0
    >>> area_triangle(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_triangle() only accepts non-negative values
    >>> area_triangle(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_triangle() only accepts non-negative values
    >>> area_triangle(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: area_triangle() only accepts non-negative values
    """
    if base < 0 or height < 0:
        raise ValueError("area_triangle() only accepts non-negative values")
    return (base * height) / 2


def area_parallelogram(base: float, height: float) -> float:
    """
    Calculate the area of a parallelogram

    >>> area_parallelogram(10, 20)
    200
    >>> area_parallelogram(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_parallelogram() only accepts non-negative values
    >>> area_parallelogram(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_parallelogram() only accepts non-negative values
    >>> area_parallelogram(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: area_parallelogram() only accepts non-negative values
    """
    if base < 0 or height < 0:
        raise ValueError("area_parallelogram() only accepts non-negative values")
    return base * height


def area_trapezium(base1: float, base2: float, height: float) -> float:
    """
    Calculate the area of a trapezium

    >>> area_trapezium(10, 20, 30)
    450.0
    >>> area_trapezium(-1, -2, -3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(-1, 2, 3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(1, -2, 3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(1, 2, -3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(-1, -2, 3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(1, -2, -3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(-1, 2, -3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    """
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("area_trapezium() only accepts non-negative values")
    return 1 / 2 * (base1 + base2) * height


def area_circle(radius: float) -> float:
    """
    Calculate the area of a circle

    >>> area_circle(20)
    1256.6370614359173
    >>> area_circle(-1)
    Traceback (most recent call last):
        ...
    ValueError: area_circle() only accepts non-negative values
    """
    if radius < 0:
        raise ValueError("area_circle() only accepts non-negative values")
    return pi * radius ** 2


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
