"""
Problem 100: https://projecteuler.net/problem=100
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain

References:
https://mathworld.wolfram.com/DiophantineEquation.html
https://www.alpertron.com.ar/QUAD.HTM
"""


def solution(L):
    """
    let b = num of blue discs, L = total num of discs
    we get, b(b-1)/n(n-1) = 1/2
    => 2b(b-1) = n(n-1)
    => 2b^2 - 2b - n^2 + n = 0
    which, is a diophantine equation and solving it to get recursive solution
    using this online solver https://www.alpertron.com.ar/QUAD.HTM we get,

    b = 3b + 2n -2
    n = 4b + 3n -3
    as the two recursive solutions

    Examples:
    >>> solution(21)
    15
    >>> solution(120)
    85
    >>> solution(10**12)
    756872327473
    """
    b, n = 3, 4
    while n < L:
        b, n = 3 * b + 2 * n - 2, 4 * b + 3 * n - 3

    return b
