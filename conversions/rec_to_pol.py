import doctest
import math


def rec_to_pol(real: float, img: float) -> tuple:
    """
    https://en.wikipedia.org/wiki/Polar_coordinate_system

    >>> rec_to_pol(5,-5)
    (7.07, -45.0)
    >>> rec_to_pol(-1,1)
    (1.41, 135.0)
    >>> rec_to_pol(-1,-1)
    (1.41, -135.0)
    >>> rec_to_pol(1e-10,1e-10)
    (0.0, 45.0)
    >>> rec_to_pol(-1e-10,1e-10)
    (0.0, 135.0)
    >>> rec_to_pol(9.75,5.93)
    (11.41, 31.31)
    >>> rec_to_pol(10000,99999)
    (100497.76, 84.29)

    """

    mod = round(math.sqrt((real**2) + (img**2)), 2)

    ang = round(math.degrees(math.atan2(img, real)), 2)
    return (mod, ang)


if __name__ == "__main__":
    doctest.testmod()
