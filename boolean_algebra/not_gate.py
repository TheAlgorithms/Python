"""
A NOT Gate is a logic gate in boolean algebra which results to 0 (False) if the
input is high, and 1 (True) if the input is low.
Following is the truth table of a XOR Gate:
    ------------------------------
    | Input   |  Output |
    ------------------------------
    |    0    |    1    |
    |    1    |    0    |
    ------------------------------
Refer - https://www.geeksforgeeks.org/logic-gates-in-python/
"""


def not_gate(input_1: int) -> int:
    """
    Calculate NOT of the input values
    >>> not_gate(0)
    1
    >>> not_gate(1)
    0
    """

    return 1 if input_1 == 0 else 0


def test_not_gate() -> None:
    """
    Tests the not_gate function
    """
    assert not_gate(0) == 1
    assert not_gate(1) == 0


if __name__ == "__main__":
    print(not_gate(0))
    print(not_gate(1))
