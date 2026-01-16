"""
Volume of a Torus
Board: https://en.wikipedia.org/wiki/Torus
"""
import math


def volume_of_torus(major_radius: float, minor_radius: float) -> float:
    """
    Calculate the volume of a torus.

    :param major_radius: Distance from the center of the tube to the center of the torus (R)
    :param minor_radius: Radius of the tube (r)
    :return: Volume of the torus

    >>> volume_of_torus(3, 1)
    59.21762640653615
    >>> volume_of_torus(5, 2)
    394.7841760435743
    """
    if major_radius < 0 or minor_radius < 0:
        raise ValueError("Radii must be non-negative")
    return 2 * (math.pi**2) * major_radius * (minor_radius**2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
