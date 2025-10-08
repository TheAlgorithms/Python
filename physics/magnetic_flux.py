"""
________________________________________________________________________________________
Magnetic flux (Φ) is a scalar quantity that measures the number of magnetic field
lines (B) that pass through a closed area (A). Furthermore, the magnetic flux depends
on the angle formed between the magnetic field and the normal line (N) in area A.
Check out the formula used to calculate this flux:
 ------------------
 | Φ = B.A.cos(θ) |
 ------------------

Φ = magnetic flux (weber (Wb) or tesla square meter (T.m²))
B = magnetic field (tesla (T))
A = area (square meter (m²))
θ = angle between magnetic field and normal line (degrees (°))

(Description adapted from https://en.wikipedia.org/wiki/Magnetic_flux )
"""

from math import cos, radians


def __check_args(magnetic_field: float, area: float, angle: float) -> None:
    """
    Check that the arguments are valid
    >>> __check_args(10, 10, -10)
    Traceback (most recent call last):
        ...
    ValueError: Invalid angle. Range is 0-180 degrees.
    >>> __check_args(10, -10, 10)
    Traceback (most recent call last):
        ...
    ValueError: Invalid area. Should be a positive number.
    >>> __check_args(-10, 10, 10)
    Traceback (most recent call last):
        ...
    ValueError: Invalid magnetic field. Should be a positive number.
    """

    # Ensure valid instance
    if not isinstance(magnetic_field, (int, float)):
        raise TypeError("Invalid magnetic field. Should be an integer or float.")

    if not isinstance(area, (int, float)):
        raise TypeError("Invalid area. Should be an integer or float.")

    if not isinstance(angle, (int, float)):
        raise TypeError("Invalid angle. Should be an integer or float.")

    # Ensure valid angle
    if angle < 0 or angle > 180:
        raise ValueError("Invalid angle. Range is 0-180 degrees.")

    # Ensure valid magnetic field
    if magnetic_field < 0:
        raise ValueError("Invalid magnetic field. Should be a positive number.")

    # Ensure valid area
    if area < 0:
        raise ValueError("Invalid area. Should be a positive number.")


def magnetic_flux(magnetic_field: float, area: float, angle: float) -> float:
    """
    >>> magnetic_flux(50.0, 2, 0.0)
    100.0
    >>> magnetic_flux(50, 2, 60.0)
    50.0
    >>> magnetic_flux(0.5, 4.0, 90.0)
    0.0
    >>> magnetic_flux(1, 2.0, 180.0)
    -2.0
    >>> magnetic_flux(-1.0, 2.0, 30.0)
    Traceback (most recent call last):
        ...
    ValueError: Invalid magnetic field. Should be a positive number.
    >>> magnetic_flux(1.0, 'a', 30.0)
    Traceback (most recent call last):
        ...
    TypeError: Invalid area. Should be an integer or float.
    >>> magnetic_flux(1.0, -2.0, 30.0)
    Traceback (most recent call last):
        ...
    ValueError: Invalid area. Should be a positive number.
    """
    __check_args(magnetic_field, area, angle)
    rad = radians(angle)
    return round(magnetic_field * area * cos(rad), 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
