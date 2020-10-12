"""
Problem Statement:
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

from itertools import product


def solution() -> int:
    """
    Returns the positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0 using
    itertool product to generate all possible digit combinations 0...9 for the nine "_"
    to fill.

    >>> solution()
    1389019170
    """

    for p in product("0123456789"[::-1], repeat=9):
        squared = int("1{}2{}3{}4{}5{}6{}7{}8{}9{}0".format(*p))

        root_integer = int(squared ** 0.5)

        if root_integer ** 2 == squared:
            return root_integer


if __name__ == "__main__":
    print(solution())
