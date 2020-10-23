"""
Project Euler problem 30: https://projecteuler.net/problem=30
Surprisingly there are only three numbers that can be written as the sum of fourth
powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of
their digits.

Solution:
This solution is almost the same as sol1.py written by @cclaus.
The only main difference is that we pre-calculate a dict that maps digits to their
fifth powers.
"""


from typing import Dict

digit_5: Dict[str, int] = {
    "0": 0,
    "1": 1,
    "2": 32,
    "3": 243,
    "4": 1024,
    "5": 3125,
    "6": 7776,
    "7": 16807,
    "8": 32768,
    "9": 59049,
}


def sum_digit_5_powers(n):
    """
    Return the sum of the fifth powers of the digits of n.
    >>> sum_digit_5_powers(100)
    1
    >>> sum_digit_5_powers(12345)
    4425
    >>> sum_digit_5_powers(12345789)
    113049
    """
    return sum(map(digit_5.get, str(n)))


def solution():
    """
    Return the sum of all numbers that are equal to the sum of
    the fifth powers of their digits.
    """
    ret = 0
    for n in range(2, 1000000):
        if n == sum_digit_5_powers(n):
            ret += n
    return ret


if __name__ == "__main__":
    print(f"{solution() = }")
