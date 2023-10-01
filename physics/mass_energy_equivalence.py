"""
Einstein's E=mc^2: Mass-energy interchange,
even in motion. Small rest mass yields big
energy,invariant across frames. Lost energy
means lost mass.Einstein's 1905 theory, vital
in nuclear and particle physics.

Reference:Wikipedia
"""


def energy_mass_equivalence(mass: float) -> float:
    """
    Converted mass into corresponding energy

    For example:
    >>>energy_mass_equivalence(2.1)
    189000000000000000.00
    >>>energy_mass_equivalence(3)
    270000000000000000.00
    >>>energy_mass_equivalence(3.123)
    281070000000000032.00
    >>.energy_mass_equivalence(1)
    90000000000000000.00
    """
    energy = mass * ((3 * 10**8) ** 2)
    return f"{energy:.2f}"


# test
if __name__ == "__main__":
    import doctest

    doctest.testmod(name="mass_energy_equivalence")
