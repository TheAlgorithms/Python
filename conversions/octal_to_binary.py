def octal_to_binary(octal_number: str) -> str:
    """
    Convert an octal number to binary.

    Args:
        octal_number (str): The octal number as a string.

    Returns:
        str: The binary representation of the octal number.
    """
    binary_number = ""
    octal_digits = "01234567"

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
