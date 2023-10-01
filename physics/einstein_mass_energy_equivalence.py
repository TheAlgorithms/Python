# Calculate Energy from Mass using Einstein's Mass-Energy Equivalence

# This Python script calculates the energy equivalent of a given mass using Albert Einstein's mass-energy equivalence equation, E=mc².
# The formula E=mc² states that energy (energy_equivalent) is equal to mass (mass_kg) multiplied by the speed of light (speed_of_light_m_per_s) squared.

# Source: https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence

def calculate_energy_from_mass(mass_kg: float, speed_of_light_m_per_s: float = 299792458) -> float:
    """
    Calculate the energy equivalent of a given mass using Einstein's mass-energy equivalence equation, E=mc².

    Args:
        mass_kg (float): Mass in kilograms.
        speed_of_light_m_per_s (float): Speed of light in meters per second (default value is the speed of light in a vacuum).

    Returns:
        float: Energy equivalent in joules.

    Examples:
        >>> calculate_energy_from_mass(1)
        8.987551787368176e+16
        >>> calculate_energy_from_mass(5, 3e8)
        1.125937723421022e+18
    """
    # Check if the mass is non-negative
    if mass_kg < 0:
        raise ValueError("Mass cannot be negative")
    
    # Check if the speed of light is positive
    if speed_of_light_m_per_s <= 0:
        raise ValueError("Speed of light must be positive")

    # Calculate energy using the mass-energy equivalence equation
    energy_equivalent_joules = mass_kg * speed_of_light_m_per_s**2
    
    # Return the energy equivalent in joules
    return energy_equivalent_joules

if __name__ == "__main__":
    # Import the doctest module to run tests
    import doctest

    # Run doctests to verify the function's correctness
    doctest.testmod()
