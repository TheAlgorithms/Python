"""
Problem:
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible(divisible with no
remainder) by all of the numbers from 1 to N?
"""
from __future__ import print_function

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3


def solution(n):
    """Returns the smallest positive number that is evenly divisible(divisible
    with no remainder) by all of the numbers from 1 to n.
    
    >>> solution(10)
    2520
    >>> solution(15)
    360360
    >>> solution(20)
    232792560
    >>> solution(22)
    232792560
    """
    i = 0
    while 1:
        i += n * (n - 1)
        nfound = 0
        for j in range(2, n):
            if i % j != 0:
                nfound = 1
                break
        if nfound == 0:
            if i == 0:
                i = 1
            return i
            break


if __name__ == "__main__":
    print(solution(int(raw_input().strip())))
