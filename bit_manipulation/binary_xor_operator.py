"""Bitwise XOR helper.

Return a zero-padded binary string representing ``a ^ b`` where the width is the
maximum bit length of the inputs. Only non-negative integers are accepted.

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

Invalid inputs raise clear exceptions:

>>> binary_xor(0, -1)
Traceback (most recent call last):
    ...
ValueError: inputs must be non-negative integers
>>> binary_xor(0, 1.1)
Traceback (most recent call last):
    ...
TypeError: inputs must be integers
>>> binary_xor("0", "1")
Traceback (most recent call last):
    ...
TypeError: inputs must be integers
"""

# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_xor(a: int, b: int) -> str:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("inputs must be non-negative integers")

    max_len = max(a.bit_length(), b.bit_length())
    return f"0b{(a ^ b):0{max_len}b}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
