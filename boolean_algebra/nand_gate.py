"""
A NAND Gate is a logic gate in boolean algebra which results to 0 (False) if both
the inputs are 1, and 1 (True) otherwise. It's similar to adding
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


def nand_gate(input_1: int, input_2: int) -> int:
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
    return int((input_1, input_2).count(0) != 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
