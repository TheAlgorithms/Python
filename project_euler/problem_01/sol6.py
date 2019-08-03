"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
"""
from __future__ import print_function

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3


def solution(n):
    """Returns the sum of all the multiples of 3 or 5 below n.
    
    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """

    a = 3
    result = 0
    while a < n:
        if a % 3 == 0 or a % 5 == 0:
            result += a
        elif a % 15 == 0:
            result -= a
        a += 1
    return result


if __name__ == "__main__":
    print(solution(int(raw_input().strip())))
