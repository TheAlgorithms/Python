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

""" Euclidean GCD Algorithm """


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


""" Using the property lcm*gcd of two numbers = product of them """


def lcm(x, y):
    return (x * y) // gcd(x, y)


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
    g = 1
    for i in range(1, n + 1):
        g = lcm(g, i)
    return g


if __name__ == "__main__":
    print(solution(int(raw_input().strip())))
