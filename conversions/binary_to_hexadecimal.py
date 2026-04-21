def bin_to_hexadecimal(binary_str: str) -> str:
    """
    Convert a binary string to hexadecimal.

    >>> bin_to_hexadecimal('101011111')
    '0x15f'
    >>> bin_to_hexadecimal(' 1010   ')
    '0xa'
    >>> bin_to_hexadecimal('-11101')
    '-0x1d'
    >>> bin_to_hexadecimal('a')
    Traceback (most recent call last):
        ...
    ValueError: Non-binary value was passed to the function
    >>> bin_to_hexadecimal('')
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function
    """
    binary_str = str(binary_str).strip()

    if not binary_str:
        raise ValueError("Empty string was passed to the function")

    is_negative = binary_str[0] == "-"
    binary_str = binary_str[1:] if is_negative else binary_str

    if not binary_str or not all(char in "01" for char in binary_str):
        raise ValueError("Non-binary value was passed to the function")

    hex_str = "0x" + hex(int(binary_str, 2))[2:]
    return "-" + hex_str if is_negative else hex_str


if __name__ == "__main__":
    from doctest import testmod
    testmod()
