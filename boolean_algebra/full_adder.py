"""
A Full Adder is a fundamental combinational circuit in digital logic.
It computes the sum and carry outputs for two input bits and an input carry bit.

Truth Table:
    -----------------------------------------
    | A | B | Cin | Sum | Cout |
    -----------------------------------------
    | 0 | 0 |  0  |  0  |   0   |
    | 0 | 1 |  0  |  1  |   0   |
    | 1 | 0 |  0  |  1  |   0   |
    | 1 | 1 |  0  |  0  |   1   |
    | 0 | 0 |  1  |  1  |   0   |
    | 0 | 1 |  1  |  0  |   1   |
    | 1 | 0 |  1  |  0  |   1   |
    | 1 | 1 |  1  |  1  |   1   |
    -----------------------------------------

Refer:
https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder
"""


def full_adder(a: int, b: int, cin: int) -> tuple[int, int]:
    """
    Compute the sum and carry-out for a Full Adder.

    Args:
        a: First input bit (0 or 1).
        b: Second input bit (0 or 1).
        cin: Carry-in bit (0 or 1).

    Returns:
        A tuple `(sum_bit, carry_out)`.

    >>> full_adder(0, 0, 0)
    (0, 0)
    >>> full_adder(0, 1, 0)
    (1, 0)
    >>> full_adder(1, 0, 0)
    (1, 0)
    >>> full_adder(1, 1, 0)
    (0, 1)
    >>> full_adder(0, 0, 1)
    (1, 0)
    >>> full_adder(1, 1, 1)
    (1, 1)

    Raises:
        ValueError: If any input is not 0 or 1.
    """
    if a not in (0, 1) or b not in (0, 1) or cin not in (0, 1):
        raise ValueError("Inputs must be 0 or 1.")

    # Sum is XOR of the inputs
    sum_bit = a ^ b ^ cin

    # Carry-out is true if any two or more inputs are 1
    carry_out = (a & b) | (b & cin) | (a & cin)

    return sum_bit, carry_out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
