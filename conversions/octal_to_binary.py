"""
* Author: Bama Charan Chhandogi (https://github.com/BamaCharanChhandogi)
* Description: Convert a Octal number to Binary.

reference for better understand

URL: https://en.wikipedia.org/wiki/Binary_number
URL: https://en.wikipedia.org/wiki/Octal
"""
def octal_to_binary(octal_number: str) -> str:
    binary_number = ""
    octal_digits = "01234567"

    """
    ValueError: String to the function
    >>> oct_to_decimal("Av")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> oct_to_decimal("90")
    Traceback (most recent call last):
        ...
    ValueError: octal value was passed to the function
    >>> oct_to_decimal("17")
    001111
    >>> oct_to_decimal("7")
    111
    """
    for digit in octal_number:
        if digit not in octal_digits:
            raise ValueError("Invalid octal digit")

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
