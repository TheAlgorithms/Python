# Einstein's Energy-Mass Equivalence #9191 (https://github.com/TheAlgorithms/Python/issues/9191)

# https://www.github.com/JehanPatel

# What is Einstein's Energy-Mass Equivalence
# It expresses the fact that mass and energy are the same physical entity and can be changed into each other.
# Refer https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence for more information on the topic.

# Module for Einstein's Energy-Mass Equivalence.


def calculate_energy_equivalent(mass):
    """
    Calculate the energy equivalent of a given mass.

    :param mass: Mass in kilograms
    :type mass: float
    :return: Energy equivalent in joules
    :rtype: float
    """
    # Constants
    G = 6.67430e-11  # Gravitational constant
    c = 3.0e8  # Speed of light
    h = 6.62607004e-34  # Planck constant

    # Calculate energy equivalent
    energy_equivalent = mass * c**2

    return energy_equivalent


# Happy Coding!
