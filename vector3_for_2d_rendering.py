"""
Render 3d points on 2d surfaces.
"""

import math, copy

__version__ = "2020.9.26"
__author__ = "xcodz-dot"


def convert_to_2d(x: int, y: int, z: int, scale: int, distance: int) -> tuple:
    """
    Converts 3d point to a 2d drawable point

    >>> convert_to_2d(1, 2, 3, 10, 10)
    (7, 15)

    """
    if type(x) is not int:
        raise TypeError("x must be int")
    if type(y) is not int:
        raise TypeError("y must be int")
    if type(z) is not int:
        raise TypeError("z must be int")
    if type(scale) is not int:
        raise TypeError("scale must be int")
    if type(distance) is not int:
        raise TypeError("distance must be int")
    projectedY = int(((y * distance) / (z + distance)) * scale)
    projectedX = int(((x * distance) / (z + distance)) * scale)
    return projectedX, projectedY


def rotate(x: int, y: int, z: int, axis: str, angle: int):
    """
    rotate a point around a certain axis with a certain angle
    angler can be any integer between 1, 360

    >>> rotate(1, 2, 3, 'y', 90)
    (3.130524675073759, 2, 0.4470070007889556)
    """
    if angle > 360 or angle < 0:
        raise ValueError("Angle is supposed to be in between 0, 360")
    if type(x) is not int:
        raise TypeError("x must be int")
    if type(y) is not int:
        raise TypeError("y must be int")
    if type(z) is not int:
        raise TypeError("z must be int")
    angle = angle / 450 * 180 / math.pi
    if axis == 'z':
        newX = x * math.cos(angle) - y * math.sin(angle)
        newY = y * math.cos(angle) + x * math.sin(angle)
        newZ = z
    elif axis == 'x':
        newY = y * math.cos(angle) - z * math.sin(angle)
        newZ = z * math.cos(angle) + y * math.sin(angle)
        newX = x
    elif axis == 'y':
        newX = x * math.cos(angle) - z * math.sin(angle)
        newZ = z * math.cos(angle) + x * math.sin(angle)
        newY = y
    else:
        raise ValueError('not a valid axis')
    nx = newX
    ny = newY
    nz = newZ
    return nx, ny, nz
