"""
Calculate sin function.

It's not a perfect function so I am rounding the result to 10 decimal places by default.

Formula: sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
Where: x = angle in randians.

Source:
    https://www.homeschoolmath.net/teaching/sine_calculator.php

"""

from math import factorial, radians


def sin(
    angle_in_degrees: float, accuracy: int = 18, rounded_values_count: int = 10
) -> float:
    """
    Implement sin function.

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
    angle_in_degrees = angle_in_degrees - ((angle_in_degrees // 360.0) * 360.0)

    # Converting from degrees to radians
    angle_in_radians = radians(angle_in_degrees)

    result = angle_in_radians
    a = 3
    b = -1

    for _ in range(accuracy):
        result += (b * (angle_in_radians**a)) / factorial(a)

        b = -b  # One positive term and the next will be negative and so on...
        a += 2  # Increased by 2 for every term.

    return round(result, rounded_values_count)


if __name__ == "__main__":
    __import__("doctest").testmod()
