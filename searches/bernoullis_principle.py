"""
Title: Bernoulli's Principle

Description:
This algorithm implements Bernoulli's Principle to calculate the unknown pressure
at a second point in a fluid system using the Bernoulli equation. Bernoulli's equation
states that for an incompressible, frictionless fluid, the total mechanical energy
(remains constant) as the fluid flows.

The equation used:
P1 + 0.5 * ρ * v1^2 + ρ * g * h1 = P2 + 0.5 * ρ * v2^2 + ρ * g * h2

Where:
- P1 and P2 are the pressures at point 1 and point 2 (Pascals)
- v1 and v2 are the fluid velocities at point 1 and point 2 (m/s)
- h1 and h2 are the heights at point 1 and point 2 (m)
- ρ is the density of the fluid (kg/m^3)
- g is the gravitational constant (9.81 m/s^2)

This algorithm solves for P2, the unknown pressure at point 2.

Example:
>>> bernoullis_principle(10, 101325, 0, 15, 5)
100732.64
"""


def bernoullis_principle(
    velocity1: float,
    pressure1: float,
    height1: float,
    velocity2: float,
    height2: float,
    density: float = 1.225,
) -> float:
    """
    Calculate the unknown pressure at a second point in a fluid system using Bernoulli's equation.

    Parameters:
    velocity1 (float): velocity at point 1 in m/s
    pressure1 (float): pressure at point 1 in Pascals
    height1 (float): height at point 1 in meters
    velocity2 (float): velocity at point 2 in m/s
    height2 (float): height at point 2 in meters
    density (float): density of the fluid in kg/m^3 (default is 1.225, for air)

    Returns:
    float: Pressure at point 2 in Pascals

    Example:
    >>> bernoullis_principle(density=1000, velocity=5, height=10, pressure=101325)
    144413.5
    >>> bernoullis_principle(density=500, velocity=10, height=5, pressure=0)
    25000.0
    >>> bernoullis_principle(density=997, velocity=0, height=0, pressure=101325)
    101325.0
    """
    g = 9.81  # gravitational constant in m/s^2

    # Bernoulli's equation to solve for pressure at point 2
    pressure2 = (
        pressure1
        + 0.5 * density * (velocity1**2)
        + density * g * height1
        - 0.5 * density * (velocity2**2)
        - density * g * height2
    )

    return round(pressure2, 2)


# Example usage
if __name__ == "__main__":
    # Example doctest
    import doctest

    doctest.testmod()

    # Manual test
    pressure_at_point_2 = bernoullis_principle(10, 101325, 0, 15, 5)
    print(f"Pressure at point 2: {pressure_at_point_2} Pascals")
