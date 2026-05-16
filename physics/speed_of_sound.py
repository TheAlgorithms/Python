"""
Title : Calculating the speed of sound

Description :
    The speed of sound (c) is the speed that a sound wave travels per unit time (m/s).
    During propagation, the sound wave propagates through an elastic medium.

    Sound propagates as longitudinal waves in liquids and gases and as transverse waves
    in solids. This file calculates the speed of sound in a fluid based on its bulk
    module and density.

    Equation for the speed of sound in a fluid:
    c_fluid = sqrt(K_s / p)

    c_fluid: speed of sound in fluid
    K_s: isentropic bulk modulus
    p: density of fluid

Source : https://en.wikipedia.org/wiki/Speed_of_sound
"""


def speed_of_sound_in_a_fluid(density: float, bulk_modulus: float) -> float:
    """
    Calculates the speed of sound in a fluid from its density and bulk modulus

    Examples:
    Example 1 --> Water 20°C: bulk_modulus= 2.15MPa, density=998kg/m³
    Example 2 --> Mercury 20°C: bulk_modulus= 28.5MPa, density=13600kg/m³

    >>> speed_of_sound_in_a_fluid(bulk_modulus=2.15e9, density=998)
    1467.7563207952705
    >>> speed_of_sound_in_a_fluid(bulk_modulus=28.5e9, density=13600)
    1447.614670861731
    """

    if density <= 0:
        raise ValueError("Impossible fluid density")
    if bulk_modulus <= 0:
        raise ValueError("Impossible bulk modulus")

    return (bulk_modulus / density) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
