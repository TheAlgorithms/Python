from scipy.constants import g

"""
Finding the gravitational potential energy of an object with reference
to the earth,by taking its mass and height above the ground as input


Description : Gravitational energy or gravitational potential energy
is the potential energy a massive object has in relation to another
massive object due to gravity. It is the potential energy associated
with the gravitational field, which is released (converted into
kinetic energy) when the objects fall towards each other.
Gravitational potential energy increases when two objects
are brought further apart.

For two pairwise interacting point particles, the gravitational
potential energy U is given by
U=-GMm/R
where M and m are the masses of the two particles, R is the distance
between them, and G is the gravitational constant.
Close to the Earth's surface, the gravitational field is approximately
constant, and the gravitational potential energy of an object reduces to
U=mgh
where m is the object's mass, g=GM/R² is the gravity of Earth, and h is
the height of the object's center of mass above a chosen reference level.

Reference : "https://en.m.wikipedia.org/wiki/Gravitational_energy"
"""


def potential_energy(mass: float, height: float) -> float:
    # function will accept mass and height as parameters and return potential energy
    """
    >>> potential_energy(10,10)
    980.665
    >>> potential_energy(0,5)
    0.0
    >>> potential_energy(8,0)
    0.0
    >>> potential_energy(10,5)
    490.3325
    >>> potential_energy(0,0)
    0.0
    >>> potential_energy(2,8)
    156.9064
    >>> potential_energy(20,100)
    19613.3
    """
    if mass < 0:
        # handling of negative values of mass
        raise ValueError("The mass of a body cannot be negative")
    if height < 0:
        # handling of negative values of height
        raise ValueError("The height above the ground cannot be negative")
    return mass * g * height


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="potential_energy")
