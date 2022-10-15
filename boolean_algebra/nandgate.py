""" A NAND Gate is a logic gate in boolean algebra which results to false(1)
    if any of the input is 0, and True(1) if  both the inputs are 1.
   Following is the truth table of an NAND Gate:
   | Input 1 | Input 2 |  Output |
   |      0      |     0      |      1      |
   |      0      |     1      |      1      |
   |      1      |     0      |      1      |
   |      1      |     1      |      0      |
"""
"""Following is the code implementation of the NAND Gate"""


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
    """
    if input_1 == input_2 == 1:
        return 0
    else:
        return 1


def main() -> None:
    print("Truth Table of NAND Gate:")
    print("| Input 1 |", " Input 2 |", " Output |")
    print("|      0      |", "     0      |     ", nand_gate(0, 0), "     |")
    print("|      0      |", "     1      |     ", nand_gate(0, 1), "     |")
    print("|      1      |", "     0      |     ", nand_gate(1, 0), "     |")
    print("|      1      |", "     1      |     ", nand_gate(1, 1), "     |")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
"""Code provided by Janith Herath"""
"""Reference: https://www.geeksforgeeks.org/logic-gates-in-python/"""
