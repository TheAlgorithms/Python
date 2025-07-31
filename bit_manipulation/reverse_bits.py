def get_reverse_bit_string(number: int) -> str:
    """
    Take in an 32 bit integer, reverse its bits,
    return a string of reversed bits

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
        msg = (
            "operation can not be conducted on a object of type "
            f"{type(number).__name__}"
        )
        raise TypeError(msg)
    bit_string = ""
    for _ in range(32):
        bit_string += str(number % 2)
        number = number >> 1
    return bit_string


def get_reverse_bit_int(number: int) -> int:
    """
    Take in an 32 bit integer, reverse its bits,
    return a 32 bit integer of reversed bits

    result of a get_reverse_bit and operation on the integer provided.

    >>> get_reverse_bit_int(25)
    2550136832
    >>> get_reverse_bit_int(37)
    2751463424
    >>> get_reverse_bit_int(21)
    2818572288
    >>> get_reverse_bit_int(58)
    1543503872
    >>> get_reverse_bit_int(0)
    0
    >>> get_reverse_bit_int(256)
    8388608
    >>> get_reverse_bit_int(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must be positive

    >>> get_reverse_bit_int(1.1)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type

    >>> get_reverse_bit_int("0")
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
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
