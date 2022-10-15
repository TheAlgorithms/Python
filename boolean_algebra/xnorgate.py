""" A XNOR Gate is a logic gate in boolean algebra which results to false(0)
    if both the inputs are different and results to true(1) if both the inputs are same.
   Following is the truth table of an XNOR Gate:
   | Input 1 | Input 2 |  Output |
   |      0      |     0      |      1      |
   |      0      |     1      |      0      |
   |      1      |     0      |      0      |
   |      1      |     1      |      1      |
"""
"""Following is the code implementation of the XNOR Gate"""


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
    """
    return int((not(input_1 != input_2)))

def main() -> None:
    print("Truth Table of XNOR Gate:")
    print("| Input 1     |", " Input 2    |", " Output     |")
    print("|      0      |", "     0      |     ", xnor_gate(0, 0), "     |")
    print("|      0      |", "     1      |     ", xnor_gate(0, 1), "     |")
    print("|      1      |", "     0      |     ", xnor_gate(1, 0), "     |")
    print("|      1      |", "     1      |     ", xnor_gate(1, 1), "     |")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()