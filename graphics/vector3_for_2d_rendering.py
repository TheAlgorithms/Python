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
    if not all(isinstance(val, (float, int)) for val in locals().values()):
        raise ValueError(f"Input values must either be float or int: "+
                         f"{list(locals().values())}")
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
    if not 0 <= angle <= 360:
        raise ValueError("Angle is supposed to be in between 0, 360")
    input_variables = dict(locals())
    del input_variables["axis"]
    if not all(isinstance(val, (float, int)) for val in input_variables.values()):
        raise ValueError(f"Input values except axis must either be float or int: "+
                         f"{list(input_variables.values())}")
    if not isinstance(axis, str):
        raise ValueError(f"Axis must be a str")
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
