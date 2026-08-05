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
    return int(not (input_1 and input_2))


def n_input_nand_gate(inputs: list[int]) -> int:
    """
    Generalization of nand_gate() to support n inputs.
    Calculate NAND of a list of input values.
    Returns 0 only when all inputs are 1, 1 otherwise.

    >>> n_input_nand_gate([1, 0, 1, 1, 0])
    1
    >>> n_input_nand_gate([1, 1, 1, 1, 1])
    0
    >>> n_input_nand_gate([0, 0, 0, 0, 0])
    1
    >>> n_input_nand_gate([1, 0, 0, 0, 0])
    1

    >>> n_input_nand_gate([1, 1])
    0

    >>> n_input_nand_gate([])
    Traceback (most recent call last):
        ...
    ValueError: Input list cannot be empty

    >>> n_input_nand_gate([1])
    Traceback (most recent call last):
        ...
    ValueError: Input list must contain at least two elements

    >>> n_input_nand_gate([2, 1])
    Traceback (most recent call last):
        ...
    ValueError: All inputs must be 0 or 1
    """

    if len(inputs) == 0:
        raise ValueError("Input list cannot be empty")
    if len(inputs) < 2:
        raise ValueError("Input list must contain at least two elements")
    if not all(i in (0, 1) for i in inputs):
        raise ValueError("All inputs must be 0 or 1")

    return int(not all(inputs))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
