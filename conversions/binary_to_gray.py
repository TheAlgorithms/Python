"""
Convert gray code into binary code and vice versa.

gray code:
In the binary numbering scheme known as gray code,
which is sometimes referred to as reflected binary code or unit distance code,
two subsequent values only differ by one bit. In other words,
Gray code is useful for error correction, rotary encoders, and
digital communication since only one bit changes its value 
as you go from one number to the next.


Reference : https://en.wikipedia.org/wiki/Gray_code
"""


def binary_to_gray(binary: str) -> str:
    """
    Convert a binary number to Gray code

    binary: A binary number as a string.
    return: The Gray code representation as a string.
    >>> binary_to_gray("1101101")
    '1011011'
    """
    gray = binary[0]
    for i in range(1, len(binary)):
        gray_bit = int(binary[i]) ^ int(binary[i - 1])
        gray += str(gray_bit)
    return gray


def gray_to_binary(gray: str) -> str:
    """
    Convert Gray code to binary.

    gray: A Gray code representation as a string.
    return: The binary number as a string.
    >>> gray_to_binary("1011110")
    '1101011'
    """
    binary = gray[0]
    for i in range(1, len(gray)):
        binary_bit = int(gray[i]) ^ int(binary[i - 1])
        binary += str(binary_bit)
    return binary


if __name__ == "__main__":
    import doctest
    doctest.testmod()
