def octal_to_hex(n: str) -> str:
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

    if not isinstance(n, str):
        raise TypeError("Expected a string as input")
    if n.startswith("0o"):
        n = n[2:]
    if n == "":
        raise ValueError("Empty string was passed to the function")
    for char in n:
        if char not in "01234567":
            raise ValueError("Not a Valid Octal Number")

    def hex_char(i: int) -> str:
        if i < 10:
            return str(i)
        return chr(i + 55)  # (i-10 + 65) i.e. for characters

    decimal = 0
    for i in str(n):
        decimal <<= 3
        decimal |= int(i)

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
