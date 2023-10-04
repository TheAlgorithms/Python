"""
An OR Gate is a logic gate in boolean algebra which results to 0 (False) if both the
inputs are 0, and 1 (True) otherwise.
Following is the truth table of an AND Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    0   |
    |    0    |    1    |    1   |
    |    1    |    0    |    1   |
    |    1    |    1    |    1   |
    ------------------------------
Refer - https://www.geeksforgeeks.org/logic-gates-in-python/
"""


def or_gate(input_1: int, input_2: int) -> int:
    """
    Calculate OR of the input values
    >>> or_gate(0, 0)
    0
    >>> or_gate(0, 1)
    1
    >>> or_gate(1, 0)
    1
    >>> or_gate(1, 1)
    1
    """
    return int((input_1, input_2).count(1) != 0)


def test_or_gate() -> None:
    """
    Tests the or_gate function
    """
    assert or_gate(0, 0) == 0
    assert or_gate(0, 1) == 1
    assert or_gate(1, 0) == 1
    assert or_gate(1, 1) == 1


if __name__ == "__main__":
    print(or_gate(0, 1))
    print(or_gate(1, 0))
    print(or_gate(0, 0))
    print(or_gate(1, 1))
