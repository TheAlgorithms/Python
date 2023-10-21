"""
Calculating the center of mass for a discrete system of particles,
given their positions and masses.

Description:

In physics, the center of mass of a distribution of mass in space
(sometimes referred to as the barycenter or balance point) is the
unique point at any given time where the weighted relative position
of the distributed mass sums to zero. This is the point to which a
force may be applied to cause a linear acceleration without an angular acceleration.
Calculations in mechanics are often simplified when formulated with respect to
the center of mass. It is a hypothetical point where the entire mass of an object
may be assumed to be concentrated to visualise its motion. In other words, the
center of mass is the particle equivalent of a given object for application of
Newton's laws of motion.

In the case of a system of particles P_i, i = 1, ..., n , each with mass m_i
that are located in space with coordinates r_i, i = 1, ..., n , the coordinates
R of the center of mass correspond to:

R = (Σ(mi * ri) / Σ(mi))

Reference: https://en.wikipedia.org/wiki/Center_of_mass#:~:text=The%20center%20of%20mass%20is%20the%20unique%20point%20at%20the,distribution%20of%20mass%20in%20space.

"""
from typing import NamedTuple


class Particle(NamedTuple):
    x: float
    y: float
    z: float
    mass: float


class Coord3D(NamedTuple):
    x: float
    y: float
    z: float


def center_of_mass(particles: list[Particle]) -> Coord3D:
    """
    Input Parameters
    ----------------
    particles: list(Particle):
    A list of particles where each particle is a tuple with it´s (x, y, z)
    position and it´s mass.

    Returns
    -------
    Coord3D:
    A tuple with the coordinates of the center of mass (Xcm, Ycm, Zcm)
    rounded to two decimal places.

    Examples
    --------

    >>> center_of_mass([(1.5, 4, 3.4, 4), (5, 6.8, 7, 8.1), (9.4, 10.1, 11.6, 12.9)])
    (6.71, 8.05, 8.8)


    >>> center_of_mass([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])
    (6.33, 7.33, 8.33)

    >>> center_of_mass([(1, 2, 3, -4), (5, 6, 7, 8), (9, 10, 11, 12)])
    Traceback (most recent call last):
        ...
    ValueError: Mass of all particles must be greater than 0

    >>> center_of_mass([(1, 2, 3, 0), (5, 6, 7, 8), (9, 10, 11, 12)])
    Traceback (most recent call last):
        ...
    ValueError: Mass of all particles must be greater than 0

    >>> center_of_mass([])
    Traceback (most recent call last):
        ...
    ValueError: No particles provided

    """
    if not particles:
        raise ValueError("No particles provided")

    for particle in particles:
        if particle.mass <= 0:
            raise ValueError("Mass of all particles must be greater than 0")

    total_mass = sum(particle.mass for particle in particles)

    center_of_mass_x = round(
        sum(particle.x * particle.mass for particle in particles) / total_mass, 2
    )
    center_of_mass_y = round(
        sum(particle.y * particle.mass for particle in particles) / total_mass, 2
    )
    center_of_mass_z = round(
        sum(particle.z * particle.mass for particle in particles) / total_mass, 2
    )
    return Coord3D(center_of_mass_x, center_of_mass_y, center_of_mass_z)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
