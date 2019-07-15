# -*- coding: utf-8 -*-
"""
Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
from __future__ import print_function

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3


def one_pence():
    return 1


def two_pence(x):
    return 0 if x < 0 else two_pence(x - 2) + one_pence()


def five_pence(x):
    return 0 if x < 0 else five_pence(x - 5) + two_pence(x)


def ten_pence(x):
    return 0 if x < 0 else ten_pence(x - 10) + five_pence(x)


def twenty_pence(x):
    return 0 if x < 0 else twenty_pence(x - 20) + ten_pence(x)


def fifty_pence(x):
    return 0 if x < 0 else fifty_pence(x - 50) + twenty_pence(x)


def one_pound(x):
    return 0 if x < 0 else one_pound(x - 100) + fifty_pence(x)


def two_pound(x):
    return 0 if x < 0 else two_pound(x - 200) + one_pound(x)


def solution(n):
    """Returns the number of different ways can £n be made using any number of
    coins?

    >>> solution(500)
    6295434
    >>> solution(200)
    73682
    >>> solution(50)
    451
    >>> solution(10)
    11
    """
    return two_pound(n)


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
