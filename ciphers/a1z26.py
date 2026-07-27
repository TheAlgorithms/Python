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
    >>> encode("HELLO")
    Traceback (most recent call last):
        ...
    ValueError: plain text must contain only lowercase letters 'a'-'z'
    """
    if not plain or any(not ("a" <= elem <= "z") for elem in plain):
        raise ValueError("plain text must contain only lowercase letters 'a'-'z'")
    return [ord(elem) - 96 for elem in plain]


def decode(encoded: list[int]) -> str:
    """
    >>> decode([13, 25, 14, 1, 13, 5])
    'myname'
    >>> decode([0, 27])
    Traceback (most recent call last):
        ...
    ValueError: encoded values must be integers between 1 and 26
    """
    if not encoded or any(not (1 <= elem <= 26) for elem in encoded):
        raise ValueError("encoded values must be integers between 1 and 26")
    return "".join(chr(elem + 96) for elem in encoded)


def main() -> None:
    encoded = encode(input("-> ").strip().lower())
    print("Encoded: ", encoded)
    print("Decoded:", decode(encoded))


if __name__ == "__main__":
    main()
