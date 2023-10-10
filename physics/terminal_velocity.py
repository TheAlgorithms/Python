"""
Terminal velocity is defined as the highest velocity attained by an
object falling through a fluid. It is observed when the sum of drag force
and buoyancy is equal to the downward gravity force acting on the
object. The acceleration of the object is zero as the net force acting on
the object is zero.

Vt = ((2 * m * g)/(ρ * A * Cd))^0.5

where :
Vt = Terminal velocity (in m/s)
m = Mass of the falling object (in Kg)
g = Acceleration due to gravity (value taken : 9.8 m/s^2)
ρ = Density of the fluid through which the object is falling (in Kg/m^3)
A = Projected area of the object (in m^2)
Cd = Drag coefficient (dimensionless)
"""


def terminal_velocity(
    mass: float, density: float, area: float, drag_coefficient: float
) -> float:
    """
    >>> terminal_velocity(1, 25, 0.6, 0.77)
    1.3026778945578592
    >>> terminal_velocity(2, 100, 0.45, 0.23)
    1.9461345311993645
    >>> terminal_velocity(5, 50, 0.2, 0.5)
    4.427188724235731
    >>> terminal_velocity(-5, 50, -0.2, -2)
    Traceback (most recent call last):
        ...
    ValueError: mass, density, area and the drag coeffiecient all need to be positive
    >>> terminal_velocity(3, -20, -1, 2)
    Traceback (most recent call last):
        ...
    ValueError: mass, density, area and the drag coeffiecient all need to be positive
    >>> terminal_velocity(-2, -1, -0.44, -1)
    Traceback (most recent call last):
        ...
    ValueError: mass, density, area and the drag coeffiecient all need to be positive
    """
    if mass <= 0 or density <= 0 or area <= 0 or drag_coefficient <= 0:
        raise ValueError(
            "mass, density, area and the drag coeffiecient all need to be positive"
        )
    return ((2 * mass * 9.8) / (density * area * drag_coefficient)) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
