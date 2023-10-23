"""
Title : Computing the time period of a simple pendulum

A simple pendulum is a mechanical arrangement that demonstrates
periodic motion. The simple pendulum comprises of a small bob of mass 'm'
suspended by a thin string secured to a platform at its upper end of
length L.

The simple pendulum is a mechanical system that sways or moves in an
oscillatory motion. This motion occurs in a vertical plane and is mainly
driven by gravitational force. Interestingly, the bob that is suspended at
the end of a thread is very light; somewhat, we can say it is even
massless. The period of a simple pendulum can be made extended by
increasing the length string while taking the measurements from the point
of suspension to the middle of the bob. However, it should be noted that if
the mass of the bob is changed, the period will remain unchanged. The
period is influenced mainly by the position of the pendulum in relation to
Earth, as the strength of the gravitational field is not uniform everywhere.

The Time Period of a simple pendulum is given by :

T = 2 * π * (l/g)^0.5

where :

T = Time period of the simple pendulum (in s)
π = Mathematical constant (value taken : 3.14159)
l = length of string from which the bob is hanging (in m)
g = Acceleration due to gravity (value taken : 9.8 m/s^2)

Reference : https://byjus.com/jee/simple-pendulum/
"""
from scipy.constants import g

def time_period_simple_pendulum(length: float) -> float:
    """
    >>> time_period_simple_pendulum(1.23)
    2.2252136710666166
    >>> time_period_simple_pendulum(2.37)
    3.088825235169592
    >>> time_period_simple_pendulum(5.63)
    4.760727912429414
    >>> time_period_simple_pendulum(-12)
    Traceback (most recent call last):
        ...
    ValueError: The length should be non-negative
    >>> time_period_simple_pendulum(0)
    0.0
    """
    if length < 0:
        raise ValueError("The length should be non-negative")
    return (2 * 3.14159) * (length / g) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
