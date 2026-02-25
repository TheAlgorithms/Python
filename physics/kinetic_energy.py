"""
Compute the kinetic energy of an object given its mass and velocity.

Formula (classical mechanics):
    KE = ½ · m · v²

Reference:
https://en.wikipedia.org/wiki/Kinetic_energy
"""


def kinetic_energy(mass: float, velocity: float) -> float:
    """
    Calculate the kinetic energy of a non-rotating object.

    Parameters
    ----------
    mass : float
        Mass of the object (must be non-negative)
    velocity : float
        Velocity of the object

    Returns
    -------
    float
        Kinetic energy in joules

    Raises
    ------
    ValueError
        If mass is negative

    Examples
    --------
    >>> kinetic_energy(10, 10)
    500.0
    >>> kinetic_energy(0, 10)
    0.0
    >>> kinetic_energy(10, 0)
    0.0
    >>> kinetic_energy(20, -20)
    4000.0
    >>> kinetic_energy(0, 0)
    0.0
    >>> kinetic_energy(2, 2)
    4.0
    >>> kinetic_energy(100, 100)
    500000.0
    """
    if mass < 0:
        raise ValueError("Mass must be non-negative")

    return 0.5 * mass * velocity ** 2


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
