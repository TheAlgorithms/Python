def bin_to_hexadecimal(binary_str: str) -> str:
    """
    Converting a binary string into hexadecimal using Grouping Method

    >>> bin_to_hexadecimal('101011111')
    '0x15f'
    >>> bin_to_hexadecimal(' 1010   ')
    '0x0a'
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
    BITS_TO_HEX = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "a",
        "1011": "b",
        "1100": "c",
        "1101": "d",
        "1110": "e",
        "1111": "f",
    }

    # Sanitising parameter
    binary_str = str(binary_str).strip()

    # Exceptions
    if not binary_str:
        raise ValueError("Empty string was passed to the function")
    is_negative = binary_str[0] == "-"
    binary_str = binary_str[1:] if is_negative else binary_str
    if not all(char in "01" for char in binary_str):
        raise ValueError("Non-binary value was passed to the function")

    binary_str = (
        "0" * (4 * (divmod(len(binary_str), 4)[0] + 1) - len(binary_str)) + binary_str
    )

    hexadecimal = []
    for x in range(0, len(binary_str), 4):
        hexadecimal.append(BITS_TO_HEX[binary_str[x : x + 4]])
    hexadecimal_str = "0x" + "".join(hexadecimal)

    return "-" + hexadecimal_str if is_negative else hexadecimal_str


if __name__ == "__main__":
    from doctest import testmod

    testmod()
