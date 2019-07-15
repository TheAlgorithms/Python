"""
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""

from math import ceil

try:
    xrange  # Python 2
except NameError:
    xrange = range  # Python 3


def diagonal_sum(n):
    """Returns the sum of the numbers on the diagonals in a n by n spiral
    formed in the same way.

    >>> diagonal_sum(1001)
    669171001
    >>> diagonal_sum(500)
    82959497
    >>> diagonal_sum(100)
    651897
    >>> diagonal_sum(50)
    79697
    >>> diagonal_sum(10)
    537
    """
    total = 1

    for i in xrange(1, int(ceil(n / 2.0))):
        odd = 2 * i + 1
        even = 2 * i
        total = total + 4 * odd ** 2 - 6 * even

    return total


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(diagonal_sum(1001))
    else:
        try:
            n = int(sys.argv[1])
            print(diagonal_sum(n))
        except ValueError:
            print("Invalid entry - please enter a number")
