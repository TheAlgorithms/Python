def octal_to_binary(octal: str) -> str:
    """
    Convert an octal value to its binary equivalent

    >>> octal_to_binary("")
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function
    >>> octal_to_binary("-")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary("e")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary(8)
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary("-e")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary("-8")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary("1")
    '0b1'
    >>> octal_to_binary("-1")
    '-0b1'
    >>> octal_to_binary("12")
    '0b1010'
    >>> octal_to_binary(" 12   ")
    '0b1010'
    >>> octal_to_binary("-45")
    '-0b100101'
    >>> octal_to_binary("-")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary("0")
    '0b0'
    >>> octal_to_binary("-4055")
    '-0b100000101101'
    >>> octal_to_binary("2-0Fm")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary("")
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function
    >>> octal_to_binary("19")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    """

    oct_string = str(octal).strip()
    if not oct_string:
        raise ValueError("Empty string was passed to the function")
    is_negative = oct_string[0] == "-"
    if is_negative:
        oct_string = oct_string[1:]
    if not oct_string.isdigit() or not all(0 <= int(char) <= 7 for char in oct_string):
        raise ValueError("Non-octal value was passed to the function")
    decimal_number = 0
    for char in oct_string:
        decimal_number = 8 * decimal_number + int(char)
    if is_negative:
        decimal_number = -decimal_number

    # Converting Decimal to Binary
    if decimal_number == 0:
        return "0b0"

    negative = False
    if decimal_number < 0:
        negative = True
        decimal_number = -decimal_number

    binary: list[int] = []
    while decimal_number > 0:
        binary.insert(0, decimal_number % 2)
        decimal_number >>= 1

    if negative:
        return "-0b" + "".join(str(e) for e in binary)

    return "0b" + "".join(str(e) for e in binary)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
