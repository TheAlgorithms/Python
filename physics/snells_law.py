"""
Snell's Law — Refraction Angle Calculation.

Calculates the angle of refraction when light passes between two
media using Snell's Law: n1 * sin(theta1) = n2 * sin(theta2).

Reference: https://en.wikipedia.org/wiki/Snell%27s_law
"""

import math


def calculate_refraction_angle(
    index_of_refraction_1: float,
    index_of_refraction_2: float,
    incident_angle_degrees: float,
) -> float:
    """
    Calculates the refraction angle of light passing from one medium to another.
    The law states that, for a given pair of media, the ratio of the sines
    of angle of incidence and angle of refraction s equal to the refractive
    index of the second medium with regard to the first which is equal to the
    ratio of the refractive indices of the two media, or equivalently, to the
    ratio of the phase velocities in the two media.


    Formula: n1 * sin(theta1) = n2 * sin(theta2)
    or     : (sin(theta1) / sin(theta2)) = (n2 / n1)
    Where:
        n1 = refractive index of the first medium
        n2 = refractive index of the second medium
        theta1 = angle of incidence
        theta2 = angle of refraction

    Note: Total Internal Reflection (TIR) occurs when light travels from a
    denser medium to a rarer medium and the incident angle exceeds the
    critical angle, making refraction impossible.

    Sources:
        - https://en.wikipedia.org/wiki/Snell%27s_law

    -----------------------------------------------------------------------------

    >>> calculate_refraction_angle(1.0, 1.33, 60.0)
    40.63
    >>> calculate_refraction_angle(2.0, 1.0, 30.0)
    90.0
    >>> calculate_refraction_angle(1.33, 1.0, 60.0)
    Traceback (most recent call last):
        ...
    ValueError: Invalid physical inputs: ratio cannot be outside [-1, 1].
    >>> calculate_refraction_angle(-1.33, 1.0, 60.0)
    Traceback (most recent call last):
        ...
    ValueError: Invalid physical inputs: ratio cannot be outside [-1, 1].
    >>>
    """

    incident_angle_radians = math.radians(incident_angle_degrees)
    refraction_sine = (index_of_refraction_1 / index_of_refraction_2) * math.sin(
        incident_angle_radians
    )

    # If the sine value is approximately 1.0 or -1.0, it's at the critical angle
    # We use math.isclose to account for floating-point precision errors
    if math.isclose(refraction_sine, 1.0):
        return 90.0
    if math.isclose(refraction_sine, -1.0):
        return -90.0

    if not -1 <= refraction_sine <= 1:
        raise ValueError("Invalid physical inputs: ratio cannot be outside [-1, 1].")

    refraction_angle = round(math.degrees(math.asin(refraction_sine)), 2)
    return refraction_angle
