"""
Title : calculating the Reynolds number for determining the type of flow of a fluid

Reynolds number is a dimensionless quantity that is used to determine
the type of flow pattern as laminar or turbulent while flowing through a
pipe. Reynolds number is defined by the ratio of inertial forces to that
of viscous forces.

Reynolds number = Inertial Force / Viscous Force

R = (ρ*V*D)/μ
where :
R = Reynolds Number (dimensionless)
ρ = Density of the fluid (in Kg/m^3)
V = Velocity of flow (in m/s)
D = Diameter of pipe (in m)
μ = Viscosity of the fluid (in Ns/m^2)

If the Reynolds number calculated is high (greater than 2000), then the
flow through the pipe is said to be turbulent. If Reynolds number is low
(less than 2000), the flow is said to be laminar. Numerically, these are
acceptable values, although in general the laminar and turbulent flows
are classified according to a range. Laminar flow falls below Reynolds
number of 1100 and turbulent falls in a range greater than 2200.

Laminar flow is the type of flow in which the fluid travels smoothly in
regular paths. Conversely, turbulent flow is not smooth and follows an
irregular math with lots of mixing.

Reference : https://byjus.com/physics/reynolds-number/#:~:text=What%20is%20a%20Reynolds%20Number,to%20that%20of%20viscous%20forces.

"""


def reynolds_number(
    density: float, velocity: float, diameter: float, viscosity: float
) -> float:
    """
    >>> reynolds_number(1.3,2,0.05,1)
    0.13
    >>> reynolds_number(1.56,2.2,0.15,2)
    0.2574
    >>> reynolds_number(900,2.5,0.2,0.4)
    1125.0
    >>> reynolds_number(-2,213,2,0.5)
    Traceback (most recent call last):
        ...
    ValueError: Please enter valid non negative inputs,only negative velocity is allowed
    >>> reynolds_number(1.3,-2,0.05,1)
    0.13
    """
    if density <= 0 or diameter <= 0 or viscosity <= 0:
        raise ValueError(
            "Please enter valid non negative inputs,only negative velocity is allowed"
        )
    return (density * abs(velocity) * diameter) / viscosity


if __name__ == "__main__":
    import doctest

    doctest.testmod()
