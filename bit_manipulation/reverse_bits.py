def get_reverse_bit_string(number: int) -> str:
    """
    Return the reverse bit string of a 32 bit integer

    >>> get_reverse_bit_string(9)
    '10010000000000000000000000000000'
    >>> get_reverse_bit_string(43)
    '11010100000000000000000000000000'
    >>> get_reverse_bit_string(2873)
    '10011100110100000000000000000000'
    >>> get_reverse_bit_string(2550136832)
    '00000000000000000000000000011001'
    >>> get_reverse_bit_string("this is not a number")
    Traceback (most recent call last):
        ...
    TypeError: operation can not be conducted on an object of type str
    """
    if not isinstance(number, int):
        msg = (
            "operation can not be conducted on an object of type "
            f"{type(number).__name__}"
        )
        raise TypeError(msg)
    bit_string = ""
    for _ in range(32):
        bit_string += str(number % 2)
        number >>= 1
    return bit_string


def reverse_bit(number: int) -> int:
    """
    Take in a 32 bit integer, reverse its bits, return a 32 bit integer result

    >>> reverse_bit(25)
    2550136832
    >>> reverse_bit(37)
    2751463424
    >>> reverse_bit(21)
    2818572288
    >>> reverse_bit(58)
    1543503872
    >>> reverse_bit(0)
    0
    >>> reverse_bit(256)
    8388608
    >>> reverse_bit(2550136832)
    25
    >>> reverse_bit(-1)
    Traceback (most recent call last):
        ...
    ValueError: The value of input must be non-negative

    >>> reverse_bit(1.1)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be an 'int' type

    >>> reverse_bit("0")
    Traceback (most recent call last):
        ...
    TypeError: Input value must be an 'int' type
    """
    if not isinstance(number, int):
        raise TypeError("Input value must be an 'int' type")
    if number < 0:
        raise ValueError("The value of input must be non-negative")

    result = 0
    # iterator over [0 to 31], since we are dealing with a 32 bit integer
    for _ in range(32):
        # left shift the bits by unity
        result <<= 1
        # get the end bit
        end_bit = number & 1
        # right shift the bits by unity
        number >>= 1
        # add that bit to our answer
        result |= end_bit
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
