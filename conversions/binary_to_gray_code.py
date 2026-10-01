"""
Convert between Binary and Gray Code representations.

Gray Code (also known as reflected binary code) is a binary numeral system where
two successive values differ in only one bit. This property makes it useful in
error correction, digital communications, and position encoders.

Wikipedia: https://en.wikipedia.org/wiki/Gray_code
"""


def binary_to_gray(binary_number: int) -> int:
    """
    Convert a binary number to its Gray Code equivalent.

    The algorithm works by XORing the binary number with itself right-shifted by 1.
    Formula: gray = binary XOR (binary >> 1)

    Args:
        binary_number: A positive integer representing a binary number

    Returns:
        The Gray Code equivalent as an integer

    Examples:
    >>> binary_to_gray(0)
    0
    >>> binary_to_gray(1)
    1
    >>> binary_to_gray(2)
    3
    >>> binary_to_gray(3)
    2
    >>> binary_to_gray(4)
    6
    >>> binary_to_gray(7)
    4
    >>> binary_to_gray(10)
    15
    >>> binary_to_gray(15)
    8
    >>> binary_to_gray(255)
    128
    >>> binary_to_gray(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    >>> binary_to_gray(3.5)
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """
    if not isinstance(binary_number, int):
        raise TypeError("Input must be an integer")
    if binary_number < 0:
        raise ValueError("Input must be a non-negative integer")

    return binary_number ^ (binary_number >> 1)


def gray_to_binary(gray_number: int) -> int:
    """
    Convert a Gray Code number to its binary equivalent.

    The algorithm works by repeatedly XORing the gray code with itself right-shifted,
    until the right-shifted value becomes 0.

    Args:
        gray_number: A positive integer representing a Gray Code number

    Returns:
        The binary equivalent as an integer

    Examples:
    >>> gray_to_binary(0)
    0
    >>> gray_to_binary(1)
    1
    >>> gray_to_binary(3)
    2
    >>> gray_to_binary(2)
    3
    >>> gray_to_binary(6)
    4
    >>> gray_to_binary(4)
    7
    >>> gray_to_binary(15)
    10
    >>> gray_to_binary(8)
    15
    >>> gray_to_binary(128)
    255
    >>> gray_to_binary(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    >>> gray_to_binary(5.5)
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """
    if not isinstance(gray_number, int):
        raise TypeError("Input must be an integer")
    if gray_number < 0:
        raise ValueError("Input must be a non-negative integer")

    binary_number = gray_number
    gray_number >>= 1

    while gray_number:
        binary_number ^= gray_number
        gray_number >>= 1

    return binary_number


def decimal_to_gray(decimal_number: int) -> str:
    """
    Convert a decimal number to its Gray Code representation as a binary string.

    Args:
        decimal_number: A positive integer in decimal

    Returns:
        Gray Code representation as a binary string

    Examples:
    >>> decimal_to_gray(0)
    '0'
    >>> decimal_to_gray(1)
    '1'
    >>> decimal_to_gray(2)
    '11'
    >>> decimal_to_gray(3)
    '10'
    >>> decimal_to_gray(4)
    '110'
    >>> decimal_to_gray(10)
    '1111'
    >>> decimal_to_gray(15)
    '1000'
    >>> decimal_to_gray(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    """
    if not isinstance(decimal_number, int):
        raise TypeError("Input must be an integer")
    if decimal_number < 0:
        raise ValueError("Input must be a non-negative integer")

    gray_code = binary_to_gray(decimal_number)
    return bin(gray_code)[2:]  # Remove '0b' prefix


def gray_to_decimal(gray_string: str) -> int:
    """
    Convert a Gray Code binary string to its decimal equivalent.

    Args:
        gray_string: A string of 0s and 1s representing Gray Code

    Returns:
        The decimal equivalent as an integer

    Examples:
    >>> gray_to_decimal('0')
    0
    >>> gray_to_decimal('1')
    1
    >>> gray_to_decimal('11')
    2
    >>> gray_to_decimal('10')
    3
    >>> gray_to_decimal('110')
    4
    >>> gray_to_decimal('1111')
    10
    >>> gray_to_decimal('1000')
    15
    >>> gray_to_decimal('invalid')
    Traceback (most recent call last):
        ...
    ValueError: Invalid binary string
    >>> gray_to_decimal('')
    Traceback (most recent call last):
        ...
    ValueError: Input string cannot be empty
    """
    if not gray_string:
        raise ValueError("Input string cannot be empty")

    # Validate binary string
    if not all(bit in "01" for bit in gray_string):
        raise ValueError("Invalid binary string")

    gray_number = int(gray_string, 2)
    return gray_to_binary(gray_number)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Interactive demonstration
    print("=== Binary to Gray Code Converter ===\n")

    # Demonstrate conversions for 0-15
    print("Decimal | Binary   | Gray Code")
    print("--------|----------|----------")
    for i in range(16):
        binary = bin(i)[2:].zfill(4)
        gray = decimal_to_gray(i).zfill(4)
        print(f"{i:7} | {binary:8} | {gray:9}")

    print("\n=== Verification: Gray to Binary ===\n")
    print("Gray Code | Binary   | Decimal")
    print("----------|----------|--------")
    for i in range(16):
        gray = decimal_to_gray(i).zfill(4)
        decimal = gray_to_decimal(gray)
        binary = bin(decimal)[2:].zfill(4)
        print(f"{gray:9} | {binary:8} | {decimal:7}")
