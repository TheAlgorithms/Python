"""
Checks if a system of forces is in static equilibrium.

python/black : true
flake8 : passed
mypy : passed
"""

from typing import List

from numpy import array, cos, cross, radians, sin  # type: ignore


def polar_force(
    magnitude: float, angle: float, radian_mode: bool = False
) -> List[float]:
    """
    Resolves force along rectangular components.
    (force, angle) => (force_x, force_y)
    >>> polar_force(10, 45)
    [7.0710678118654755, 7.071067811865475]
    >>> polar_force(10, 3.14, radian_mode=True)
    [-9.999987317275394, 0.01592652916486828]
    """
    if radian_mode:
        return [magnitude * cos(angle), magnitude * sin(angle)]
    return [magnitude * cos(radians(angle)), magnitude * sin(radians(angle))]


def in_static_equilibrium(
    forces: array, location: array, eps: float = 10 ** -1
) -> bool:
    """
    Check if a system is in equilibrium.
    It takes two numpy.array objects.
    forces ==>  [
                        [force1_x, force1_y],
                        [force2_x, force2_y],
                        ....]
    location ==>  [
                        [x1, y1],
                        [x2, y2],
                        ....]
    >>> force = array([[1, 1], [-1, 2]])
    >>> location = array([[1, 0], [10, 0]])
    >>> in_static_equilibrium(force, location)
    False
    """
    # summation of moments is zero
    moments: array = cross(location, forces)
    sum_moments: float = sum(moments)
    return abs(sum_moments) < eps


if __name__ == "__main__":
    # Test to check if it works
    forces = array(
        [polar_force(718.4, 180 - 30), polar_force(879.54, 45), polar_force(100, -90)]
    )

    location = array([[0, 0], [0, 0], [0, 0]])

    assert in_static_equilibrium(forces, location)

    # Problem 1 in image_data/2D_problems.jpg
    forces = array(
        [
            polar_force(30 * 9.81, 15),
            polar_force(215, 180 - 45),
            polar_force(264, 90 - 30),
        ]
    )

    location = array([[0, 0], [0, 0], [0, 0]])

    assert in_static_equilibrium(forces, location)

    # Problem in image_data/2D_problems_1.jpg
    forces = array([[0, -2000], [0, -1200], [0, 15600], [0, -12400]])

    location = array([[0, 0], [6, 0], [10, 0], [12, 0]])

    assert in_static_equilibrium(forces, location)

    import doctest

    doctest.testmod()
