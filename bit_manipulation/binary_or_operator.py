"""Bitwise OR helper.

Return a zero-padded binary string representing ``a | b`` where the width is the
maximum bit length of the inputs. Only non-negative integers are accepted.

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

Invalid inputs raise clear exceptions:

>>> binary_or(0, -1)
Traceback (most recent call last):
    ...
ValueError: inputs must be non-negative integers
>>> binary_or(0, 1.1)
Traceback (most recent call last):
    ...
TypeError: inputs must be integers
>>> binary_or("0", "1")
Traceback (most recent call last):
    ...
TypeError: inputs must be integers
"""

# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_or(a: int, b: int) -> str:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("inputs must be non-negative integers")
    max_len = max(a.bit_length(), b.bit_length())
    return f"0b{(a | b):0{max_len}b}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
