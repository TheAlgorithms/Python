"""
----------------------------------------------------------------------------------------
An electric field (E) is a physical field that surrounds electrically charged particles.
In classical electromagnetism, the electric field of a single charge describes their
capacity to exert attractive or repulsive forces on another charged object.

The electric field is a vector field, which means it has both a magnitude and
a direction.

The direction of the electric field is the direction of the force that a positive test
charge would experience if placed in the field.

The magnitude of the electric field of an electrically charged point object is given by
the formula:

-------------------
| E = k * Q / r^2 |
-------------------

k --> Coulomb's constant and is equal to 1/(4π*ε0)
Q --> charge of the charged object (C)
r --> distance between the center of the charged object and the electric field
measurement point (m)

Reference: https://en.wikipedia.org/wiki/Electric_field
"""

def __check_args(charge: float, distance: float) -> None:
    """
    Check that the arguments are valid
    >>> __check_args(50, -10)
    Traceback (most recent call last):
        ...
    ValueError: The distance is always a positive number.
    >>> __check_args("50", 10)
    Traceback (most recent call last):
        ...
    TypeError: Invalid charge. Should be an integer or float.
    >>> __check_args(50, "10")
    Traceback (most recent call last):
        ...
    TypeError: Invalid distance. Should be an integer or float.
    """

    # Ensure valid instance
    if not isinstance(charge, (int, float)):
        raise TypeError("Invalid charge. Should be an integer or float.")

    if not isinstance(distance, (int, float)):
        raise TypeError("Invalid distance. Should be an integer or float.")

    # Ensure valid distance
    if distance <= 0:
        raise ValueError("The distance is always a positive number.")



def __eletric_field_direction(magnitude_of_the_electric_field: float) -> float:
    """
    Determine the direction of the electric field based on the magnitude.
    >>> __eletric_field_direction(-15)
    'Since the charge is negative, the electric field is pointing towards the charge.'
    >>> __eletric_field_direction(20)
    'Since the charge is positive, the electric field is pointing away from the charge.'
    >>> __eletric_field_direction(0)
    'The electric field is zero.'
    """
    if magnitude_of_the_electric_field < 0:
        return "Since the charge is negative, the electric field is pointing towards the charge."
    elif magnitude_of_the_electric_field > 0:
        return "Since the charge is positive, the electric field is pointing away from the charge."
    else:
        return "The electric field is zero."


def electric_field(charge: float, distance: float) -> float:
    """
    Calculate the magnitude of the electric field of an electrically charged
    point object.

    >>> electric_field(20, 15)
    Since the charge is positive, the electric field is pointing away from the charge.
    798893492.65
    >>> electric_field(15, 5)
    Since the charge is positive, the electric field is pointing away from the charge.
    5392531075.38
    >>> electric_field(-20, 15)
    Since the charge is negative, the electric field is pointing towards the charge.
    -798893492.65
    >>> electric_field(0, 1)
    The electric field is zero.
    0.0
    """
    __check_args(charge, distance)

    coulombs_constant = 8.9875517923e9  # in N·m²/C²
    mag_eletric_field = (coulombs_constant * charge) / (distance**2)

    print(__eletric_field_direction(mag_eletric_field))

    return round(mag_eletric_field, 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
