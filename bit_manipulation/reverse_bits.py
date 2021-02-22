def get_reverse_bit_string(number: int) -> str:
    """
    return the bit string of an integer

    >>> get_reverse_bit_string(9)
    '10010000000000000000000000000000'
    >>> get_reverse_bit_string(43)
    '11010100000000000000000000000000'
    >>> get_reverse_bit_string(2873)
    '10011100110100000000000000000000'
    >>> get_reverse_bit_string("this is not a number")
    Traceback (most recent call last):
        ...
    TypeError: operation can not be conducted on a object of type str
    """
    if not isinstance(number, int):
        raise TypeError(
            "operation can not be conducted on a object of type "
            f"{type(number).__name__}"
        )
    bit_string = ""
    for _ in range(0, 32):
        bit_string += str(number % 2)
        number = number >> 1
    return bit_string


def reverse_bit(number: int) -> str:
    """
    Take in an 32 bit integer, reverse its bits,
    return a string of reverse bits

    result of a reverse_bit and operation on the integer provided.

    >>> reverse_bit(25)
    '00000000000000000000000000011001'
    >>> reverse_bit(37)
    '00000000000000000000000000100101'
    >>> reverse_bit(21)
    '00000000000000000000000000010101'
    >>> reverse_bit(58)
    '00000000000000000000000000111010'
    >>> reverse_bit(0)
    '00000000000000000000000000000000'
    >>> reverse_bit(256)
    '00000000000000000000000100000000'
    >>> reverse_bit(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must be positive

    >>> reverse_bit(1.1)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type

    >>> reverse_bit("0")
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
    # iterator over [1 to 32],since we are dealing with 32 bit integer
    for _ in range(1, 33):
        # left shift the bits by unity
        result = result << 1
        # get the end bit
        end_bit = number % 2
        # right shift the bits by unity
        number = number >> 1
        # add that bit to our ans
        result = result | end_bit
    return get_reverse_bit_string(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
