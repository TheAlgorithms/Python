"""
Title : computing the Reynolds number to find
        out the type of flow (laminar or turbulent)

Reynolds number is a dimensionless quantity that is used to determine
the type of flow pattern as laminar or turbulent while flowing through a
pipe. Reynolds number is defined by the ratio of inertial forces to that of
viscous forces.

R = Inertial Forces / Viscous Forces
R = (p * V * D)/μ

where :
p = Density of fluid (in Kg/m^3)
D = Diameter of pipe through which fluid flows (in m)
V = Velocity of flow of the fluid (in m/s)
μ = Viscosity of the fluid (in Ns/m^2)

If the Reynolds number calculated is high (greater than 2000), then the
flow through the pipe is said to be turbulent. If Reynolds number is low
(less than 2000), the flow is said to be laminar. Numerically, these are
acceptable values, although in general the laminar and turbulent flows
are classified according to a range. Laminar flow falls below Reynolds
number of 1100 and turbulent falls in a range greater than 2200.
Laminar flow is the type of flow in which the fluid travels smoothly in
regular paths. Conversely, turbulent flow isn't smooth and follows an
irregular path with lots of mixing.

Reference : https://byjus.com/physics/reynolds-number/
"""


def reynolds_number(
    density: float, velocity: float, diameter: float, viscosity: float
) -> float:
    """
    >>> reynolds_number(900, 2.5, 0.05, 0.4)
    281.25
    >>> reynolds_number(450, 3.86, 0.078, 0.23)
    589.0695652173912
    >>> reynolds_number(234, -4.5, 0.3, 0.44)
    717.9545454545454
    >>> reynolds_number(-90, 2, 0.045, 1)
    Traceback (most recent call last):
        ...
    ValueError: please ensure that density, diameter and viscosity are positive
    >>> reynolds_number(0, 2, -0.4, -2)
    Traceback (most recent call last):
        ...
    ValueError: please ensure that density, diameter and viscosity are positive
    """

    if density <= 0 or diameter <= 0 or viscosity <= 0:
        raise ValueError(
            "please ensure that density, diameter and viscosity are positive"
        )
    return (density * abs(velocity) * diameter) / viscosity


if __name__ == "__main__":
    import doctest

    doctest.testmod()
