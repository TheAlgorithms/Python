def bin_to_decimal(bin_string: str) -> int:
    """
    Convert a binary value to its decimal equivalent

    >>> bin_to_decimal("101")
    5
    >>> bin_to_decimal(" 1010   ")
    10
    >>> bin_to_decimal("-11101")
    -29
    >>> bin_to_decimal("0")
    0
    >>> bin_to_decimal("a")
    Traceback (most recent call last):
        ...
    ValueError: Non-binary value was passed to the function
    >>> bin_to_decimal("")
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function
    >>> bin_to_decimal("39")
    Traceback (most recent call last):
        ...
    ValueError: Non-binary value was passed to the function
    """
    bin_string = str(bin_string).strip()
    if not bin_string:
        raise ValueError("Empty string was passed to the function")
    is_negative = bin_string[0] == "-"
    if is_negative:
        bin_string = bin_string[1:]
    if not all(char in "01" for char in bin_string):
        raise ValueError("Non-binary value was passed to the function")
    decimal_number = 0
    for char in bin_string:
        decimal_number = 2 * decimal_number + int(char)
    return -decimal_number if is_negative else decimal_number


def bcd_to_gray(bcd):
    """
    Convert a Binary-Coded Decimal (BCD) number to Gray code.

    Args:
    bcd (int): The BCD number (0-9).

    Returns:
    str: The Gray code representation of the BCD number.

    Raises:
    ValueError: If the input is not a valid BCD number (0-9).
    """

    # Check if the input is a valid BCD (0-9)
    if bcd < 0 or bcd > 9:
        raise ValueError("Input must be a BCD number between 0 and 9.")

    # Convert BCD to binary
    binary = format(bcd, "04b")  # 4-bit binary representation

    # Convert binary to Gray code
    gray = binary[0]  # The most significant bit remains the same
    for i in range(1, len(binary)):
        # XOR the current bit with the previous bit
        gray += str(int(binary[i]) ^ int(binary[i - 1]))

    return gray


# Example usage
if __name__ == "__main__":
    bcd_values = range(10)  # BCD values from 0 to 9
    for bcd in bcd_values:
        gray_code = bcd_to_gray(bcd)
        print(f"BCD: {bcd} -> Gray Code: {gray_code}")


if __name__ == "__main__":
    from doctest import testmod

    testmod()
