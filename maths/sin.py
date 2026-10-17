"""
Calculate the sine function, approximated by Taylor series expansion

Formula: sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
  Where: x = angle in randians.

Source:
    https://www.homeschoolmath.net/teaching/sine_calculator.php
    Wikipedia reference: https://en.wikipedia.org/wiki/Taylor_series
"""

from math import radians


def sin(angle_in_degrees: float, rounded_values_count: int = 10) -> float:
    """
    Calculate the sine function, approximated by Taylor series expansion

    For trigonometry calculations the expected precision is about 10 digits.
    Python has floating precision of about 15 digits.
    Using operation ** and / iteratively, precision is lost quickly
    This method rounds to 10 digits by default, to be safe.

    >>> sin(0.0)
    0.0
    >>> sin(90.0)
    1.0
    >>> sin(180.0)
    0.0
    >>> sin(270.0)
    -1.0
    >>> sin(0.68)
    0.0118679603
    >>> sin(1.97)
    0.0343762121
    >>> sin(64.0)
    0.8987940463
    >>> sin(9999.0)
    -0.9876883406
    >>> sin(-689.0)
    0.5150380749
    >>> sin(89.7)
    0.9999862922
    """

    # Simplify the angle to be between 360 and -360 degrees.
    angle_in_degrees %= 360.0

    angle_in_radians = radians(angle_in_degrees)

    result = angle_in_radians
    power_x = 3
    fac = -6  # - factorial(power_x)
    result_old = 2  # any impossible sine result will do

    # Keep adding the next Tayler term until the result stops changing.
    while True:
        result += angle_in_radians**power_x / fac
        power_x += 2  # Increased by 2 for every term.
        fac *= -power_x * (power_x - 1)
        if result == result_old:
            break
        result_old = result

    return round(result, rounded_values_count)


if __name__ == "__main__":
    __import__("doctest").testmod()
