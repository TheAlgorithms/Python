"""
Find Surface Area of Various Shapes.

Wikipedia reference: https://en.wikipedia.org/wiki/Surface_area
"""
from math import pi, pow
from typing import Union

def surface_area_cube(side_length: Union[int, float]) -> float:
    """
    Calculate the Surface Area of a Cube.

    >>> surface_area_cube(1)
    6.0
    >>> surface_area_cube(3)
    54.0
    """
    return 6 * pow(side_length, 2)

def surface_area_sphere(radius: float) -> float:
    """
    Calculate the Surface Area of a Sphere.
    Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
    :return 4 * pi * r^2

    >>> vol_sphere(5)
    314.1592653589793
    >>> vol_sphere(1)
    12.566370614359172
    """
    return 4 * pi * pow(radius, 2)
