"""
* Author: Siddharth Singh (https://github.com/coolsidd)
* Description: Convert a binary string to Base64.

References for better understanding:
https://en.wikipedia.org/wiki/Base64
"""

BITS_TO_B64 = {
    "000000": "A",
    "000001": "B",
    "000010": "C",
    "000011": "D",
    "000100": "E",
    "000101": "F",
    "000110": "G",
    "000111": "H",
    "001000": "I",
    "001001": "J",
    "001010": "K",
    "001011": "L",
    "001100": "M",
    "001101": "N",
    "001110": "O",
    "001111": "P",
    "010000": "Q",
    "010001": "R",
    "010010": "S",
    "010011": "T",
    "010100": "U",
    "010101": "V",
    "010110": "W",
    "010111": "X",
    "011000": "Y",
    "011001": "Z",
    "011010": "a",
    "011011": "b",
    "011100": "c",
    "011101": "d",
    "011110": "e",
    "011111": "f",
    "100000": "g",
    "100001": "h",
    "100010": "i",
    "100011": "j",
    "100100": "k",
    "100101": "l",
    "100110": "m",
    "100111": "n",
    "101000": "o",
    "101001": "p",
    "101010": "q",
    "101011": "r",
    "101100": "s",
    "101101": "t",
    "101110": "u",
    "101111": "v",
    "110000": "w",
    "110001": "x",
    "110010": "y",
    "110011": "z",
    "110100": "0",
    "110101": "1",
    "110110": "2",
    "110111": "3",
    "111000": "4",
    "111001": "5",
    "111010": "6",
    "111011": "7",
    "111100": "8",
    "111101": "9",
    "111110": "+",
    "111111": "/",
}


def bin_to_base64(bin_str: str) -> str:
    """Convert a binary value to its base64 equivalent


    >>> bin_to_base64("000001")
    'AB'
    >>> bin_to_base64("0")
    'A'
    >>> bin_to_base64("1")
    'B'
    >>> bin_to_base64("-1")
    '-B'
    >>> bin_to_base64(" -000001 ")
    '-AB'
    >>> bin_to_base64("0-0")
    Traceback (most recent call last):
        ...
    ValueError: Non-binary value was passed to the function
    >>> bin_to_base64("")
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function
    """
    bin_str = str(bin_str).strip()
    if not bin_str:
        raise ValueError("Empty string was passed to the function")
    is_negative = bin_str[0] == "-"
    if is_negative:
        bin_str = bin_str[1:]
    if not all(char in "01" for char in bin_str):
        raise ValueError("Non-binary value was passed to the function")
    bin_str = "0" * (6 * (divmod(len(bin_str), 6)[0] + 1) - len(bin_str)) + bin_str
    base64_str = ""
    while len(bin_str) > 0:
        base64_str += BITS_TO_B64[bin_str[:6]]
        bin_str = bin_str[6:]

    return "-" + base64_str if is_negative else base64_str


if __name__ == "__main__":
    from doctest import testmod

    testmod()
