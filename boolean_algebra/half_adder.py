"""
A Half Adder is a basic combinational circuit in digital logic.
It computes the sum and carry outputs for two input bits.

Truth Table:
    -------------------------
    | Input A | Input B | Sum | Carry |
    -------------------------
    |    0    |    0    |  0  |   0   |
    |    0    |    1    |  1  |   0   |
    |    1    |    0    |  1  |   0   |
    |    1    |    1    |  0  |   1   |
    -------------------------

Refer - https://en.wikipedia.org/wiki/Adder_(electronics)#Half_adder
"""


def half_adder(a: int, b: int) -> tuple[int, int]:
    """
    Compute the sum and carry for a Half Adder.

    >>> half_adder(0, 0)
    (0, 0)
    >>> half_adder(0, 1)
    (1, 0)
    >>> half_adder(1, 0)
    (1, 0)
    >>> half_adder(1, 1)
    (0, 1)

    Raises:
        ValueError: If inputs are not 0 or 1.
    """
    if a not in (0, 1) or b not in (0, 1):
        raise ValueError("Inputs must be 0 or 1")

    sum_bit = a ^ b
    carry_bit = a & b
    return sum_bit, carry_bit


if __name__ == "__main__":
    import doctest

    doctest.testmod()
