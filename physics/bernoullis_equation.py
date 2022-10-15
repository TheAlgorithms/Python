"""


Source:
- https://courses.lumenlearning.com/suny-osuniversityphysics/chapter/14-6-bernoullis-equation/
"""

# Acceleration Constant on Earth (unit m/s^2)
g = 9.80665


def bernoulli_static_equation(
    fluid_density: float, h: float, gravity: float = g, initial_pressure: float = 0
) -> float:
    """
    Bernoulli's equation for static fluids.
    Calculate pressure from static fluid at given depth.

    Pascals law, "a pressure change at any point in a confined incompressible fluid,
    is transmitted throughout the fluid such that the same change occurs everywhere"
    According to Pascals law, the pressure will be the same at a given depth,
    regardless of whether this is a submerged object or a force on container wall.

    This function models:
    P (pressure) = h (depth) * ρ (density) * g (gravity)
    P = hρg

    In addition to this equation being used independently to calculate pressure at a depth,
    It is a component of bernoulli's principle.


    Args:
        fluid_density: Density of fluid within which pressure is being calculated
        h: depth at which pressure is being calculated.
        gravity: Acceleration from gravity. Default is Earth Gravity
        initial_pressure: represents any external pressure acting on system (Pa)
    returns:
        Pressure at given depth in Pa (Pascals)


    >>> bernoulli_static_equation(fluid_density=997, h=5)
    48886.15025

    >>> bernoulli_static_equation(fluid_density=997, h=5, gravity=9.8)
    48853.0

    >>> bernoulli_static_equation(fluid_density=997, h=5, gravity=9.8, initial_pressure=3.7)
    48856.7
    """

    if fluid_density <= 0:
        raise ValueError("Impossible fluid density")
    if h < 0:
        raise ValueError("Impossible depth")
    if gravity <= 0:
        raise ValueError("Impossible Gravity")

    return fluid_density * h * gravity + initial_pressure


def bernoulli_fluid_equation(
    fluid_density: float, fluid_velocity: float, initial_pressure: float = 0
) -> float:
    """
    Calculates pressure/fluids-kinetic-energy - work of a dynamic non-compressible fluid through a tube

    Bernoulli's Equation:
        W = P1 + 0.5*ρ*v^2

    Args:
        fluid_density: Density of fluid within which pressure is being calculated
        fluid_velocity: Velocity at which the fluid is travelling at
        initial_pressure: represents any external pressure acting on system (Pa)
   Returns:
        Pressure of system in Pa (Pascals)

    >>> bernoulli_fluid_equation(fluid_density=997, fluid_velocity=0.7)
    244.26499999999996
    >>> bernoulli_fluid_equation(fluid_density=997, fluid_velocity=0.7, initial_pressure=2)
    246.26499999999996
    """

    if fluid_density <= 0:
        raise ValueError("Impossible fluid density")

    return 0.5 * fluid_density * fluid_velocity ** 2 + initial_pressure


def bernoulli_full_equation(
    fluid_density: float,
    fluid_velocity: float = 0,
    h: float = 0,
    gravity: float = g,
    initial_pressure: float = 0,
) -> float:
    """
    Bernoulli's equation represents the relation of (Pressure, KE, and GPE) of a non-compressible,
    frictionless fluid within a container.

    P1 + 0.5*ρ*v1^2 + ρgh1 = P2 + 0.5*ρ*v2^2 + ρgh2
    or
    P + 0.5*ρ*v^2 + ρgh = constant

    Equation is often rearranged to solve for different variables

    Args:
        fluid_density: Density of fluid within which pressure is being calculated
        fluid_velocity: Velocity at which the fluid is travelling at
        h: height difference between two pressures being compared
        gravity: Acceleration from gravity. Default is Earth Gravity
        initial_pressure: represents any external pressure acting on system (Pa), Default = 0
   Returns:
        Pressure of system in Pa (Pascals)


    >>> bernoulli_full_equation(fluid_density=997, fluid_velocity=0.2, h=5, gravity=9.8, initial_pressure=7)
    48879.94
    >>> bernoulli_full_equation(fluid_density=997, fluid_velocity=0.2, h=5, gravity=9.8)
    48872.94
    >>> bernoulli_full_equation(fluid_density=997, fluid_velocity=0.2, h=5)
    48906.09025
    >>> bernoulli_full_equation(fluid_density=997, h=9)
    87995.07045
    """

    return (
        bernoulli_fluid_equation(fluid_density=fluid_density, fluid_velocity=fluid_velocity)
        + bernoulli_static_equation(fluid_density=fluid_density, h=h, gravity=gravity)
        + initial_pressure
    )


if __name__ == '__main__':
    import doctest

    # run doctest
    doctest.testmod()
