from __future__ import annotations

COULOMB_CONSTANT = 8.99e9  # N·m²/C², Coulomb's constant
"""reference: https://en.wikipedia.org/wiki/Electric_potential"""


def electric_potential_point_charge(charge: float, distance: float) -> float:
    """
    Calculate the electric potential at a point due to a point charge.

    Parameters:
    - charge (float): The charge in Coulombs.
    - distance (float): The distance from the charge in meters.

    Returns:
    - float: The electric potential at the point.

    Raises:
    - ValueError: If both charge and distance are zero, or if distance is negative.

    Examples:
    >>> electric_potential_point_charge(1e-6, 0.05)
    179800.0
    >>> electric_potential_point_charge(0, 0.05)
    0
    >>> electric_potential_point_charge(1e-6, 0)
    inf
    >>> electric_potential_point_charge(1e-6, -0.05)
    Traceback (most recent call last):
        ...
    ValueError: Distance cannot be negative.
    """
    if distance < 0:
        raise ValueError("Distance cannot be negative.")
    elif distance == 0 and charge == 0:
        raise ValueError("Charge and distance cannot both be zero.")
    elif distance == 0:
        return float("inf")  # Potential is infinity when distance is zero
    elif charge == 0:
        return 0  # Zero potential for zero charge
    return (COULOMB_CONSTANT * charge) / distance


if __name__ == "__main__":
    import doctest

    doctest.testmod()
