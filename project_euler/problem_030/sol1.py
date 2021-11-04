""" Problem Statement (Digit Fifth Powers): https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum of fourth
powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their
digits.

9^5 = 59049
59049 * 7 = 413343 (which is only 6 digit number)
So, numbers greater than 999999 are rejected
and also 59049 * 3 = 177147 (which exceeds the criteria of number being 3 digit)
So, number > 999
and hence a number between 1000 and 1000000
"""


def digitsum(s: str) -> int:
    """
    >>> all(digitsum(str(i)) == (1 if i == 1 else 0) for i in range(100))
    True
    """
    i = sum(pow(int(c), 5) for c in s)
    return i if i == int(s) else 0


def solution() -> int:
    return sum(digitsum(str(i)) for i in range(1000, 1000000))


if __name__ == "__main__":
    print(solution())
