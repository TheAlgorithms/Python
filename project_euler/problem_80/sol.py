import decimal
from math import floor

"""
Square root digital expansion
It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred
decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred
decimal digits for all the irrational square roots.

>>> solution()
40886
"""


def solution() -> int:
    """Return the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

    >>> solution()
    40886
    """

    n = 100
    p = 100
    tot = 0

    for i in range(1, n + 1):
        sm = 0
        decimal.getcontext().prec = p + 10
        fv = decimal.Decimal(i).sqrt()
        if fv - floor(fv) == 0:
            continue
        else:
            fv = str(fv).replace(".", "")
            fv = fv[0:p]
            fv = int(fv)
            while fv != 0:
                sm = sm + (fv % 10)
                fv = fv // 10
            tot += sm
    return tot


if __name__ == "__main__":
    res=solution()
    print(res)
