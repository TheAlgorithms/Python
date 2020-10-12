def oct_to_decimal(oct_string: str) -> int:
    """
    Convert a octal value to its decimal equivalent

    >>> oct_to_decimal("12")
    10
    >>> oct_to_decimal(" 12   ")
    10
    >>> oct_to_decimal("-45")
    -37
    >>> oct_to_decimal("2-0Fm")
    Traceback (most recent call last):
    ...
    ValueError: Non-octal value was passed to the function
    >>> oct_to_decimal("")
    Traceback (most recent call last):
    ...
    ValueError: Empty string value was passed to the function
    >>> oct_to_decimal("19")
    Traceback (most recent call last):
    ...
    ValueError: Non-octal value was passed to the function
    """
    # Strip oct_string of whitespaces
    oct_string = str(oct_string).strip()
    if not oct_string:
        raise ValueError("Empty string value was passed to the function")

    # Check if oct_string is a negative value
    is_negative = oct_string[0] == "-"
    if is_negative:
        # Remove (-) from oct_string
        oct_string = oct_string[1:]

    # check if oct_string is an octal value and convert
    if oct_string.isdecimal() and all(0 <= int(char) <= 7 for char in oct_string):
        decimal_number = 0
        for char in oct_string:
            decimal_number = 8 * decimal_number + int(char)
        if is_negative:
            decimal_number = -decimal_number
        return decimal_number
    else:
        # else raise exception
        raise ValueError("Non-octal value was passed to the function")


if __name__ == "__main__":
    from doctest import testmod

    testmod()
