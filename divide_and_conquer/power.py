def actual_power(g: int, b: int):
    """
    Function using divide and conquer to calculate a^b.
    It only works for integer a,b.
    """
    if b == 0:
        return 1
    if (b % 2) == 0:
        return actual_power(g, int(b / 2)) * actual_power(g, int(b / 2))
    else:
        return g * actual_power(g, int(b / 2)) * actual_power(g, int(b / 2))


def power(a: int, b: int) -> float:
    """
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
