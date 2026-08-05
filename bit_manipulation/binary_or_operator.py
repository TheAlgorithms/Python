# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_or(a: int, b: int) -> str:
    """
    Take in 2 integers, convert them to binary, and return a binary number that is the
    result of a binary or operation on the integers provided.
    The OR operation compares each bit position of two numbers. The result has a 1 bit
    if AT LEAST ONE of the input numbers has a 1 bit at that position;
    the result is 0 only when both input bits are 0.
    Algorithm:
    1. Convert both numbers to binary representation
    2. Pad shorter binary string with leading zeros
    3. For each bit position, output 1 if at least one input bit is 1
    4. Output 0 only if both input bits are 0
    5. Return the result as a binary string
    Example: 25 (0b11001) OR 32 (0b100000)
    Position: 5 4 3 2 1 0
    25:       0 1 1 0 0 1
    32:       1 0 0 0 0 0
    Result:   1 1 1 0 0 1 = 57 (all positions with at least one 1)
    >>> binary_or(25, 32)
    '0b111001'
    >>> binary_or(37, 50)
    '0b110111'
    >>> binary_or(21, 30)
    '0b11111'
    >>> binary_or(58, 73)
    '0b1111011'
    >>> binary_or(0, 255)
    '0b11111111'
    >>> binary_or(0, 256)
    '0b100000000'
    >>> binary_or(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: the value of both inputs must be positive
    >>> binary_or(0, 1.1)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> binary_or("0", "1")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0 or b < 0:
        raise ValueError("the value of both inputs must be positive")
    a_binary = str(bin(a))[2:]  # remove the leading "0b"
    b_binary = str(bin(b))[2:]
    max_len = max(len(a_binary), len(b_binary))
    return "0b" + "".join(
        str(int("1" in (char_a, char_b)))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
