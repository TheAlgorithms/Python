def actual_power(a: int, b: int):
    """
    Function using divide and conquer to calculate a^b.
    It only works for integer a,b.

    :param a: The base of the power operation, an integer.
    :param b: The exponent of the power operation, a non-negative integer.
    :return: The result of a^b.

    Examples:
    >>> actual_power(3, 2)
    9
    >>> actual_power(5, 3)
    125
    >>> actual_power(2, 5)
    32
    >>> actual_power(7, 0)
    1
    """
    if b == 0:
        return 1
    if (b % 2) == 0:
        return actual_power(a, int(b / 2)) * actual_power(a, int(b / 2))
    else:
        return a * actual_power(a, int(b / 2)) * actual_power(a, int(b / 2))


def power(a: int, b: int) -> float:
    """
    :param a: The base (integer).
    :param b: The exponent (integer).
    :return: The result of a^b, as a float for negative exponents.

    >>> power(4,6)
    4096
    >>> power(2,3)
    8
    >>> power(-2,3)
    -8
    >>> power(2,-3)
    0.125
    >>> power(-2,-3)
    -0.125
    """
    if b < 0:
        return 1 / actual_power(a, b)
    return actual_power(a, b)


if __name__ == "__main__":
    print(power(-2, -3))
