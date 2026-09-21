def excess_3_code(number: int) -> str:
    """
    Find excess-3 code of integer base 10.
    Add 3 to all digits in a decimal number then convert to a binary-coded decimal.
    https://en.wikipedia.org/wiki/Excess-3

    >>> excess_3_code(0)
    '0b0011'
    >>> excess_3_code(3)
    '0b0110'
    >>> excess_3_code(2)
    '0b0101'
    >>> excess_3_code(20)
    '0b01010011'
    >>> excess_3_code(120)
    '0b010001010011'
    """
    num = ""
    for digit in str(max(0, number)):
        num += str(bin(int(digit) + 3))[2:].zfill(4)
    return "0b" + num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
