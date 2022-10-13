""" A NOR Gate is a logic gate in boolean algebra which results to false(0) if any of the input is
   1, and True(1) if  both the inputs are 0.
   Following is the truth table of an NOR Gate:
   | Input 1 | Input 2 |  Output |
   |      0      |     0      |      1      |
   |      0      |     1      |      0      |
   |      1      |     0      |      0      |
   |      1      |     1      |      0      |
"""
"""Following is the code implementation of the NOR Gate"""


def NOR_Gate(input_1, input_2):
    if input_1 == input_2 == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    print("Truth Table of NOR Gate:")
    print("| Input 1 |", " Input 2 |", " Output |")
    print("|      0      |", "     0      |     ", NOR_Gate(0, 0), "     |")
    print("|      0      |", "     1      |     ", NOR_Gate(0, 1), "     |")
    print("|      1      |", "     0      |     ", NOR_Gate(1, 0), "     |")
    print("|      1      |", "     1      |     ", NOR_Gate(1, 1), "     |")

"""Code provided by Akshaj Vishwanathan"""
