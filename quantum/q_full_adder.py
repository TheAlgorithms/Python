"""Full-adder simulation inspired by reversible/quantum circuits."""

from __future__ import annotations


def q_full_adder(bit_a: int, bit_b: int, carry_in: int) -> tuple[int, int]:
    """Add two one-bit operands plus input carry.

    Returns ``(sum_bit, carry_out)``.

    Time Complexity: ``O(1)``
    Space Complexity: ``O(1)``

    >>> q_full_adder(0, 0, 0)
    (0, 0)
    >>> q_full_adder(1, 1, 0)
    (0, 1)
    >>> q_full_adder(1, 1, 1)
    (1, 1)
    """
    if bit_a not in (0, 1) or bit_b not in (0, 1) or carry_in not in (0, 1):
        raise ValueError("all inputs must be 0 or 1")

    sum_bit = bit_a ^ bit_b ^ carry_in
    carry_out = (bit_a & bit_b) | (bit_a & carry_in) | (bit_b & carry_in)
    return sum_bit, carry_out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
