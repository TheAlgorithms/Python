"""
* Author: Siddharth Singh (https://github.com/coolsidd)
* Description: Convert a binary string to Base64.
References for better understanding:
https://en.wikipedia.org/wiki/Base64
"""

B64_TO_BITS = {
    "A": "000000",
    "B": "000001",
    "C": "000010",
    "D": "000011",
    "E": "000100",
    "F": "000101",
    "G": "000110",
    "H": "000111",
    "I": "001000",
    "J": "001001",
    "K": "001010",
    "L": "001011",
    "M": "001100",
    "N": "001101",
    "O": "001110",
    "P": "001111",
    "Q": "010000",
    "R": "010001",
    "S": "010010",
    "T": "010011",
    "U": "010100",
    "V": "010101",
    "W": "010110",
    "X": "010111",
    "Y": "011000",
    "Z": "011001",
    "a": "011010",
    "b": "011011",
    "c": "011100",
    "d": "011101",
    "e": "011110",
    "f": "011111",
    "g": "100000",
    "h": "100001",
    "i": "100010",
    "j": "100011",
    "k": "100100",
    "l": "100101",
    "m": "100110",
    "n": "100111",
    "o": "101000",
    "p": "101001",
    "q": "101010",
    "r": "101011",
    "s": "101100",
    "t": "101101",
    "u": "101110",
    "v": "101111",
    "w": "110000",
    "x": "110001",
    "y": "110010",
    "z": "110011",
    "0": "110100",
    "1": "110101",
    "2": "110110",
    "3": "110111",
    "4": "111000",
    "5": "111001",
    "6": "111010",
    "7": "111011",
    "8": "111100",
    "9": "111101",
    "+": "111110",
    "/": "111111",
}


def base64_to_bin(base64_str: str) -> str:
    """Convert a base64 value to its binary equivalent.

    >>> base64_to_bin("ABC")
    '000000000001000010'
    >>> base64_to_bin("    -abc    ")
    '-011010011011011100'
    >>> base64_to_bin("    a-bc    ")
    Traceback (most recent call last):
      ...
    ValueError: Invalid base64 string. Invalid char - at pos 1
    >>> base64_to_bin("")
    Traceback (most recent call last):
      ...
    ValueError: Empty string was passed to the function
    """
    b64_str = str(base64_str).strip()
    if not b64_str:
        raise ValueError("Empty string was passed to the function")
    is_negative = b64_str[0] == "-"
    if is_negative:
        b64_str = b64_str[1:]
    bin_str = ""
    for i, x in enumerate(b64_str):
        if x not in B64_TO_BITS:
            exception_message = f"Invalid base64 string. Invalid char {x} at pos {i}"
            raise ValueError(exception_message)
        bin_str += B64_TO_BITS[x]
    if is_negative:
        bin_str = "-" + bin_str
    return bin_str


if __name__ == "__main__":
    import doctest

    doctest.testmod()
