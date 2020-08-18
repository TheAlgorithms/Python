"""
https://www.tutorialspoint.com/python3/bitwise_operators_example.htm
This function takes in 2 integer, convert them to binary and returns a binary
in str format that is the result of an Binary OR operation from the 2 integer
input.

Returns a binary resulted from 2 integer input in str format
>>> binary_or(25,32)
'0b111001'

>>> binary_or(37,50)
'0b110111'

>>> binary_or(21,30)
'0b11111'

>>> binary_or(58,73)
'0b1111011'
"""


def binary_or(a : int, b : int):
    if isinstance(a, float) or isinstance(b, float):
        raise TypeError("'Float' object cannot be implemented as an integer")
    if isinstance(a, str) or isinstance(b, str):
        raise TypeError("'str' object cannot be implemented as an integer")
    if a < 0 or b < 0:
        raise ValueError("the value of both input must be positive")
    """
    a_binary and b_binary are the binary of a and b in str format
    """
    a_binary = str(bin(a))[2:]
    b_binary = str(bin(b))[2:]
    binary = []
    max_len = max(len(a_binary), len(b_binary))
    a_binary = a_binary.zfill(max_len)
    b_binary = b_binary.zfill(max_len)
    for char_a, char_b in zip(a_binary, b_binary):
        binary.append(str(int(char_a == "1" or char_b == "1")))
    return "0b" + "".join(binary)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
