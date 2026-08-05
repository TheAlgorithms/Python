# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_xor(a: int, b: int) -> str:
    """
    Take in 2 integers, convert them to binary,
    return a binary number that is the
    result of a binary xor operation on the integers provided.
    The XOR operation compares each bit position of two numbers. The result has a 1 bit
    only when the input bits are DIFFERENT (one is 1 and the other is 0);
    the result is 0 when both input bits are the same (both 0 or both 1).
    Algorithm:
    1. Convert both numbers to binary representation
    2. Pad shorter binary string with leading zeros
    3. For each bit position, output 1 if input bits are different
    4. Output 0 if input bits are the same
    5. Return the result as a binary string
    Example: 25 (0b11001) XOR 32 (0b100000)
    Position: 5 4 3 2 1 0
    25:       0 1 1 0 0 1
    32:       1 0 0 0 0 0
    Result:   1 1 1 0 0 1 = 57 (all positions have different bits)
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
    ValueError: the value of both inputs must be positive
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
        raise ValueError("the value of both inputs must be positive")

    a_binary = str(bin(a))[2:]  # remove the leading "0b"
    b_binary = str(bin(b))[2:]  # remove the leading "0b"

    max_len = max(len(a_binary), len(b_binary))

    return "0b" + "".join(
        str(int(char_a != char_b))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
