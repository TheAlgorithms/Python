"""
Problem:
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers which
is less than N.
"""
from __future__ import print_function

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3


def solution(n):
    """Returns the largest palindrome made from the product of two 3-digit
    numbers which is less than n.
    
    >>> solution(20000)
    19591
    >>> solution(30000)
    29992
    >>> solution(40000)
    39893
    """
    answer = 0
    for i in range(999, 99, -1):  # 3 digit nimbers range from 999 down to 100
        for j in range(999, 99, -1):
            t = str(i * j)
            if t == t[::-1] and i * j < n:
                answer = max(answer, i * j)
    return answer


if __name__ == "__main__":
    print(solution(int(raw_input().strip())))
