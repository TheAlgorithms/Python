"""
A NAND Gate is a logic gate in boolean algebra which results to 0 (False) if any
of the inputs is 1, and 1 (True) otherwise. It's similar to adding
a NOT gate along with an AND gate.
Following is the truth table of a NAND Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    1   |
    |    0    |    1    |    1   |
    |    1    |    0    |    1   |
    |    1    |    1    |    0   |
    ------------------------------
Refer - https://www.geeksforgeeks.org/logic-gates-in-python/
"""


def nand_gate(*args) -> int:
    """
    Calculate NAND of the input values
    >>> nand_gate(0, 0)
    1
    >>> nand_gate(0, 1)
    1
    >>> nand_gate(1, 0)
    1
    >>> nand_gate(1, 1)
    0
    """
    if all(isinstance(arg, int) for arg in args):
        return int(any(arg == 0 for arg in args))
    else:
        raise TypeError("Input values must be integers")


def test_nand_gate() -> None:
    """
    Tests the nand_gate function
    """
    assert nand_gate(0, 0) == 1
    assert nand_gate(0, 1) == 1
    assert nand_gate(1, 0) == 1
    assert nand_gate(1, 1) == 0
    assert nand_gate(1, 1, 1) == 0
    assert nand_gate(0, 1, 1) == 0
    assert nand_gate(0, 0, 0) == 1


if __name__ == "__main__":
    print(nand_gate(0, 0))
    print(nand_gate(0, 1))
    print(nand_gate(1, 0))
    print(nand_gate(1, 1))
    print(nand_gate(1, 1, 1))
    print(nand_gate(0, 1, 1))
    print(nand_gate(0, 0, 0))
