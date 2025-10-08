"""
Calculate the magnetic field (B) produced by a long straight current-carrying
conductor at a distance r from the wire in free space.

Equation for calculating magnetic field:
B = (μ₀ * I) / (2 * π * r)

where:
B = Magnetic field (Tesla, T)
μ₀ = Permeability of free space (4π × 10⁻⁷ T·m/A)
I = Current (Amperes, A)
r = Perpendicular distance from the wire (meters, m)

https://en.wikipedia.org/wiki/Biot–Savart_law
"""

import math

# Magnetic constant (Permeability of free space) in T·m/A
mu_0 = 4 * math.pi * 1e-7


def magnetic_field(current: float, distance: float, permeability: float = mu_0) -> float:
    """
    Args:
        current: electric current through the wire (Amperes, A)
        distance: perpendicular distance from the wire (meters, m)
        permeability: permeability of the medium (T·m/A),
            default is free space permeability (μ₀)

    returns:
        the magnetic field strength at the given point (Tesla, T)

    >>> magnetic_field(current=10, distance=0.05)
    3.9999999999999996e-05
    >>> magnetic_field(current=5, distance=0.1)
    1.0e-05
    >>> magnetic_field(current=0, distance=0.1)
    0.0
    >>> magnetic_field(current=-5, distance=0.1)
    Traceback (most recent call last):
        ...
    ValueError: Impossible current
    >>> magnetic_field(current=5, distance=-0.1)
    Traceback (most recent call last):
        ...
    ValueError: Impossible distance
    >>> magnetic_field(current=5, distance=0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Distance cannot be zero
    """

    if current < 0:
        raise ValueError("Impossible current")
    if distance < 0:
        raise ValueError("Impossible distance")
    if distance == 0:
        raise ZeroDivisionError("Distance cannot be zero")

    return (permeability * current) / (2 * math.pi * distance)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
