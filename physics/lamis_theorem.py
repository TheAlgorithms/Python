"""
Title : Finding the value of an unknown force/tension in a string, or an angle at which
the force will be pointed at from the center in a tri-directional classic Lami's
arrangement.

Description : In physics, Lami's theorem is an equation relating the magnitudes of
three coplanar, concurrent and non-collinear vectors, which keeps an object in static
equilibrium, with the angles directly opposite to the corresponding vectors.

The equation for the theorem:
(A/sin(a)) = (B/sin(b)) = (C/sin(c));
A, B, C: Non-linear, coplanar vectors/forces (concurrent)
a, b, c: The angles present opposite to the vectors A, B, C respectively

Approach:
By the nature of the equality, we only need to know only 4 values. 2 from one fraction
(For example, C and c so that we can find C/sin(c)), and 1 from the other fractions (
Say, B, and a to find sin(a)). We then can evaluate the unknown 2 values.
We will assume we get C and c as parameters, then we will check for the missing values and
find them one by one.

Source :
- https://en.wikipedia.org/wiki/Lami%27s_theorem
"""

import math
from math import asin, sin


def lamis_theorem(force_c: float, angle_c: float, forces: list, angles: list) -> list:
    """
    Input Parameters:
    ---------------------
    C and c are given, so we can find C/sin(c).

    Forces is a list of 2 forces which may have 0, 1 or 2 unknown values in it
    (represented by 0)

    angles is a list of 2 angles that are opposite to the forces present in the
    Forces list (order matters). Can have 0, 1 or 2 unknowns (represented by 0).

    Returns
    -----------------------
    result: List of key value pairs containing A, B, C and a, b, c

    Returns the value of the entire set of Forces and angles given sufficient
    number of values of forces and/angles have been provided
    >>> lamis_theorem(C = 100, c = 90, Forces = [0, 0], angles = [150, 120])
    [[49.99999999999999, 150], [86.60254037844388, 120], [100, 90]]

    >>> lamis_theorem(C = 110, c = 90, Forces = [0, 0], angles = [200, 70])
    [[-37.622215765823555, 200], [103.36618828644991, 70], [110, 90]]

    >>> lamis_theorem(C = 100, c = 90, Forces = [20, 0], angles = [0, 70])
    [[20, 11.536959032815489], [93.96926207859083, 70], [100, 90]]

    >>> lamis_theorem(C = 100, c = 90, Forces = [0, 0], angles = [0, 70])
    Traceback (most recent call last):
        ...
    ValueError: Only 2 arguments must be 0

    >>> lamis_theorem(C = 100, c = 90, Forces = [-100, 0], angles = [200, 70])
    Traceback (most recent call last):
        ...
    ValueError: Forces cannot be negative
    """

    fractional_value = force_c / sin(
        math.radians(angle_c)
    )  # Will be used to find other values by solving

    # Performing checks for value integrity
    if (forces[0], forces[1], angles[0], angles[1]).count(0) > 2:
        raise ValueError("Only 2 arguments must be 0")
    if forces[0] == 0 and angles[0] == 0:
        raise ValueError("Both vector and its opposite angle cannot be 0")
    if forces[1] == 0 and angles[1] == 0:
        raise ValueError("Both vector and opposite angle cannot be 0")
    if forces[0] < 0 or forces[1] < 0:
        raise ValueError("Forces cannot be negative")

    # Calculation part
    if forces[0] == 0:
        #Have to convert the degree value into radians
        forces[0] = fractional_value * sin(math.radians(angles[0]))
    if forces[1] == 0:
        forces[1] = fractional_value * sin(math.radians(angles[1]))
    if angles[0] == 0:
        #Solving using usual equation solving techniques
        angles[0] = math.degrees(asin(forces[0] / fractional_value))
    if angles[1] == 0:
        angles[1] = math.degrees(asin(forces[1] / fractional_value))

    result = []
    result.append([forces[0], angles[0]])
    result.append([forces[1], angles[1]])
    result.append([force_c, angle_c])

    return result


# Run doctest
if __name__ == "__main__":
    import doctest

    doctest.testmod()
