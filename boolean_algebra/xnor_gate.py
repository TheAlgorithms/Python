"""
A XNOR Gate is a logic gate in boolean algebra which results to 0 (False) if both the
inputs are different, and 1 (True), if the inputs are same.
It's similar to adding a NOT gate to an XOR gate

Following is the truth table of a XNOR Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    1   |
    |    0    |    1    |    0   |
    |    1    |    0    |    0   |
    |    1    |    1    |    1   |
    ------------------------------
Refer - https://www.geeksforgeeks.org/logic-gates-in-python/
"""


def xnor_gate(input_1: int, input_2: int) -> int:
    """
    Calculate XOR of the input values
    >>> xnor_gate(0, 0)
    1
    >>> xnor_gate(0, 1)
    0
    >>> xnor_gate(1, 0)
    0
    >>> xnor_gate(1, 1)
    1
    """
    return 1 if input_1 == input_2 else 0


def test_xnor_gate() -> None:
    """
    Tests the xnor_gate function
    """
    assert xnor_gate(0, 0) == 1
    assert xnor_gate(0, 1) == 0
    assert xnor_gate(1, 0) == 0
    assert xnor_gate(1, 1) == 1


if __name__ == "__main__":
    print(xnor_gate(0, 0))
    print(xnor_gate(0, 1))
    print(xnor_gate(1, 0))
    print(xnor_gate(1, 1))
