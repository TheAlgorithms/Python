"""
An IMPLY Gate is a logic gate in boolean algebra which results to 1 if
either input 1 is 0, or if input 1 is 1, then the output is 1 only if input 2 is 1.
It is true if input 1 implies input 2.

Following is the truth table of an IMPLY Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    1   |
    |    0    |    1    |    1   |
    |    1    |    0    |    0   |
    |    1    |    1    |    1   |
    ------------------------------

Refer - https://en.wikipedia.org/wiki/IMPLY_gate
"""


def imply_gate(input_1: int, input_2: int) -> int:
    """
    Calculate IMPLY of the input values

    >>> imply_gate(0, 0)
    1
    >>> imply_gate(0, 1)
    1
    >>> imply_gate(1, 0)
    0
    >>> imply_gate(1, 1)
    1
    """
    return int(input_1 == 0 or input_2 == 1)


def recursive_imply_list(input_list: list[int]) -> int:
    """
    Recursively calculates the implication of a list.
    Strictly the implication is applied consecutively left to right:
    ( (a -> b) -> c ) -> d ...

    >>> recursive_imply_list([])
    Traceback (most recent call last):
        ...
    ValueError: Input list must contain at least two elements
    >>> recursive_imply_list([0])
    Traceback (most recent call last):
        ...
    ValueError: Input list must contain at least two elements
    >>> recursive_imply_list([1])
    Traceback (most recent call last):
        ...
    ValueError: Input list must contain at least two elements
    >>> recursive_imply_list([0, 0])
    1
    >>> recursive_imply_list([0, 1])
    1
    >>> recursive_imply_list([1, 0])
    0
    >>> recursive_imply_list([1, 1])
    1
    >>> recursive_imply_list([0, 0, 0])
    0
    >>> recursive_imply_list([0, 0, 1])
    1
    >>> recursive_imply_list([0, 1, 0])
    0
    >>> recursive_imply_list([0, 1, 1])
    1
    >>> recursive_imply_list([1, 0, 0])
    1
    >>> recursive_imply_list([1, 0, 1])
    1
    >>> recursive_imply_list([1, 1, 0])
    0
    >>> recursive_imply_list([1, 1, 1])
    1
    """
    if len(input_list) < 2:
        raise ValueError("Input list must contain at least two elements")
    first_implication = imply_gate(input_list[0], input_list[1])
    if len(input_list) == 2:
        return first_implication
    new_list = [first_implication, *input_list[2:]]
    return recursive_imply_list(new_list)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
