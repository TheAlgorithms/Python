"""
Title : Calculate Light Aberration (astronomy)

Description :
    The below algorithm calculates astronomical light aberration as obtained
    using Special Relativity.

"""

from math import atan, sqrt, tan


def get_aberration_angle(angle_rest: float, velocity_over_c: float) -> float:
    """
    This method calculates astronomical light aberration.
    The angle at rest 'angle_rest' is given in radians [rad]
    and is in the range (-pi, pi).
    The relative velocity of observer w.r.t. to the light emitting object is
    expressed by 'velocity_over_c' that is given as ratio for velocity
    w.r.t. the speed of light c and is in the range (0, 1).

    https://en.wikipedia.org/wiki/Aberration_(astronomy)

    tan(phi/2) = sqrt((1 - v/c)/(1 + v/c)) * tan(theta/2)

    Where v is the relative velocity, phi is the observed angle with respect to the
    velocity vector (affected by light aberration), and theta is the angle observed
    angle in the limit of veclocity being equal to 0.

    Examples:
    >>> get_aberration_angle(0.2, 0.1)
    0.18102
    >>> get_aberration_angle(0.2, 0)
    0.2
    >>> get_aberration_angle(0, 0.2)
    0.0
    >>> get_aberration_angle(-1.5707963267948966, 0.7)
    -0.7954
    """

    factor = sqrt((1 - velocity_over_c) / (1 + velocity_over_c))
    angle_ab = 2 * atan(factor * tan(angle_rest / 2))

    return round(angle_ab, 5)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
