import math


def pol_to_rec(mod: float, mag: float):
    ### https://en.wikipedia.org/wiki/Polar_coordinate_system
    """
    >>> pol_to_rec(5, 53)
    (3.01, 3.99)
    >>> pol_to_rec(10, 0)
    (10.0, 0.0)
    >>> pol_to_rec(0, 45)
    (0.0, 0.0)
    >>> pol_to_rec(5, 90)
    (0.0, 5.0)
    >>> pol_to_rec(5, 180)
    (-5.0, 0.0)
    >>> pol_to_rec(5, 270)
    (-0.0, -5.0)
    >>> pol_to_rec(5, 360)
    (5.0, -0.0)
    """

    rad = math.radians(mag)

    real = round((mod * math.cos(rad)), 2)
    img = round(mod * math.sin(rad), 2)

    rec = (real, img)

    return rec


if __name__ == "__main__":
    import doctest

    doctest.testmod()
