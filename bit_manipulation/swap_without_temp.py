"""
Swap two integers without using a temporary variable or arithmetic operators.

This implementation relies on the properties of the bitwise XOR (exclusive OR)
operator. XOR-ing two values twice with the same operand restores the original
value, which makes it possible to exchange two integers without allocating an
extra variable or performing arithmetic.

https://en.wikipedia.org/wiki/Bitwise_operation#XOR
"""


def swap_without_temp(first: int, second: int) -> tuple[int, int]:
    """Return ``second`` and ``first`` without using a temporary variable.

    >>> swap_without_temp(3, 7)
    (7, 3)
    >>> swap_without_temp(-5, 12)
    (12, -5)
    >>> swap_without_temp(0, 0)
    (0, 0)
    >>> swap_without_temp(2**31 - 1, -2**31)
    (-2147483648, 2147483647)
    >>> swap_without_temp(True, 1)
    Traceback (most recent call last):
        ...
    TypeError: swap_without_temp expects two integers
    >>> swap_without_temp(1.5, 2)
    Traceback (most recent call last):
        ...
    TypeError: swap_without_temp expects two integers
    """

    if type(first) is not int or type(second) is not int:
        raise TypeError("swap_without_temp expects two integers")

    if first == second:
        return first, second

    first ^= second
    second ^= first
    first ^= second
    return first, second


if __name__ == "__main__":
    import doctest

    doctest.testmod()
