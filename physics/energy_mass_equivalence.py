"""
Calculates the energy equivalent (in J) of a given mass (in kg).

- In physics, mass–energy equivalence is the relationship between mass and energy in a system's rest frame.
- The two quantities differ only by a multiplicative constant and the units of measurement.
- The principle is described by the physicist Albert Einstein's formula: E = mc².

Source: https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence

"""


def energy_eq(mass: float) -> float:
    """
    Calculate energy equivalent.
    The energy equivalent of a mass m is mc², where c is the speed of light.

    >>> energy_eq(0.001)
    89875517873681.77

    """
    if mass < 0:
        raise ValueError("The mass of a body cannot be negative")
    c = 2.99792458e8
    return mass * c**2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
