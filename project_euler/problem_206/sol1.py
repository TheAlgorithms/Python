"""
Project Euler Problem 206: https://projecteuler.net/problem=206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

To find the solution all possible permutations to fill the pattern 1_2_3_4_5_6_7_8_9_0
with the digits 0...9 are checked until the check for the correct solution is true.
The check is done by converting the string into an integer, taking its root square,
converted also into an integer and then check if squaring again equals the first
integer. To generate the permutations 'itertools.product' is used

"""

from itertools import product


def solution() -> int:
    """
    Returns the positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0 using
    itertool product to generate all possible digit combinations 0...9 for the nine "_"
    to fill.

    """

    # iterate through all permutations
    # (starting from 9*"9" to speed up finding solution)
    for permutation in product("0123456789"[::-1], repeat=9):
        # form string and convert to int
        squared = int("1{}2{}3{}4{}5{}6{}7{}8{}9{}0".format(*permutation))

        # integer of square root
        root_integer = int(squared ** 0.5)

        # check if integer of square root is equal to original integer
        if root_integer ** 2 == squared:
            return root_integer


if __name__ == "__main__":
    print(f"{solution() = }")
