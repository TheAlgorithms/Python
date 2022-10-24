"""
A XOR Gate is a logic gate in boolean algebra which results to True(1)
if only one of the two inputs is 1, and False(1) if even number
of inputs are 1.
Following is the truth table of a XOR Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    0   |
    |    0    |    1    |    1   |
    |    1    |    0    |    1   |
    |    1    |    1    |    0   |
    ------------------------------

Refer - https://www.geeksforgeeks.org/logic-gates-in-python/

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
    num_ones = 0

    if input_1 != 0:
        num_ones += 1
    
    if input_2 != 0:
        num_ones += 1
    
    return int(num_ones % 2 != 0)


def main() -> None:
    print("Truth Table of XOR Gate:")
    print("|   Input 1   |  Input 2  | Output |")
    print(f"|      0      |    0      |  {xor_gate(0, 0)}     |")
    print(f"|      0      |    1      |  {xor_gate(0, 1)}     |")
    print(f"|      1      |    0      |  {xor_gate(1, 0)}     |")
    print(f"|      1      |    1      |  {xor_gate(1, 1)}     |")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
