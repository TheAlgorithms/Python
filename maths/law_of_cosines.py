# url: https://en.wikipedia.org/wiki/Law_of_cosines


import math


def law_of_cosines(side_a: float, side_b: float, angle_c: float) -> float:
    """
    Calculate the length of the third side of a triangle using the Law of Cosines.

    :param side_a: The length of side 'a' (float).
    :param side_b: The length of side 'b' (float).
    :param angle_c: The measure of angle 'C' in degrees (float).

    :return: The length of side 'c' (float).

    >>> round(law_of_cosines(5, 7, 60), 12)  # Rounding to 12 decimal places
    5.830951894845
    >>> round(law_of_cosines(3, 4, 90), 12)
    5.0
    """
    # Convert the angle from degrees to radians
    angle_c_radians = math.radians(angle_c)

    # Use the Law of Cosines formula
    c_squared = (
        side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_c_radians)
    )

    # Take the square root to find the length of side 'c'
    side_c = math.sqrt(c_squared)

    return side_c


if __name__ == "__main__":
    import doctest

    doctest.testmod()
