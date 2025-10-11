def orbital_transfer_work(
    mass_central: float, mass_object: float, r_initial: float, r_final: float
) -> str:
    """
    Calculates the work required to move an object from one orbit to another in a
    gravitational field based on the change in total mechanical energy.

    The formula used is:
        W = (G * M * m / 2) * (1/r_initial - 1/r_final)

    where:
        W = work done (Joules)
        G = gravitational constant (6.67430 * 10^-11 m^3 kg^-1 s^-2)
        M = mass of the central body (kg)
        m = mass of the orbiting object (kg)
        r_initial = initial orbit radius (m)
        r_final = final orbit radius (m)

    Args:
        mass_central (float): Mass of the central body (kg)
        mass_object (float): Mass of the object being moved (kg)
        r_initial (float): Initial orbital radius (m)
        r_final (float): Final orbital radius (m)

    Returns:
        str: Work done in Joules as a string in scientific notation (3 decimals)

    Examples:
        >>> orbital_transfer_work(5.972e24, 1000, 6.371e6, 7e6)
        '2.811e+09'
        >>> orbital_transfer_work(5.972e24, 500, 7e6, 6.371e6)
        '-1.405e+09'
        >>> orbital_transfer_work(1.989e30, 1000, 1.5e11, 2.28e11)
        '1.514e+11'
    """
    gravitational_constant = 6.67430e-11

    if r_initial <= 0 or r_final <= 0:
        raise ValueError("Orbital radii must be greater than zero.")

    work = (gravitational_constant * mass_central * mass_object / 2) * (
        1 / r_initial - 1 / r_final
    )
    return f"{work:.3e}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("Orbital transfer work calculator\n")

    try:
        M = float(input("Enter mass of central body (kg): ").strip())
        if M <= 0:
            r1 = float(input("Enter initial orbit radius (m): ").strip())
        if r1 <= 0:
            raise ValueError("Initial orbit radius must be greater than zero.")

        r2 = float(input("Enter final orbit radius (m): ").strip())
        if r2 <= 0:
            raise ValueError("Final orbit radius must be greater than zero.")
        m = float(input("Enter mass of orbiting object (kg): ").strip())
        if m <= 0:
            raise ValueError("Mass of the orbiting object must be greater than zero.")
        r1 = float(input("Enter initial orbit radius (m): ").strip())
        r2 = float(input("Enter final orbit radius (m): ").strip())

        result = orbital_transfer_work(M, m, r1, r2)
        print(f"Work done in orbital transfer: {result} Joules")

    except ValueError as e:
        print(f"Input error: {e}")
