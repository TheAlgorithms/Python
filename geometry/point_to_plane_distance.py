from math import sqrt


def point_to_plane_distance(
    x: float, y: float, z: float, a: float, b: float, c: float, d: float
) -> float:
    """
    Return the distance between a point (x, y, z) and the plane
    ax + by + cz + d = 0 using the Hesse normal form.

    Reference:
    https://en.wikipedia.org/wiki/Hesse_normal_form

    >>> point_to_plane_distance(1, 2, 3, 1, 0, 0, -1)
    0.0
    >>> point_to_plane_distance(3, 2, 1, 1, 0, 0, -1)
    2.0
    >>> point_to_plane_distance(1, 2, 3, 0, 0, 0, 4)
    Traceback (most recent call last):
        ...
    ValueError: Normal vector cannot be zero.
    """
    if a == 0 and b == 0 and c == 0:
        raise ValueError("Normal vector cannot be zero.")

    return abs(a * x + b * y + c * z + d) / sqrt(a**2 + b**2 + c**2)
