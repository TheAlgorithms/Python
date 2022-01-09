def get_1s_count(number: int) -> int:
    """
    Count the number of set bits in a 32 bit integer using Brian Kernighan's way.
    Ref - http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan
    >>> get_1s_count(25)
    3
    >>> get_1s_count(37)
    3
    >>> get_1s_count(21)
    3
    >>> get_1s_count(58)
    4
    >>> get_1s_count(0)
    0
    >>> get_1s_count(256)
    1
    >>> get_1s_count(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must be positive
    >>> get_1s_count(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be an 'int' type
    """
    if number < 0:
        raise ValueError("the value of input must be positive")
    elif isinstance(number, float):
        raise TypeError("Input value must be an 'int' type")
    count = 0
    while number:
        # This way we arrive at next set bit (next 1) instead of looping
        # through each bit and checking for 1s hence the
        # loop won't run 32 times it will only run the number of `1` times
        number &= number - 1
        count += 1
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
