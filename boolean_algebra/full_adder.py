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


def full_adder(input_a: int, input_b: int, carry_in: int) -> tuple[int, int]:
    """
    Compute the sum and carry-out for a Full Adder.

    Args:
        input_a: First input bit (0 or 1).
        input_b: Second input bit (0 or 1).
        carry_in: Carry-in bit (0 or 1).

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
    if input_a not in (0, 1) or input_b not in (0, 1) or carry_in not in (0, 1):
        raise ValueError("Inputs must be 0 or 1.")

    # Sum is XOR of the inputs
    sum_bit = input_a ^ input_b ^ carry_in

    # Carry-out is true if any two or more inputs are 1
    carry_out = (input_a & input_b) | (input_b & carry_in) | (input_a & carry_in)

    return sum_bit, carry_out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
