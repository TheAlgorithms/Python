def leonardo_numbers(n: int) -> int:
    """
    Return the n-th Leonardo number.

    The Leonardo numbers are a sequence of numbers given by the recurrence:
    L(n) = L(n-1) + L(n-2) + 1
    with initial values L(0) = 1 and L(1) = 1.

    Reference: https://en.wikipedia.org/wiki/Leonardo_number

    >>> leonardo_numbers(0)
    1
    >>> leonardo_numbers(1)
    1
    >>> leonardo_numbers(2)
    3
    >>> leonardo_numbers(3)
    5
    >>> leonardo_numbers(4)
    9
    >>> leonardo_numbers(20)
    21891
    >>> leonardo_numbers(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer
    >>> leonardo_numbers(1.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0 or n == 1:
        return 1

    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b + 1

    return b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
