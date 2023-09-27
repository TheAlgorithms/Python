"""
Coulomb's law states that the magnitude of the electrostatic force of attraction
or repulsion between two point charges is directly proportional to the product
of the magnitudes of charges and inversely proportional to the square of the
distance between them.

F = k * q1 * q2 / r^2

k is Coulomb's constant and equals 1/(4π*ε0)
q1 is charge of first body (C)
q2 is charge of second body (C)
r is distance between two charged bodies (m)

Reference: https://en.wikipedia.org/wiki/Coulomb%27s_law
"""


def coulombs_law(q1: float, q2: float, radius: float) -> float:
    """
    Calculate the electrostatic force of attraction or repulsion
    between two point charges

    >>> coulombs_law(15.5, 20, 15)
    12382849136.06
    >>> coulombs_law(1, 15, 5)
    5392531075.38
    >>> coulombs_law(20, -50, 15)
    -39944674632.44
    >>> coulombs_law(-5, -8, 10)
    3595020716.92
    >>> coulombs_law(50, 100, 50)
    17975103584.6
    """
    if radius <= 0:
        raise ValueError("The radius is always a positive non zero integer")
    return round(((8.9875517923 * 10**9) * q1 * q2) / (radius**2), 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
