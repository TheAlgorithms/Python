"""
A XOR Gate is a logic gate in boolean algebra which results to 1 (True) if only one of
the two inputs is 1, and 0 (False) if an even number of inputs are 1.
Following is the truth table of a XOR Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    0   |
    |    0    |    1    |    1   |
    |    1    |    0    |    1   |
    |    1    |    1    |    0   |
    ------------------------------

Refer - https://www.geeksforgeeks.org/logic-gates-in-python/
"""


def xor_gate(input_1: int, input_2: int) -> int:
    """
    calculate xor of the input values

    >>> xor_gate(0, 0)
    0
    >>> xor_gate(0, 1)
    1
    >>> xor_gate(1, 0)
    1
    >>> xor_gate(1, 1)
    0
    """
    return (input_1, input_2).count(0) % 2


def test_xor_gate() -> None:
    """
    Tests the xor_gate function
    """
    assert xor_gate(0, 0) == 0
    assert xor_gate(0, 1) == 1
    assert xor_gate(1, 0) == 1
    assert xor_gate(1, 1) == 0


if __name__ == "__main__":
    print(xor_gate(0, 0))
    print(xor_gate(0, 1))
