"""
Find the relativistic kinetic energy of a particle, given its rest mass and velocity.

Description: In special relativity, the kinetic energy of a particle is the extra
energy it has due to its motion beyond the energy associated with its rest mass.
It is defined as the difference between the total relativistic energy and the rest
energy of the particle. After a force does work to accelerate a particle from rest
to some high speed comparable to the speed of light, the particle carries this
relativistic kinetic energy as long as its speed stays the same. The same amount of
energy must be removed (for example, by an opposite force) to slow the particle
back down to rest. Formally, relativistic kinetic energy appears in the relativistic
energy momentum relation and depends on the Lorentz factor, which encodes how time
and space change at high speeds.

In relativistic mechanics, the kinetic energy K of a particle with rest mass m
moving at speed v is

    K = (y - 1) m c^2,

where c is the speed of light in vacuum and

    y = 1 / sqrt(1 - v^2 / c^2)

is the Lorentz factor. At speeds much smaller than c, this expression reduces to the
classical formula K ≈ (1/2) m v^2, so the relativistic result agrees with Newtonian
kinetic energy in the low velocity limit.The standard unit of kinetic energy is the
joule, while the English unit of kinetic energy is the foot-pound.

Reference : https://en.wikipedia.org/wiki/Kinetic_energy
"""

from math import sqrt

from scipy.constants import c  # speed of light in vacuum (299792458 m/s)


def relativistic_kinetic_energy(mass: float, velocity: float) -> float:
    """
    Calculate relativistic kinetic energy.
    mass --- kg
    velocity ---- m/s
    K.E ---- j

    >>> relativistic_kinetic_energy(10,10)
    598.6912157608277
    >>> relativistic_kinetic_energy(40,200000)
    800000266962.5057
    >>> relativistic_kinetic_energy(50,100000)
    250000021062.11475
    >>> relativistic_kinetic_energy(0,0)
    0.0
    >>> relativistic_kinetic_energy(100,0)
    0.0

    """

    if (mass < 0 ):
        raise ValueError("The mass of a body cannot be negative")
    else:
        gamma = 1/sqrt(1 - (velocity**2 / c**2))
        return (gamma-1) * mass * c**2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
