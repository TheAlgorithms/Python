from math import pi

def arc_length(angle: float, radius: float) -> float:
    """
    Calculate the arc length of a circle.
    The arc length is the distance along the curved line making up the arc.
    Formula: arc_length = 2 * pi * radius * (angle / 360)
    Wikipedia: https://en.wikipedia.org/wiki/Arc_length
    Args:
        angle: The angle in degrees
        radius: The radius of the circle
    Returns:
        The arc length as a float
    >>> arc_length(45, 5)
    3.9269908169872414
    >>> arc_length(120, 15)
    31.415926535897928
    >>> arc_length(90, 10)
    15.707963267948966
    >>> arc_length(0, 10)
    0.0
    >>> arc_length(360, 5)
    31.41592653589793
    >>> arc_length(180, 10)
    31.41592653589793
    >>> arc_length(45.5, 10.5)
    8.33831050140291
    >>> arc_length(-90, 10)
    Traceback (most recent call last):
        ...
    ValueError: angle and radius must be positive
    >>> arc_length(90, -10)
    Traceback (most recent call last):
        ...
    ValueError: angle and radius must be positive
    """
    if angle < 0 or radius < 0:
        raise ValueError("angle and radius must be positive")
    return 2 * pi * radius * (angle / 360)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
