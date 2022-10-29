"""
Find the kinetic energy of an object, given its mass and velocity.

Description : In physics, the kinetic energy of an object is the energy that it
possesses due to its motion.  It is defined as the work needed to accelerate a body of a
given mass from rest to its stated velocity.  Having gained this energy during its
acceleration, the body maintains this kinetic energy unless its speed changes.  The same
amount of work is done by the body when decelerating from its current speed to a state
of rest.  Formally, a kinetic energy is any term in a system's Lagrangian which includes
a derivative with respect to time.

In classical mechanics, the kinetic energy of a non-rotating object of mass m traveling
at a speed v is ½mv².  In relativistic mechanics, this is a good approximation only when
v is much less than the speed of light.  The standard unit of kinetic energy is the
joule, while the English unit of kinetic energy is the foot-pound.

Reference : https://en.m.wikipedia.org/wiki/Kinetic_energy
"""


def kinetic_energy(mass: float, velocity: float) -> float:
    """
    Calculate kinetick energy.

    The kinetic energy of a non-rotating object of mass m traveling at a speed v is ½mv²

    >>> kinetic_energy(10,10)
    500.0
    >>> kinetic_energy(0,10)
    0.0
    >>> kinetic_energy(10,0)
    0.0
    >>> kinetic_energy(20,-20)
    4000.0
    >>> kinetic_energy(0,0)
    0.0
    >>> kinetic_energy(2,2)
    4.0
    >>> kinetic_energy(100,100)
    500000.0
    """
    if mass < 0:
        raise ValueError("The mass of a body cannot be negative")
    return 0.5 * mass * abs(velocity) * abs(velocity)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
