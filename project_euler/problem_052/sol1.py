"""
Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""


def solution():
    """Returns the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and
    6x, contain the same digits.

    >>> solution()
    142857
    """
    i = 1

    while True:
        if (
            sorted(str(i))
            == sorted(str(2 * i))
            == sorted(str(3 * i))
            == sorted(str(4 * i))
            == sorted(str(5 * i))
            == sorted(str(6 * i))
        ):
            return i

        i += 1


if __name__ == "__main__":
    print(solution())
