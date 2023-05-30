import cmath
import math


def apparent_power(
    voltage: float, current: float, voltage_angle: float, current_angle: float
) -> complex:
    """
    Calculate the apparent power in a single-phase AC circuit.

    Reference: https://en.wikipedia.org/wiki/AC_power#Apparent_power

    >>> apparent_power(100, 5, 0, 0)
    (500+0j)
    >>> apparent_power(100, 5, 90, 0)
    (3.061616997868383e-14+500j)
    >>> apparent_power(100, 5, -45, -60)
    (-129.40952255126027-482.9629131445341j)
    >>> apparent_power(200, 10, -30, -90)
    (-999.9999999999998-1732.0508075688776j)
    """
    # Convert angles from degrees to radians
    voltage_angle_rad = math.radians(voltage_angle)
    current_angle_rad = math.radians(current_angle)

    # Convert voltage and current to rectangular form
    voltage_rect = cmath.rect(voltage, voltage_angle_rad)
    current_rect = cmath.rect(current, current_angle_rad)

    # Calculate apparent power
    return voltage_rect * current_rect


if __name__ == "__main__":
    import doctest

    doctest.testmod()
