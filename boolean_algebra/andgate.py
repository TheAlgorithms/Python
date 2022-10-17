""" An AND Gate is a logic gate in boolean algebra which results to false(0)
    if any of the input is 0, and True(1) if  both the inputs are 1.
    """


def and_gate(input_1, input_2):

    return input_1 * input_2


def main():
    print("Truth Table of AND Gate:")
    print("| Input 1 |", " Input 2 |", " Output |")
    print("|      0      |", "     0      |     ", and_gate(0, 0), "     |")
    print("|      0      |", "     1      |     ", and_gate(0, 1), "     |")
    print("|      1      |", "     0      |     ", and_gate(1, 0), "     |")
    print("|      1      |", "     1      |     ", and_gate(1, 1), "     |")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

"""Contributed by Aanya Jain
Wikipedia link for AND GAte: https://en.wikipedia.org/wiki/AND_gate"""
