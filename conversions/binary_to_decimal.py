def bin_to_decimal(bin_string: str) -> int:
    """
    Convert a binary value to its decimal equivalent.

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

    if not bin_string or not all(char in "01" for char in bin_string):
        raise ValueError("Non-binary value was passed to the function")

    result = int(bin_string, 2)
    return -result if is_negative else result


if __name__ == "__main__":
    from doctest import testmod
    testmod()
