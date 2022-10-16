""" A NAND Gate is a logic gate in boolean algebra which results to False(0)
    if both the inputs are 1, and True(1) if any of the input is 0.
   Following is the truth table of a NAND Gate:
   |   Input 1   |   Input 2   |    Output   |
   |      0      |      0      |      1      |
   |      0      |      1      |      1      |
   |      1      |      0      |      1      |
   |      1      |      1      |      0      |

Following is the code implementation of the NAND Gate"""


def nand_gate(input_1: int, input_2: int) -> int:
    """
    >>> nand_gate(0, 0)
    1
    >>> nand_gate(0, 1)
    1
    >>> nand_gate(1, 0)
    1
    >>> nand_gate(1, 1)
    0
    >>> nand_gate(0.0, 0.0)
    1
    >>> nand_gate(0, -7)
    0
    """
    return 1 - int(input_1 == input_2 == 1)


def main() -> None:
    print("Truth Table of NAND Gate:")
    print(f"|   Input 1   |   Input 2   |   Output   |")
    print(f"|      0      |      0      |      {nand_gate(0, 0)}      |")
    print(f"|      0      |      1      |      {nand_gate(0, 1)}      |")
    print(f"|      1      |      0      |      {nand_gate(1, 0)}      |")
    print(f"|      1      |      1      |      {nand_gate(1, 1)}      |")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

"""Code provided by Divyajeet Singh (Github: divyajeettt)"""
"""Reference: nor_gate.py by Akshaj Vishwanathan"""
