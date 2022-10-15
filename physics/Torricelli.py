"""
Calculates velocity of fluid from Potential Gravitational Energy

Equation for finding velocity
V = sqrt(2 * gravity * Δy)

Source:
- https://en.wikipedia.org/wiki/Archimedes%27_principle
"""


# Acceleration Constant on Earth (unit m/s^2)
g = 9.80665


def torricelli_theorem(height: float, gravity: float = g) -> float:
    """
    Args:
        height: The change in height between initial and point of flow (where,
        velocity is being measured)
        gravity: Acceleration from gravity. Gravitational force on system,
            Default is Earth Gravity
    returns:
    velocity of exiting fluid.

    >>> torricelli_theorem(height=5)
    9.90285312422637
    >>> torricelli_theorem(height=3, gravity=9.8)
    7.6681158050723255
    """
    if gravity <= 0:
        raise ValueError("Impossible Gravity")

    return (2 * height * gravity) ** 0.5


if __name__ == "__main__":
    import doctest

    # run doctest
    doctest.testmod()
