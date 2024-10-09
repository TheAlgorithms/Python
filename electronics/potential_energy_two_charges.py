"""Reference: https://en.wikipedia.org/wiki/Electric_potential_energy"""

from __future__ import annotations

k_e = 8.99 * (10**9)  # N·m²/C², Coulomb's constant


def potential_energy_2_charges(
    charge_1: float,
    charge_2: float,
    distance: float,
) -> float:
    """
    Calculate the potential energy due to two charges.

    Parameters:
    - charge_1 (float): The charge in Coulombs.
    - charge_2 (float): The charge in Coulombs.
    - distance (float): The distance between the charges in meters.

    Returns:
    - float: The potential energy.

    Raises:
    - ValueError: If distance is less than zero.

    Examples:
    >>> potential_energy_2_charges(1e-6, 1e-6, 0.01)
    0.899
    >>> potential_energy_2_charges(2e-6, 3e-6, 0.05)
    1.0788
    >>> potential_energy_2_charges(0, 3e-6, 0.05)
    0
    >>> potential_energy_2_charges(2e-6, 3e-6, 0)
    inf
    >>> potential_energy_2_charges(2e-6, 3e-6, -0.05)
    Traceback (most recent call last):
        ...
    ValueError: Distance must be greater than zero.
    """
    if charge_1 == 0 or charge_2 == 0:
        return 0
    if distance <= 0:
        if distance == 0:
            return float("inf")
        raise ValueError("Distance must be greater than zero.")

    potential_energy = k_e * charge_1 * charge_2 / distance
    return round(potential_energy, 6)  # Round for precision


if __name__ == "__main__":
    import doctest

    doctest.testmod()
