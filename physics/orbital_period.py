"""
The time period of a satellite is the time taken by a satellite to
complete one full orbit around a celestial body.

T = 2π * sqrt((R + h)^3 / (G * M))

G is the Universal Gravitational Constant and equals 6.674 X 10^-11 N m²/kg²
M is the mass of the celestial body (kg)
R is the radius of the celestial body (m)
h is the height of the satellite above the surface (m)

Reference: https://en.wikipedia.org/wiki/Orbital_period
"""


def time_period_of_satellite(mass: float, radius: float, height: float) -> float:
    """
    Calculate the time period of a satellite orbiting a celestial body

    >>> time_period_of_satellite(5.972e24, 6.371e6, 3.5e5)
    5562.65
    >>> time_period_of_satellite(5.972e24, 6.371e6, 0)
    5060.84
    >>> time_period_of_satellite(7.342e22, 1.737e6, 1.0e5)
    7045.95
    >>> time_period_of_satellite(6.39e23, 3.389e6, 3.0e5)
    7113.64
    >>> time_period_of_satellite(-5.972e24, 6.371e6, 3.5e5)
    Traceback (most recent call last):
        ...
    ValueError: Mass must be a positive value
    >>> time_period_of_satellite(5.972e24, -6.371e6, 3.5e5)
    Traceback (most recent call last):
        ...
    ValueError: Radius must be a positive value
    >>> time_period_of_satellite(5.972e24, 6.371e6, -3.5e5)
    Traceback (most recent call last):
        ...
    ValueError: Height must be a non-negative value
    """
    if mass <= 0:
        raise ValueError("Mass must be a positive value")
    if radius <= 0:
        raise ValueError("Radius must be a positive value")
    if height < 0:
        raise ValueError("Height must be a non-negative value")

    import math
    return round(2 * math.pi * ((radius + height) ** 3 / (6.674e-11 * mass)) ** 0.5, 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    