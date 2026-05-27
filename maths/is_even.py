def is_even(n: int) -> bool:
    """
    Check whether a number is even.

    An even number is an integer divisible by 2.
    Reference: https://en.wikipedia.org/wiki/Parity_(mathematics)

    >>> is_even(10)
    True
    >>> is_even(7)
    False

    :param n: Integer number
    :return: True if even, False otherwise
    """
    return n % 2 == 0
