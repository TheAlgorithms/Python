# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_xor(a: int, b: int):
    """
    Take in 2 integers, convert them to binary,
    return a binary number that is the
    result of a binary xor operation on the integers provided.

    >>> binary_xor(25, 32)
    '0b111001'
    >>> binary_xor(37, 50)
    '0b010111'
    >>> binary_xor(21, 30)
    '0b01011'
    >>> binary_xor(58, 73)
    '0b1110011'
    >>> binary_xor(0, 255)
    '0b11111111'
    >>> binary_xor(256, 256)
    '0b000000000'
    >>> binary_xor(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: the value of both input must be positive
    >>> binary_xor(0, 1.1)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> binary_xor("0", "1")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0 or b < 0:
        raise ValueError("the value of both input must be positive")
    if isinstance(a, float) or isinstance(b, float):
        raise TypeError("'float' object cannot be interpreted as an integer")

    result = []
    append = result.append
    while a or b:
        # comparing every bit of a and b, finding bits through division method.
        # https://en.wikipedia.org/wiki/Binary_number#Conversion_to_and_from_other_numeral_systems
        append(str(int((a % 2) != (b % 2))))
        a //= 2
        b //= 2
    append('0b')
    return ''.join(reversed(result))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
