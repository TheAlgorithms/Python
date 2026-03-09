from math import sqrt


def point_to_plane_distance(
    point_x: float,
    point_y: float,
    point_z: float,
    normal_x: float,
    normal_y: float,
    normal_z: float,
    plane_constant: float,
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
    if normal_x == 0 and normal_y == 0 and normal_z == 0:
        raise ValueError("Normal vector cannot be zero.")

    return abs(
        normal_x * point_x + normal_y * point_y + normal_z * point_z + plane_constant
    ) / sqrt(normal_x**2 + normal_y**2 + normal_z**2)
