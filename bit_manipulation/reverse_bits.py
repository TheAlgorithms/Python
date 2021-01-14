def get_reverse_bit_string(bn : int) -> str:
    """    return the bit string of an interger
    """
    bit_string = ""
    for trk in range(0, 32):
        bit_string += str(bn % 2)
        bn = bn >> 1
    return bit_string


def reverse_bit(n: int) -> str:
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
    if n < 0:
        raise ValueError("the value of input must be positive")
    elif isinstance(n, float):
        raise TypeError("Input value must be a 'int' type")
    elif isinstance(n, str):
        raise TypeError("'<' not supported between instances of 'str' and 'int'")
    ans = 0
    # iterator over [1 to 32],since we are dealing with 32 bit integer
    for i in range(1, 33):
        # left shift the bits by unity
        ans = ans << 1
        # get the end bit
        k = n % 2
        # right shif the bits by unity
        n = n >> 1
        # add that bit to our ans
        ans = ans | k
    return get_reverse_bit_string(ans)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
