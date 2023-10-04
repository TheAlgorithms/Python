"""
Title : calculating the time period of a simple pendulum

A simple pendulum can be defined as a device where its point mass
is attached to a light inextensible string and suspended from a fixed
support. Equilibrium position is subjected to a restoring force when a
pendulum is displaced sideways from its resting due to its gravity
that will accelerate it back toward the equilibrium position. A simple
pendulum consists of a small metal ball (called bob) suspended by a
long thread from a rigid support by a massless and inextensible
string, such that the bob is free to swing back and forth. When the
bob from its mean position is dragged to one side and then released,
the pendulum is set to motion and the bob moves oppositely on either
side of its mean position. And when the pendulum bob is displaced it
oscillates on a plane about the vertical line through the support.

The Period (T) of a simple pendulum is the time taken for the bob to complete one
oscillation about the mean position.

Period (T) of a simple pendulum is T=2π√L/g.

where :
T = time period of the pendulum (in seconds)
L = length of the massless and inextensible string (in meters)
g = acceleration due to gravity (value taken : 9.8 m/s^2)
π = mathematical constant (value taken : 3.14159)

Reference : https://unacademy.com/content/nda/study-material/physics/what-is-the-time-period/#:~:text=The%20formula%20for%20determining%20the,full%20back%20and%20forth%20swing.
"""


def simple_pendulum_time_period(l: float) -> float:
    """
    >>> simple_pendulum_time_period(1.34)
    0.857167413819559
    >>> simple_pendulum_time_period(0.45)
    0.49672899372041895
    >>> simple_pendulum_time_period(2.6)
    1.193987904579067
    >>> simple_pendulum_time_period(3.23)
    1.3308052775536363
    >>> simple_pendulum_time_period(34)
    4.3177024674613955
    >>> simple_pendulum_time_period(-2)
    Traceback (most recent call last):
        ...
    ValueError: The length cannot be a negative number
    >>> simple_pendulum_time_period(0)
    0.0
    """
    if l < 0:
        raise ValueError("The length cannot be a negative number")
    return 2 * 3.14159 * ((l / 9 / 8) ** 0.5)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
