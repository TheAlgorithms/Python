c = 299792458


def energy_equivalence(mass_kg):
    # Check if the mass is non-negative
    if mass < 0:
        raise ValueError("mass should be positive")

    # Check if the speed of light is positive
    if c <= 0:
        raise ValueError("Speed of light must be positive")

    # Calculate energy using the mass-energy equivalence equation
    energy = mass * c**2
    return energy


if __name__ == "__main__":
    energy_equivalence()
