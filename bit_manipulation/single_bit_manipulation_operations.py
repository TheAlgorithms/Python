#!/usr/bin/env python3

"""Provide the functionality to manipulate a single bit."""


def set_bit(number: int, position: int) -> int:
    """
    Set the bit at position to 1.

    Details: perform bitwise or for given number and X.
    Where X is a number with all the bits – zeroes and bit on given
    position – one.

    >>> set_bit(0b1101, 1) # 0b1111
    15
    >>> set_bit(0b0, 5) # 0b100000
    32
    >>> set_bit(0b1111, 1) # 0b1111
    15
    """
    return number | (1 << position)


def clear_bit(number: int, position: int) -> int:
    """
    Set the bit at position to 0.

    Details: perform bitwise and for given number and X.
    Where X is a number with all the bits – ones and bit on given
    position – zero.

    >>> clear_bit(0b10010, 1) # 0b10000
    16
    >>> clear_bit(0b0, 5) # 0b0
    0
    """
    return number & ~(1 << position)


def flip_bit(number: int, position: int) -> int:
    """
    Flip the bit at position.

    Details: perform bitwise xor for given number and X.
    Where X is a number with all the bits – zeroes and bit on given
    position – one.

    >>> flip_bit(0b101, 1) # 0b111
    7
    >>> flip_bit(0b101, 0) # 0b100
    4
    """
    return number ^ (1 << position)


def is_bit_set(number: int, position: int) -> bool:
    """
    Is the bit at position set?

    Details: Shift the bit at position to be the first (smallest) bit.
    Then check if the first bit is set by anding the shifted number with 1.

    >>> is_bit_set(0b1010, 0)
    False
    >>> is_bit_set(0b1010, 1)
    True
    >>> is_bit_set(0b1010, 2)
    False
    >>> is_bit_set(0b1010, 3)
    True
    >>> is_bit_set(0b0, 17)
    False
    """
    return ((number >> position) & 1) == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
