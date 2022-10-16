"""
The NAND gate (negated AND) gives an output of 0 if both inputs
are 1, it gives 1 otherwise.

Below is the truth table for NAND gate.

| Input 1 | Input 2 | Output |
| ------- | ------- | ------ |
|    0    |    0    |   1    |
|    0    |    1    |   1    |
|    1    |    0    |   1    |
|    1    |    1    |   0    |

Code By: @rajatshenoi
"""


def nand_gate(input1: int, input2: int) -> int:
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
    1
    """

    if input1 == input2 == 1:
        return 0
    return 1


def main() -> None:
    print("Truth table of NAND Gate:")
    print("| Input 1 | Input 2 | Output |")
    print("|      0      |", "     0      |     ", nand_gate(0, 0), "     |")
    print("|      0      |", "     1      |     ", nand_gate(0, 1), "     |")
    print("|      1      |", "     0      |     ", nand_gate(1, 0), "     |")
    print("|      1      |", "     1      |     ", nand_gate(1, 1), "     |")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

"""
More information on NAND gate: https://en.wikipedia.org/wiki/NAND_gate
"""
