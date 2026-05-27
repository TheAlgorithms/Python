def lucas_number(input_index: int) -> int:
    """
    Returns the n-th Lucas number using an iterative approach.
    The Lucas numbers are an integer sequence where each term is the sum of the
    two preceding terms, starting with 2 and 1.

    Reference: https://en.wikipedia.org/wiki/Lucas_number

    >>> lucas_number(0)
    2
    >>> lucas_number(1)
    1
    >>> lucas_number(5)
    11
    >>> lucas_number(10)
    123
    >>> lucas_number(-3)
    Traceback (most recent call last):
        ...
    ValueError: input_index must be a non-negative integer.
    """
    if input_index < 0:
        raise ValueError("input_index must be a non-negative integer.")

    if input_index == 0:
        return 2
    if input_index == 1:
        return 1

    a, b = 2, 1
    for _ in range(2, input_index + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
