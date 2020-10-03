""" Coordinate conversion """

from math import atan, cos, sin


def polar_to_cartesian(radius: float, angle: float) -> (float, float):
    """
    This function returns (x, y) i.e. cartesian co ordinates
    given polar coordinates (r, theta)
    Reference:
    https://en.wikipedia.org/wiki/Polar_coordinate_system
    https://en.wikipedia.org/wiki/Cartesian_coordinate_system

    >>> polar_to_cartesian(0, 0)
    (0.0, 0.0)
    >>> polar_to_cartesian(1, 0.7853981633974483)
    (0.7071067811865476, 0.7071067811865475)
    """
    x_coordinate = radius * cos(angle)
    y_coordinate = radius * sin(angle)
    return (x_coordinate, y_coordinate)


def cartesian_to_polar(x_coordinate: float, y_coordinate: float) -> (float, float):
    """
    This function returns (r, theta) i.e. cartesian co ordinates
    given polar coordinates (x, y)
    Reference:
    https://en.wikipedia.org/wiki/Polar_coordinate_system
    https://en.wikipedia.org/wiki/Cartesian_coordinate_system

    >>> cartesian_to_polar(0, 0)
    (0.0, inf)
    >>> cartesian_to_polar(0.7071067811865476, 0.7071067811865475)
    (1.0, 0.7853981633974483)

    """
    radius = (
        (x_coordinate ** 2) + (y_coordinate ** 2)
    ) ** 0.5  # root of x squared and y squared
    theta = atan(y_coordinate / x_coordinate) if (x_coordinate != 0) else float("inf")
    return (radius, theta)


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
