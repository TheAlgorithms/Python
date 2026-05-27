"""
An AND Gate is a logic gate in boolean algebra which results to 1 (True) if all the
inputs are 1 (True), and 0 (False) otherwise.

Following is the truth table of a Two Input AND Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    0   |
    |    0    |    1    |    0   |
    |    1    |    0    |    0   |
    |    1    |    1    |    1   |
    ------------------------------

Refer - https://www.geeksforgeeks.org/logic-gates/
"""


def and_gate(input_1: int, input_2: int) -> int:
    """
    Calculate AND of two binary input values.

    >>> and_gate(0, 0)
    0
    >>> and_gate(0, 1)
    0
    >>> and_gate(1, 1)
    1
    >>> and_gate(2, 1)
    Traceback (most recent call last):
        ...
    ValueError: Both inputs must be 0 or 1
    >>> and_gate(0, "1")
    Traceback (most recent call last):
        ...
    TypeError: Both inputs must be integers
    """
    # Type validation
    if not isinstance(input_1, int) or not isinstance(input_2, int):
        raise TypeError("Both inputs must be integers")

    # Value validation
    if input_1 not in (0, 1) or input_2 not in (0, 1):
        raise ValueError("Both inputs must be 0 or 1")

    return input_1 & input_2


def n_input_and_gate(inputs: list[int]) -> int:
    """
    Calculate AND of a list of binary input values.

    >>> n_input_and_gate([1, 1, 1, 1, 1])
    1
    >>> n_input_and_gate([1, 0, 1, 1, 0])
    0
    >>> n_input_and_gate([])
    Traceback (most recent call last):
        ...
    ValueError: Input list cannot be empty
    >>> n_input_and_gate([1, 2, 1])
    Traceback (most recent call last):
        ...
    ValueError: All inputs in the list must be 0 or 1
    >>> n_input_and_gate([1, "1"])
    Traceback (most recent call last):
        ...
    TypeError: All inputs in the list must be integers
    """
    # Type validation for the list itself
    if not isinstance(inputs, list):
        raise TypeError("Input must be a list")

    # Edge case validation for an empty list
    if not inputs:
        raise ValueError("Input list cannot be empty")

    # Type and value validation for items within the list
    for item in inputs:
        if not isinstance(item, int):
            raise TypeError("All inputs in the list must be integers")
        if item not in (0, 1):
            raise ValueError("All inputs in the list must be 0 or 1")

    return int(all(inputs))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
