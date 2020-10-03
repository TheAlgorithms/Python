# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_and(a: int, b: int):
    """
    Take in 2 integers, convert them to binary,
    return a binary number that is the
    result of a binary and operation on the integers provided.

    >>> binary_and(25, 32)
    '0b000000'
    >>> binary_and(37, 50)
    '0b100000'
    >>> binary_and(21, 30)
    '0b10100'
    >>> binary_and(58, 73)
    '0b0001000'
    >>> binary_and(0, 255)
    '0b00000000'
    >>> binary_and(256, 256)
    '0b100000000'
    >>> binary_and(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: the value of both input must be positive
    >>> binary_and(0, 1.1)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> binary_and("0", "1")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0 or b < 0:
        raise ValueError("the value of both input must be positive")
    if isinstance(a, float) or isinstance(b, float):
        raise TypeError("'float' object cannot be interpreted as an integer")

    And = []
    append = And.append
    while a or b:
        append(str(int((a % 2) and (b % 2))))
        a //= 2
        b //= 2
    append('0b')
    return ''.join(reversed(And))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
