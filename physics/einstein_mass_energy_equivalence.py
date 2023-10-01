# Einstein's Mass-Energy Equivalence
# This code calculates the energy equivalent of a given mass using Einstein's mass-energy equivalence equation, E=mc².

# Source: https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence


def mass_energy_equivalence(mass: float, c: float = 299792458) -> float:
    """
    Calculate the energy equivalent of a given mass using Einstein's mass-energy equivalence equation, E=mc².

    Args:
        mass (float): Mass in kilograms.
        c (float): Speed of light in meters per second (default value is the speed of light in a vacuum).

    Returns:
        float: Energy equivalent in joules.

    Examples:
        >>> mass_energy_equivalence(1)
        8.987551787368176e+16
        >>> mass_energy_equivalence(5, 3e8)
        1.125937723421022e+18
    """
    if mass < 0:
        raise ValueError("Mass cannot be negative")
    if c <= 0:
        raise ValueError("Speed of light must be positive")

    energy = mass * c**2
    return energy


if __name__ == "__main__":
    import doctest

    # Run doctests
    doctest.testmod()
