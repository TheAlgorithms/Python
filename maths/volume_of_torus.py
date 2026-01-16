"""
Volume of a Torus
Reference: https://en.wikipedia.org/wiki/Torus
"""

from math import pi


def volume_of_torus(major_radius: float, minor_radius: float) -> float:
    """
    Calculate the volume of a torus.

    Formula:
        V = 2 * π² * R * r²

    :param major_radius: Distance from the center of the tube to the center of the torus (R)
    :param minor_radius: Radius of the tube (r)
    :return: Volume of the torus

    >>> volume_of_torus(3.0, 1.0)
    59.21762640653615
    >>> volume_of_torus(5.0, 2.0)
    394.7841760435743
    >>> volume_of_torus(0.0, 0.0)
    0.0
    """
    if major_radius < 0:
        raise ValueError("major_radius must be non-negative")
    if minor_radius < 0:
        raise ValueError("minor_radius must be non-negative")

    return 2 * (pi**2) * major_radius * (minor_radius**2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
