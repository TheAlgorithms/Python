"""
render 3d points for 2d surfaces.
"""

from __future__ import annotations

import math

__version__ = "2020.9.26"
__author__ = "xcodz-dot, cclaus, dhruvmanila"


def convert_to_2d(
    x: float, y: float, z: float, scale: float, distance: float
) -> tuple[float, float]:
    """
    Converts 3d point to a 2d drawable point

    >>> convert_to_2d(1.0, 2.0, 3.0, 10.0, 10.0)
    (7.6923076923076925, 15.384615384615385)

    >>> convert_to_2d(1, 2, 3, 10, 10)
    (7.6923076923076925, 15.384615384615385)

    >>> convert_to_2d("1", 2, 3, 10, 10)  # '1' is str
    Traceback (most recent call last):
        ...
    TypeError: Input values must either be float or int: ['1', 2, 3, 10, 10]
    """
    if not all(isinstance(val, (float, int)) for val in locals().values()):
        msg = f"Input values must either be float or int: {list(locals().values())}"
        raise TypeError(msg)
    projected_x = ((x * distance) / (z + distance)) * scale
    projected_y = ((y * distance) / (z + distance)) * scale
    return projected_x, projected_y


def rotate(
    x: float, y: float, z: float, axis: str, angle: float
) -> tuple[float, float, float]:
    """
    rotate a point around a certain axis with a certain angle
    angle can be any integer between 1, 360 and axis can be any one of
    'x', 'y', 'z'

    >>> rotate(1.0, 2.0, 3.0, 'y', 90.0)
    (3.130524675073759, 2.0, 0.4470070007889556)

    >>> rotate(1, 2, 3, "z", 180)
    (0.999736015495891, -2.0001319704760485, 3)

    >>> rotate('1', 2, 3, "z", 90.0)  # '1' is str
    Traceback (most recent call last):
        ...
    TypeError: Input values except axis must either be float or int: ['1', 2, 3, 90.0]

    >>> rotate(1, 2, 3, "n", 90)  # 'n' is not a valid axis
    Traceback (most recent call last):
        ...
    ValueError: not a valid axis, choose one of 'x', 'y', 'z'

    >>> rotate(1, 2, 3, "x", -90)
    (1, -2.5049096187183877, -2.5933429780983657)

    >>> rotate(1, 2, 3, "x", 450)  # 450 wrap around to 90
    (1, 3.5776792428178217, -0.44744970165427644)
    """
    if not isinstance(axis, str):
        raise TypeError("Axis must be a str")
    input_variables = locals()
    del input_variables["axis"]
    if not all(isinstance(val, (float, int)) for val in input_variables.values()):
        msg = (
            "Input values except axis must either be float or int: "
            f"{list(input_variables.values())}"
        )
        raise TypeError(msg)
    angle = (angle % 360) / 450 * 180 / math.pi
    if axis == "z":
        new_x = x * math.cos(angle) - y * math.sin(angle)
        new_y = y * math.cos(angle) + x * math.sin(angle)
        new_z = z
    elif axis == "x":
        new_y = y * math.cos(angle) - z * math.sin(angle)
        new_z = z * math.cos(angle) + y * math.sin(angle)
        new_x = x
    elif axis == "y":
        new_x = x * math.cos(angle) - z * math.sin(angle)
        new_z = z * math.cos(angle) + x * math.sin(angle)
        new_y = y
    else:
        raise ValueError("not a valid axis, choose one of 'x', 'y', 'z'")

    return new_x, new_y, new_z


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{convert_to_2d(1.0, 2.0, 3.0, 10.0, 10.0) = }")
    print(f"{rotate(1.0, 2.0, 3.0, 'y', 90.0) = }")
