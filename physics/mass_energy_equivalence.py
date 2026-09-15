"""
Title:
Finding the energy equivalence of mass and mass equivalence of energy
by Einstein's equation.

Description:
Einstein's mass-energy equivalence is a pivotal concept in theoretical physics.
It asserts that energy (E) and mass (m) are directly related by the speed of
light in vacuum (c) squared, as described in the equation E = mc². This means that
mass and energy are interchangeable; a mass increase corresponds to an energy increase,
and vice versa. This principle has profound implications in nuclear reactions,
explaining the release of immense energy from minuscule changes in atomic nuclei.

Equations:
E = mc² and m = E/c², where m is mass, E is Energy, c is speed of light in vacuum.

Reference:
https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence
"""

from scipy.constants import c  # speed of light in vacuum (299792458 m/s)


def energy_from_mass(mass: float) -> float:
    """
    Calculates the Energy equivalence of the Mass using E = mc²
    in SI units J from Mass in kg.

    mass (float): Mass of body.

    Usage example:
    >>> energy_from_mass(124.56)
    1.11948945063458e+19
    >>> energy_from_mass(320)
    2.8760165719578165e+19
    >>> energy_from_mass(0)
    0.0
    >>> energy_from_mass(-967.9)
    Traceback (most recent call last):
        ...
    ValueError: Mass can't be negative.

    """
    if mass < 0:
        raise ValueError("Mass can't be negative.")
    return mass * c**2


def mass_from_energy(energy: float) -> float:
    """
    Calculates the Mass equivalence of the Energy using m = E/c²
    in SI units kg from Energy in J.

    energy (float): Mass of body.

    Usage example:
    >>> mass_from_energy(124.56)
    1.3859169098203872e-15
    >>> mass_from_energy(320)
    3.560480179371579e-15
    >>> mass_from_energy(0)
    0.0
    >>> mass_from_energy(-967.9)
    Traceback (most recent call last):
        ...
    ValueError: Energy can't be negative.

    """
    if energy < 0:
        raise ValueError("Energy can't be negative.")
    return energy / c**2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
