def get_set_bits_count(number: int) -> int:
    """
    Count the number of set bits in a 32 bit integer
    >>> get_set_bits_count(25)
    3
    >>> get_set_bits_count(37)
    3
    >>> get_set_bits_count(21)
    3
    >>> get_set_bits_count(58)
    4
    >>> get_set_bits_count(0)
    0
    >>> get_set_bits_count(256)
    1
    >>> get_set_bits_count(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must be positive
    """
    if number < 0:
        raise ValueError("the value of input must be positive")
    result = 0
    while number:
        if number % 2 == 1:
            result += 1
        number = number >> 1
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
