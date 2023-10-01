def energy_equivalence(mass_kg):
    # Check if the mass is non-negative
    if mass_kg < 0:
        raise ValueError("mass should be positive")

    # Check if the speed of light is positive
    if speed_of_light_m_per_s <= 0:
        raise ValueError("Speed of light must be positive")

    # Calculate energy using the mass-energy equivalence equation
    energy = mass_kg * speed_of_light_m_per_s**2
    return energy


if __name__ == "__main__":
    energy_equivalence()
