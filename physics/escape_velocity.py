"""
Title: Calculate Escape Velocity

Description:
    Calculate the escape velocity required for an object to leave the
    gravitational influence of a celestial body.
"""

import math


def escape_velocity(mass_celestial_body: float, distance_from_center: float) -> float:
    """
    Calculate the escape velocity required for an object to leave the
    gravitational influence of a celestial body.

    Formula:
    escape_velocity = sqrt(2 * gravitational_constant * mass_celestial_body /
    distance_from_center)

    Parameters:
    - mass_celestial_body (float): Mass of the celestial body in kilograms.
    - distance_from_center (float): Distance from the center of the celestial
    body in meters.

    Constants:
    - gravitational_constant (float): Universal gravitational constant in SI
    units (6.67430e-11 m³/kg/s²).

    Examples:
    >>> escape_velocity(mass_celestial_body=5.972e24, distance_from_center=6.371e6)
    11188.464977716847
    >>> escape_velocity(mass_celestial_body=1.989e30, distance_from_center=6.9634e8)
    617713.607596756
    >>> escape_velocity(mass_celestial_body=3.3011e23, distance_from_center=3.3895e6)
    5651.451689426722
    >>> escape_velocity(mass_celestial_body=0.0, distance_from_center=6.371e6)
    0.0
    >>> escape_velocity(mass_celestial_body=1e-4, distance_from_center=1e-4)
    Traceback (most recent call last):
      ...
    ValueError: Mass of celestial body must be greater than zero!
    >>> escape_velocity(mass_celestial_body=5.972e24, distance_from_center=0.0)
    Traceback (most recent call last):
      ...
    ValueError: Distance from the center must be greater than zero!

    """
    if mass_celestial_body <= 0:
        raise ValueError("Mass of celestial body must be greater than zero!")

    if distance_from_center <= 0:
        raise ValueError("Distance from the center must be greater than zero!")

    gravitational_constant = 6.67430e-11  # Universal gravitational constant in SI units
    return math.sqrt(
        2 * gravitational_constant * mass_celestial_body / distance_from_center
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
