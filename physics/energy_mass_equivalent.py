import doctest
import math
import scipy.constants


def energy_equivalent_for_stationary_mass(mass_kg: float) -> float | ValueError:
    """
    Calculate the energy equivalent for a given mass using E=mc^2.

    Wikipedia link:
    "https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence"

    Parameters:
        mass_kg (float): Mass in kilograms.
        (must be positive)

    Returns:
        float: Energy equivalent in joules.

    >>> energy_equivalent_for_stationary_mass(4)
    3.5950207149472704e+17

    """
    if mass_kg < 0:
        ValueError("mass of object cannot be negative")

    speed_of_light = scipy.constants.speed_of_light  # Speed of light in meters/second
    energy_joules = mass_kg * (speed_of_light**2)
    return energy_joules


def energy_equivalent_for_moving_mass(
    mass_kg: float, velocity_m_s: float
) -> float | ValueError:
    """
    Calculate the energy equivalent for a moving mass using
    relativistic energy-momentum relation
    (E^2= m^2*c^4 +p^2*c^2).

    Parameters:
        mass_kg (float): Mass in kilograms.
        (must be positive)
        velocity_m_s (float): Velocity in meters per second.
        (can be negative as well as positive)

    Returns:
        float: Energy equivalent in joules.

    >>> energy_equivalent_for_moving_mass(1,5675)
    1701322225868.2546
    """
    if mass_kg < 0:
        ValueError("mass of object cannot be negative")

    speed_of_light = scipy.constants.speed_of_light  # Speed of light in meters/second

    # Calculating momentum
    momentum = (
        mass_kg
        * velocity_m_s
        / math.sqrt(1 - (velocity_m_s**2 / speed_of_light**2))
    )

    # Calculating energy using the relativistic energy-momentum relation
    energy_joules = math.sqrt(
        (mass_kg * speed_of_light) ** 2 + (momentum * speed_of_light) ** 2
    )
    return energy_joules


if __name__ == "__main__":
    doctest.testmod()
