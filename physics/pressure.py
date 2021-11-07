"""
Description :
https://en.wikipedia.org/wiki/Pressure

Pressure is the amount of force applied at right angles to the surface of an object per unit area.
P = F/A

P is the pressure,
F is the magnitude of the normal force,
A is the area of the surface on contact.
"""


def solid_pressure(force: float, area: float) -> float:
    """
    Return the force applied perpendicular to the surface of an object(Pressure).
    >>> solid_pressure(10, 5)
    2.0

    >>> solid_pressure(5.5, 2.1)
    2.619047619047619

    >>> solid_pressure(0, -3)
    Traceback (most recent call last):
    ...
    ValueError: Force and Area must be > 0

    >>> solid_pressure(-4.3, 2)
    Traceback (most recent call last):
    ...
    ValueError: Force must be > 0

    >>> solid_pressure(4, -2)
    Traceback (most recent call last):
    ...
    ValueError: Area must be > 0
    """
    if force <= 0 and area <= 0:
        raise ValueError("Force and Area must be > 0")
    elif force <= 0:
        raise ValueError("Force must be > 0")
    elif area <= 0:
        raise ValueError("Area must be > 0")
    else:
        return force / area


if __name__ == "__main__":

    import doctest

    # run doctest
    doctest.testmod()
