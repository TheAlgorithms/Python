"""
Title : Computing the time period of a simple pendulum

The simple pendulum is a mechanical system that sways or moves in an
oscillatory motion. The simple pendulum comprises of a small bob of
mass m suspended by a thin string of length L and secured to a platform
at its upper end. Its motion occurs in a vertical plane and is mainly
driven by gravitational force. The period of the pendulum depends on the
length of the string and the amplitude (the maximum angle) of oscillation.
However, the effect of the amplitude can be ignored if the amplitude is
small. It should be noted that the period does not depend on the mass of
the bob.

For small amplitudes, the period of a simple pendulum is given by the
following approximation:
T ≈ 2π * √(L / g)

where:
L = length of string from which the bob is hanging (in m)
g = acceleration due to gravity (approx 9.8 m/s²)

Reference : https://byjus.com/jee/simple-pendulum/
"""

from math import pi

from scipy.constants import g


def period_of_pendulum(length: float) -> float:
    """
    >>> period_of_pendulum(1.23)
    2.2252155506257845
    >>> period_of_pendulum(2.37)
    3.0888278441908574
    >>> period_of_pendulum(5.63)
    4.76073193364765
    >>> period_of_pendulum(-12)
    Traceback (most recent call last):
        ...
    ValueError: The length should be non-negative
    >>> period_of_pendulum(0)
    0.0
    """
    if length < 0:
        raise ValueError("The length should be non-negative")
    return 2 * pi * (length / g) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
