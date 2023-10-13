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


if __name__ == "__main__":
    print(imply_gate(0, 0))
    print(imply_gate(0, 1))
    print(imply_gate(1, 0))
    print(imply_gate(1, 1))
