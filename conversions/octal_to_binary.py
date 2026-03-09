"""
* Author: Bama Charan Chhandogi (https://github.com/BamaCharanChhandogi)
* Description: Convert a Octal number to Binary.

References for better understanding:
https://en.wikipedia.org/wiki/Binary_number
https://en.wikipedia.org/wiki/Octal
"""


def octal_to_binary(octal_number: str) -> str:
    """
    Convert an Octal number to Binary.

    >>> octal_to_binary("17")
    '001111'
    >>> octal_to_binary("7")
    '111'
    >>> octal_to_binary("Av")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary("@#")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary("")
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function
    """
    if not octal_number:
        raise ValueError("Empty string was passed to the function")

    binary_number = ""
    octal_digits = "01234567"
    for digit in octal_number:
        if digit not in octal_digits:
            raise ValueError("Non-octal value was passed to the function")

        binary_digit = ""
        value = int(digit)
        for _ in range(3):
            binary_digit = str(value % 2) + binary_digit
            value //= 2
        binary_number += binary_digit

    return binary_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
