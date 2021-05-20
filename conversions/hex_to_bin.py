def hex_to_bin(hex_num: str) -> int:
    """
    Convert a hexadecimal value to its binary equivalent
    #https://stackoverflow.com/questions/1425493/convert-hex-to-binary
    Here, we have used the bitwise right shift operator: >>
    Shifts the bits of the number to the right and fills 0 on voids left as a result.
    Similar effect as of dividing the number with some power of two.
    Example:
    a = 10
    a >> 1 = 5

    >>> hex_to_bin("AC")
    10101100
    >>> hex_to_bin("9A4")
    100110100100
    >>> hex_to_bin("   12f   ")
    100101111
    >>> hex_to_bin("FfFf")
    1111111111111111
    >>> hex_to_bin("-fFfF")
    -1111111111111111
    >>> hex_to_bin("F-f")
    Traceback (most recent call last):
    ...
    ValueError: Invalid value was passed to the function
    >>> hex_to_bin("")
    Traceback (most recent call last):
    ...
    ValueError: No value was passed to the function
    """

    hex_num = hex_num.strip()
    if not hex_num:
        raise ValueError("No value was passed to the function")

    is_negative = hex_num[0] == "-"
    if is_negative:
        hex_num = hex_num[1:]

    try:
        int_num = int(hex_num, 16)
    except ValueError:
        raise ValueError("Invalid value was passed to the function")

    bin_str = ""
    while int_num > 0:
        bin_str = str(int_num % 2) + bin_str
        int_num >>= 1

    return int(("-" + bin_str) if is_negative else bin_str)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
