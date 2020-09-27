"""
render 3d points for 2d surfaces.
"""

import math

__version__ = "2020.9.26"
__author__ = "xcodz-dot"


def convert_to_2d(x: float, y: float, z: float, scale: float,
                  distance: float) -> (float, float):
    """
    Converts 3d point to a 2d drawable point

    >>> convert_to_2d(1.0, 2.0, 3.0, 10.0, 10.0)
    (7.6923076923076925, 15.384615384615385)
    """
    if not isinstance(x, (float, int)):
        raise ValueError("x must be float or int")
    if not isinstance(y, (float, int)):
        raise ValueError("y must be float or int")
    if not isinstance(z, (float, int)):
        raise ValueError("z must be float or int")
    if not isinstance(scale, (float, int)):
        raise ValueError("scale must be float or int")
    if not isinstance(distance, (float, int)):
        raise ValueError("distance must be float")
    projected_x = ((x * distance) / (z + distance)) * scale
    projected_y = ((y * distance) / (z + distance)) * scale
    return projected_x, projected_y


def rotate(x: float, y: float, z: float, axis: str,
           angle: float) -> (float, float, float):
    """
    rotate a point around a certain axis with a certain angle
    angle can be any integer between 1, 360 and axis can be any one of
    'x', 'y', 'z'

    >>> rotate(1.0, 2.0, 3.0, 'y', 90.0)
    (3.130524675073759, 2.0, 0.4470070007889556)
    """
    if not isinstance(angle, (int, float)):
        raise ValueError("Angel must be int or float")
    if angle > 360 or angle < 0:
        raise ValueError("Angle is supposed to be in between 0, 360")
    if not isinstance(x, (int, float)):
        raise ValueError("x must be int or float")
    if not isinstance(y, (int, float)):
        raise ValueError("y must be int or float")
    if not isinstance(z, (int, float)):
        raise ValueError("z must be int or float")
    angle = angle / 450 * 180 / math.pi
    if axis == 'z':
        new_x = x * math.cos(angle) - y * math.sin(angle)
        new_y = y * math.cos(angle) + x * math.sin(angle)
        new_z = z
    elif axis == 'x':
        new_y = y * math.cos(angle) - z * math.sin(angle)
        new_z = z * math.cos(angle) + y * math.sin(angle)
        new_x = x
    elif axis == 'y':
        new_x = x * math.cos(angle) - z * math.sin(angle)
        new_z = z * math.cos(angle) + x * math.sin(angle)
        new_y = y
    else:
        raise ValueError("not a valid axis, choose one of 'x', 'y', 'z'")

    return new_x, new_y, new_z
