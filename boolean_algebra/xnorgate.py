""" An XNOR Gate is a logic gate in boolean algebra which results to False(0)
    if both inputs are different, and True(1) if both inputs are the same.
   Following is the truth table of an XNOR Gate:
   |   Input 1   |   Input 2   |    Output   |
   |      0      |      0      |      1      |
   |      0      |      1      |      0      |
   |      1      |      0      |      0      |
   |      1      |      1      |      1      |

The XNOR gate resembles the A <=> B relationship in Mathematical Logic
Following is the code implementation of the XNOR Gate"""


def xnor_gate(input_1: int, input_2: int) -> int:
    """
    >>> xnor_gate(0, 0)
    1
    >>> xnor_gate(0, 1)
    0
    >>> xnor_gate(1, 0)
    0
    >>> xnor_gate(1, 1)
    1
    >>> xnor_gate(0.0, 0.0)
    1
    >>> xnor_gate(0, -7)
    0
    """
    return int(input_1 == input_2)


def main() -> None:
    print("Truth Table of XNOR Gate:")
    print(f"|   Input 1   |   Input 2   |   Output   |")
    print(f"|      0      |      0      |      {xnor_gate(0, 0)}      |")
    print(f"|      0      |      1      |      {xnor_gate(0, 1)}      |")
    print(f"|      1      |      0      |      {xnor_gate(1, 0)}      |")
    print(f"|      1      |      1      |      {xnor_gate(1, 1)}      |")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

"""Code provided by Divyajeet Singh (Github: divyajeettt)"""
"""Reference: nor_gate.py by Akshaj Vishwanathan"""
