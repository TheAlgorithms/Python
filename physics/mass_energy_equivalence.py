"""
Mass-energy equivalence, described by Albert Einstein's E=mc^2 formula, reveals that mass and energy are interchangeable in a system's rest frame. Even when the system is moving, its relativistic energy and mass obey this formula. This principle asserts that a small amount of rest mass corresponds to a significant amount of energy, regardless of matter composition. Invariant mass is a fundamental property unaffected by momentum and is consistent across reference frames. When energy is lost in reactions, an equivalent mass is also lost, releasing energy in various forms. Einstein's groundbreaking idea, originating from special relativity, was published in 1905, and it has since played a crucial role in nuclear and particle physics.

Reference:https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence
"""


import math


def mass_energy_equivalence(mass: float) -> float:
    """
    Calculate energy equivalent of given mass
    >>mass_energy_equivalence(2.1)
    189000000000000000.00
    """
    return "{:.2f}".format(mass * ((3 * 10**8) ** 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
