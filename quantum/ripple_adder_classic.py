"""Ripple-carry adder simulation using full-adder logic."""

from __future__ import annotations

from quantum.q_full_adder import q_full_adder


def ripple_adder(val1: int, val2: int) -> int:
    """Add two non-negative integers using bitwise full-adder steps.

    Time Complexity: ``O(max(bit_length(val1), bit_length(val2)))``
    Space Complexity: ``O(1)``

    >>> ripple_adder(3, 4)
    7
    >>> ripple_adder(10, 4)
    14
    >>> ripple_adder(-1, 10)
    Traceback (most recent call last):
        ...
    ValueError: val1 and val2 must be non-negative integers
    """
    if val1 < 0 or val2 < 0:
        raise ValueError("val1 and val2 must be non-negative integers")

    carry = 0
    result = 0
    max_bits = max(val1.bit_length(), val2.bit_length(), 1)

    for idx in range(max_bits):
        bit_a = (val1 >> idx) & 1
        bit_b = (val2 >> idx) & 1
        sum_bit, carry = q_full_adder(bit_a, bit_b, carry)
        result |= sum_bit << idx

    if carry:
        result |= carry << max_bits
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
