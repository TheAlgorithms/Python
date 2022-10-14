"""
Formula for calculating pressure in Pascals at given depth.
Discovered by greek mathematician, Archimedes. The principle is named after him
"""


# Acceleration Constant on Earth (unit m/s^2)
g = 9.80665


def archimedes_principle(
    fluid_density: float, volume: float, gravity: float = g
) -> float:
    """
    Calculates buoyant force on object submerged within static fluid.
    Formula for buoyant force also known as Archimedes Principle.

    Fb = ρ * V * g

    Args:
        fluid_density: density of fluid (kg/m^3)
        volume: volume of object / liquid being displaced by object
        gravity: Acceleration from gravity. Gravitational force on system. Default is Earth Gravity
    returns:
        buoyant force on object in Newtons
    """

    if fluid_density <= 0:
        raise ValueError("Impossible fluid density")
    if volume < 0:
        raise ValueError("Impossible Object volume")
    if gravity <= 0:
        raise ValueError("Impossible Gravity")

    return fluid_density * gravity * volume


if __name__ == "__main__":
    import doctest

    # run doctest
    doctest.testmod()

    # demo
    fluid_density = 997
    volume = 0.5
    g = 9.80665
    buoyant_force = archimedes_principle(fluid_density, volume, g)
    print("The buoyant force is", buoyant_force, "N")
