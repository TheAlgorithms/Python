def hex_char(value: int) -> str:
    if value < 10:
        return str(value)
    return chr(value + 55)  # (i-10 + 65) i.e. for characters


def octal_to_hex(octal: str) -> str:
    """
    Convert an Octal number to Hexadecimal number.

    >>> octal_to_hex("100")
    '0X40'
    >>> octal_to_hex("235")
    '0X9D'
    >>> octal_to_hex(17)
    Traceback (most recent call last):
        ...
    TypeError: Expected a string as input
    >>> octal_to_hex("Av")
    Traceback (most recent call last):
        ...
    ValueError: Not a Valid Octal Number
    >>> octal_to_hex("")
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function

    For more information: https://en.wikipedia.org/wiki/Octal
    """

    if not isinstance(octal, str):
        raise TypeError("Expected a string as input")
    if octal.startswith("0o"):
        octal = octal[2:]
    if octal == "":
        raise ValueError("Empty string was passed to the function")
    for char in octal:
        if char not in "01234567":
            raise ValueError("Not a Valid Octal Number")

    decimal = 0
    for char in str(octal):
        decimal <<= 3
        decimal |= int(char)

    revhex = ""
    while decimal:
        revhex += hex_char(decimal & 15)
        decimal >>= 4

    hexadecimal = "0X" + revhex[::-1]
    return hexadecimal


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    nums = ["030", "100", "247", "235", "007"]

    ## Main Tests

    for num in nums:
        hexadecimal = octal_to_hex(num)
        expected = hex(int(num, 8)).upper()

        assert hexadecimal == expected

        print(
            "Hex of '0o"
            + num
            + "' is : "
            + hexadecimal
            + " - and Expected was : "
            + expected
        )

    ## Doctests for hex_char function

    for i in range(16):
        assert hex_char(i) == hex(i)[2:].upper()
