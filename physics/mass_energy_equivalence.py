"""
Mass-energy equivalence
Reference: https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence

This file defines a function to calculate energy (in joules) equivalent to a given
mass (in kilograms) using Einstein's mass-energy equivalence equation E=mc^2,
where m is mass and c = 299,792,458 m/s is the speed of light in a vacuum.

The function takes a single argument mass(in kg) having datatype float and
returns the energy(in joule) having datatype float
"""

SPEED_OF_LIGHT = 299792458


def calculate_energy(mass: float) -> float:
    """
    get energy equivalent of given mass in joules:
    >>> calculate_energy(1.2)
    1.0785062144841811e+17
    >>> calculate_energy(3.0)
    2.6962655362104528e+17
    >>> calculate_energy(5)
    449377589368408820
    >>> calculate_energy(-5)
    Traceback (most recent call last):
      ...
        raise TypeError("Mass cannot be negative")
    TypeError: Mass cannot be negative
    """
    if mass < 0:
        raise TypeError("Mass cannot be negative")
    energy = mass * SPEED_OF_LIGHT**2
    return energy


if __name__ == "__main__":
    mass = float(input("Enter mass (in kilograms): "))
    energy = calculate_energy(mass)
    print(f"Energy equivalent: {energy} joules")
