""" A NOR Gate is a logic gate in boolean algebra which results to false(0)
    if any of the input is 1, and True(1) if  both the inputs are 0.
   Following is the truth table of an NOR Gate:
   | Input 1 | Input 2 |  Output |
   |      0      |     0      |      1      |
   |      0      |     1      |      0      |
   |      1      |     0      |      0      |
   |      1      |     1      |      0      |
"""
"""Following is the code implementation of the NOR Gate"""


def nor_gate(input_1: int, input_2: int) -> int:
    """
    >>> nor_gate(0, 0)
    1
    >>> nor_gate(0, 1)
    0
    >>> nor_gate(1, 0)
    0
    >>> nor_gate(1, 1)
    0
    >>> nor_gate(0.0, 0.0)
    1
    >>> nor_gate(0, -7)
    0
    """
    return int(input_1 == input_2 == 0)


def main() -> None:
    print("Truth Table of NOR Gate:")
    print("| Input 1 |", " Input 2 |", " Output |")
    print("|      0      |", "     0      |     ", nor_gate(0, 0), "     |")
    print("|      0      |", "     1      |     ", nor_gate(0, 1), "     |")
    print("|      1      |", "     0      |     ", nor_gate(1, 0), "     |")
    print("|      1      |", "     1      |     ", nor_gate(1, 1), "     |")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
"""Code provided by Akshaj Vishwanathan"""
"""Reference: https://www.geeksforgeeks.org/logic-gates-in-python/"""
