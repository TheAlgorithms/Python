"""
A XOR Gate is a logic gate in boolean algebra which results to true(1)
    only when the two input values are different, and false(0) if the inputs are equal.
   Following is the truth table of an XOR Gate:
   | Input 1 | Input 2 |  Output |
   |      0      |     0      |      0      |
   |      0      |     1      |      1      |
   |      1      |     0      |      1      |
   |      1      |     1      |      0      |

Following is the code implementation of the XOR Gate
"""


def xor_gate(input_1: int, input_2: int) -> int:
    """
    >>> xor_gate(0, 0)
    0
    >>> xor_gate(0, 1)
    1
    >>> xor_gate(1, 0)
    1
    >>> xor_gate(1, 1)
    0
    """
    return int(input_1 != input_2)


def main() -> None:
    print("Truth Table of XOR Gate:")
    print("| Input 1     |", " Input 2    |", " Output     |")
    print(f"|      0      |      0      |      {xor_gate(0,0)}      |")
    print(f"|      0      |      1      |      {xor_gate(0,1)}      |")
    print(f"|      1      |      0      |      {xor_gate(1,0)}      |")
    print(f"|      1      |      1      |      {xor_gate(1,1)}      |")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
