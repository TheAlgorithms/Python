import doctest

"""



Finding the kinetic energy of an object,by taking its mass and velocity as input


Description : In physics, the kinetic energy of an object is the energy that it possesses due to its motion.
It is defined as the work needed to accelerate a body of a given mass from rest to its stated velocity.
Having gained this energy during its acceleration, the body maintains this kinetic energy unless its speed changes.
The same amount of work is done by the body when decelerating from its current speed to a state of rest.
Formally, a kinetic energy is any term in a system's Lagrangian which includes a derivative with respect to time.

In classical mechanics, the kinetic energy of a non-rotating object of mass m traveling at a speed v is ½mv².
In relativistic mechanics, this is a good approximation only when v is much less than the speed of light.
The standard unit of kinetic energy is the joule, while the English unit of kinetic energy is the foot-pound.

Reference : "https://en.m.wikipedia.org/wiki/Kinetic_energy"

"""


def kinetic_energy(
    mass: float, velocity: float
) -> float:  # function will accept mass and velocity as parameters and return kinetic energy
    if mass < 0:
        raise ValueError("The mass of a body cannot be negative")
    elif mass >= 0:
        ke = 0.5 * mass * abs(velocity) * abs(velocity)
    return ke


if __name__ == "__main__":
    doctest.testmod()
