"""
Convert a string of characters to a sequence of numbers
corresponding to the character's position in the alphabet.

https://www.dcode.fr/letter-number-cipher
http://bestcodes.weebly.com/a1z26.html
"""

from __future__ import annotations


def encode(plain: str) -> list[int]:
    """
    >>> encode("myname")
    [13, 25, 14, 1, 13, 5]
    """
    return [ord(elem) - 96 for elem in plain]


def decode(encoded: list[int]) -> str:
    """
    >>> decode([13, 25, 14, 1, 13, 5])
    'myname'

    >>> decode([0, 1, 2])
    Traceback (most recent call last):
        ...
    ValueError: 0 is not a valid A1Z26 code (must be 1-26)

    >>> decode([26, 27, 28])
    Traceback (most recent call last):
        ...
    ValueError: 27 is not a valid A1Z26 code (must be 1-26)
    """
    out = []
    for code in encoded:
        if not isinstance(code, int) or isinstance(code, bool) or not 1 <= code <= 26:
            raise ValueError(
                f"{code} is not a valid A1Z26 code (must be 1-26)"
            )
        out.append(chr(code + 96))
    return "".join(out)


def main() -> None:
    encoded = encode(input("-> ").strip().lower())
    print("Encoded: ", encoded)
    print("Decoded:", decode(encoded))


if __name__ == "__main__":
    main()
