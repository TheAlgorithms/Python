"""
Calculates buoyant force on object submerged within static fluid.
Discovered by greek mathematician, Archimedes. The principle is named after him.

Equation for calculating buoyant force:
Fb = ρ * V * g

Source:
- https://en.wikipedia.org/wiki/Archimedes%27_principle
"""


# Acceleration Constant on Earth (unit m/s^2)
g = 9.80665


def archimedes_principle(
    fluid_density: float, volume: float, gravity: float = g
) -> float:
    """
    Args:
        fluid_density: density of fluid (kg/m^3)
        volume: volume of object / liquid being displaced by object
        gravity: Acceleration from gravity. Gravitational force on system,
            Default is Earth Gravity
    returns:
        buoyant force on object in Newtons

    >>> archimedes_principle(fluid_density=997, volume=0.5, gravity=9.8)
    4885.3
    >>> archimedes_principle(fluid_density=997, volume=0.7)
    6844.061035
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
