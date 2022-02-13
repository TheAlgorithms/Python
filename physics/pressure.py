"""
Description :
https://en.wikipedia.org/wiki/Pressure

- Solid Pressure
P = F/A
P is the pressure,
F is the magnitude of the normal force,
A is the area of the surface on contact.

- Liquid Pressure
https://en.wikipedia.org/wiki/Pressure#Liquid_pressure
P = d*g*h
P is liquid pressure,
g is gravity at the surface of overlaying material,
d is density of liquid,
h is height of liquid column or depth within a substance.
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


def liquid_pressure(density: float, gravity: float, height: float) -> float:
    """
    >>> liquid_pressure(1, 10, 2)
    20

    >>> liquid_pressure(3.7, 6.2, 9.1)
    208.754

    >>> liquid_pressure(-1, 10, 2)
    Traceback (most recent call last):
    ...
    ValueError: Density must be > 0

    >>> liquid_pressure(2, -5, 7)
    Traceback (most recent call last):
    ...
    ValueError: Gravity must be > 0

    >>> liquid_pressure(5, 23, -5)
    Traceback (most recent call last):
    ...
    ValueError: Height must be > 0
    """
    if density < 0 and gravity < 0 and height < 0:
        raise ValueError("Density, gravity and height must be > 0")
    elif density < 0:
        raise ValueError("Density must be > 0")
    elif gravity < 0:
        raise ValueError("Gravity must be > 0")
    elif height < 0:
        raise ValueError("Height must be > 0")
    else:
        return density * gravity * height


if __name__ == "__main__":
    import doctest

    # run doctest
    doctest.testmod()
