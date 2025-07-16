def last_digit(n: int) -> int:
    """
    Return the last digit of a given integer.

    >>> last_digit(1234)
    4
    >>> last_digit(-98)
    8
    >>> last_digit(0)
    0
    """
    return abs(n) % 10
