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

    sum = 0
    terms = (n - 1) // 3
    sum += ((terms) * (6 + (terms - 1) * 3)) // 2  # sum of an A.P.
    terms = (n - 1) // 5
    sum += ((terms) * (10 + (terms - 1) * 5)) // 2
    terms = (n - 1) // 15
    sum -= ((terms) * (30 + (terms - 1) * 15)) // 2
    return sum


if __name__ == "__main__":
    print(solution(int(raw_input().strip())))
