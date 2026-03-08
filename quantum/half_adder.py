"""Half-adder simulation based on quantum-logic intuition."""

from __future__ import annotations


def half_adder(bit_a: int, bit_b: int) -> tuple[int, int]:
    """Add two one-bit operands.

    Returns ``(sum_bit, carry_bit)``.

    Time Complexity: ``O(1)``
    Space Complexity: ``O(1)``

    >>> half_adder(0, 0)
    (0, 0)
    >>> half_adder(1, 1)
    (0, 1)
    >>> half_adder(1, 0)
    (1, 0)
    """
    if bit_a not in (0, 1) or bit_b not in (0, 1):
        raise ValueError("bit_a and bit_b must be 0 or 1")

    sum_bit = bit_a ^ bit_b
    carry_bit = bit_a & bit_b
    return sum_bit, carry_bit


if __name__ == "__main__":
    import doctest

    doctest.testmod()
