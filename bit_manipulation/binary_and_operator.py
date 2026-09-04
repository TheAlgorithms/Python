# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_and(a: int, b: int) -> str:
    """
    Take in 2 integers, convert them to binary,
    return a binary number that is the
    result of a binary and operation on the integers provided.
    The AND operation compares each bit position of two numbers. The result has a 1 bit
    only where BOTH input numbers have 1 bits at the same position; otherwise,
    the result bit is 0.
    Algorithm:
    1. Convert both numbers to binary representation
    2. Pad shorter binary string with leading zeros
    3. For each bit position, output 1 only if both input bits are 1
    4. Return the result as a binary string
    Example: 25 (0b11001) AND 32 (0b100000)
    Position: 5 4 3 2 1 0
    25:       0 1 1 0 0 1
    32:       1 0 0 0 0 0
    Result:   0 0 0 0 0 0 = 0 (no position has both 1s)
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
    ValueError: the value of both inputs must be positive
    >>> binary_and(0, 1.1)
    Traceback (most recent call last):
        ...
    ValueError: Unknown format code 'b' for object of type 'float'
    >>> binary_and("0", "1")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0 or b < 0:
        raise ValueError("the value of both inputs must be positive")

    a_binary = format(a, "b")
    b_binary = format(b, "b")

    max_len = max(len(a_binary), len(b_binary))

    return "0b" + "".join(
        str(int(char_a == "1" and char_b == "1"))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
