def count_one_bits(number: int) -> int:
    """
    Take in an 32 bit integer, count the number of one bits,
    return the number of one bits
    result of a count_one_bits and operation on the integer provided.
    >>> count_one_bits(25)
    3
    >>> count_one_bits(37)
    3
    >>> count_one_bits(21)
    3
    >>> count_one_bits(58)
    4
    >>> count_one_bits(0)
    0
    >>> count_one_bits(256)
    1
    >>> count_one_bits(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must be positive
    >>> count_one_bits(1.1)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type
    >>> count_one_bits("0")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if number < 0:
        raise ValueError("the value of input must be positive")
    elif isinstance(number, float):
        raise TypeError("Input value must be a 'int' type")
    elif isinstance(number, str):
        raise TypeError("'<' not supported between instances of 'str' and 'int'")
    result = 0
    while number:
        if number % 2 == 1:
            result += 1
        number = number >> 1
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
