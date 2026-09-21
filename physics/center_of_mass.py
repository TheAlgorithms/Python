"""
Calculating the center of mass for a discrete system of particles, given their
positions and masses.

Description:

In physics, the center of mass of a distribution of mass in space (sometimes referred
to as the barycenter or balance point) is the unique point at any given time where the
weighted relative position of the distributed mass sums to zero. This is the point to
which a force may be applied to cause a linear acceleration without an angular
acceleration.

Calculations in mechanics are often simplified when formulated with respect to the
center of mass. It is a hypothetical point where the entire mass of an object may be
assumed to be concentrated to visualize its motion. In other words, the center of mass
is the particle equivalent of a given object for the application of Newton's laws of
motion.

In the case of a system of particles P_i, i = 1, ..., n , each with mass m_i that are
located in space with coordinates r_i, i = 1, ..., n , the coordinates R of the center
of mass corresponds to:

R = (Σ(mi * ri) / Σ(mi))

Reference: https://en.wikipedia.org/wiki/Center_of_mass
"""

from collections import namedtuple

Particle = namedtuple("Particle", "x y z mass")  # noqa: PYI024
Coord3D = namedtuple("Coord3D", "x y z")  # noqa: PYI024


def center_of_mass(particles: list[Particle]) -> Coord3D:
    """
    Input Parameters
    ----------------
    particles: list(Particle):
    A list of particles where each particle is a tuple with it's (x, y, z) position and
    it's mass.

    Returns
    -------
    Coord3D:
    A tuple with the coordinates of the center of mass (Xcm, Ycm, Zcm) rounded to two
    decimal places.

    Examples
    --------
    >>> center_of_mass([
    ...     Particle(1.5, 4, 3.4, 4),
    ...     Particle(5, 6.8, 7, 8.1),
    ...     Particle(9.4, 10.1, 11.6, 12)
    ... ])
    Coord3D(x=6.61, y=7.98, z=8.69)

    >>> center_of_mass([
    ...     Particle(1, 2, 3, 4),
    ...     Particle(5, 6, 7, 8),
    ...     Particle(9, 10, 11, 12)
    ... ])
    Coord3D(x=6.33, y=7.33, z=8.33)

    >>> center_of_mass([
    ...     Particle(1, 2, 3, -4),
    ...     Particle(5, 6, 7, 8),
    ...     Particle(9, 10, 11, 12)
    ... ])
    Traceback (most recent call last):
        ...
    ValueError: Mass of all particles must be greater than 0

    >>> center_of_mass([
    ...     Particle(1, 2, 3, 0),
    ...     Particle(5, 6, 7, 8),
    ...     Particle(9, 10, 11, 12)
    ... ])
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

    if any(particle.mass <= 0 for particle in particles):
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
