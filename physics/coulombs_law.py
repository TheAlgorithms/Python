"""
Description : The law states that the magnitude of the electrostatic force of attraction or repulsion between two point charges is directly proportional
to the product of the magnitudes of charges and inversely proportional to the square of the distance between them.
Coulomb studied the repulsive force between bodies having electrical charges of the same sign.

F  = k*q1*q2/ r^2

where

k is proportionality constant and equals to 1/4πε0.
q1 is charge of first body (C)
q2 is charge of second body (C)
r is distance between two charged bodies (m)
"""


def coulombs_law(q1: float, q2: float, radius: float) -> float:
    """
    >>> round(coulombs_law(15.5,20,15),2)
    12382849136.06
    >>> round(coulombs_law(1,15,5),2)
    5392531075.38
    >>> round(coulombs_law(20,-50,15),2)
    -39944674632.44
    >>> round(coulombs_law(-5,-8,10),2)
    3595020716.92
    >>> round(coulombs_law(50,100,50),2)
    17975103584.6
    """
    if radius <= 0:
        raise ValueError("The radius is always a positive non zero integer")
    return ((8.9875517923 * 10**9) * q1 * q2) / (radius**2)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
