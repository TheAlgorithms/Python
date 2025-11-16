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


def half_adder(input_a: int, input_b: int) -> tuple[int, int]:
    """
    Compute the sum and carry for a Half Adder.

    Args:
        input_a: First input bit (0 or 1).
        input_b: Second input bit (0 or 1).

    Returns:
        A tuple `(sum_bit, carry_bit)`.

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
    if input_a not in (0, 1) or input_b not in (0, 1):
        raise ValueError("Inputs must be 0 or 1")

    sum_bit = input_a ^ input_b
    carry_bit = input_a & input_b
    return sum_bit, carry_bit


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
     