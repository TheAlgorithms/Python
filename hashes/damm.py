"""
The Damm algorithm is a check digit algorithm that detects all single-digit
errors and all adjacent transposition errors.

The operation table below defines a weakly totally anti-symmetric quasigroup
of order 10: every row and column is a permutation of the digits, and the main
diagonal contains only zeros. These properties are what give the algorithm its
error-detection guarantees.

https://en.wikipedia.org/wiki/Damm_algorithm
"""

from __future__ import annotations

DAMM_TABLE: tuple[tuple[int, ...], ...] = (
    (0, 3, 1, 7, 5, 9, 8, 6, 4, 2),
    (7, 0, 9, 2, 1, 5, 4, 8, 6, 3),
    (4, 2, 0, 6, 8, 7, 1, 3, 5, 9),
    (1, 7, 5, 0, 9, 8, 3, 4, 2, 6),
    (6, 1, 2, 3, 0, 4, 5, 9, 7, 8),
    (3, 6, 7, 4, 2, 0, 9, 5, 8, 1),
    (5, 8, 6, 9, 7, 2, 0, 1, 3, 4),
    (8, 9, 4, 5, 3, 6, 2, 0, 1, 7),
    (9, 4, 3, 8, 6, 1, 7, 2, 0, 5),
    (2, 5, 8, 1, 4, 3, 6, 7, 9, 0),
)


def damm_checksum(number: str) -> int:
    """
    Return the Damm interim digit after processing every digit in number.

    A complete number (payload plus its check digit) is valid when the checksum
    is 0. Applied to a payload without a check digit, the checksum is exactly
    the digit that should be appended.

    >>> damm_checksum("5724")
    0
    >>> damm_checksum("5725")
    4
    >>> damm_checksum("572")
    4
    >>> damm_checksum("05724")
    0
    >>> damm_checksum("")
    Traceback (most recent call last):
        ...
    ValueError: number must be a non-empty string of digits
    >>> damm_checksum(572)
    Traceback (most recent call last):
        ...
    TypeError: number must be a string
    """
    if not isinstance(number, str):
        raise TypeError("number must be a string")
    if not number or not number.isascii() or not number.isdigit():
        raise ValueError("number must be a non-empty string of digits")

    interim = 0
    for digit in number:
        interim = DAMM_TABLE[interim][int(digit)]
    return interim


def generate_check_digit(number: str) -> str:
    """
    Return the Damm check digit for a payload without a check digit.

    >>> generate_check_digit("572")
    '4'
    >>> generate_check_digit("5724")
    '0'
    >>> generate_check_digit("")
    Traceback (most recent call last):
        ...
    ValueError: number must be a non-empty string of digits
    """
    return str(damm_checksum(number))


def is_valid(number: str) -> bool:
    """
    Return whether a number with an appended check digit is valid.

    >>> is_valid("5724")
    True
    >>> is_valid("05724")
    True
    >>> is_valid("5725")
    False
    >>> is_valid("572")
    False
    >>> is_valid("")
    False
    >>> is_valid(5724)
    Traceback (most recent call last):
        ...
    TypeError: number must be a string
    """
    if not isinstance(number, str):
        raise TypeError("number must be a string")
    return len(number) > 1 and damm_checksum(number) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
