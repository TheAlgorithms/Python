"""
Project Euler Problem 197: https://projecteuler.net/problem=197

Given is the function f(x) = ⌊2^30.403243784 - x^2⌋ * 10^(-9)(⌊⌋ is the floor function),
the sequence u_n is defined by u_0 = -1 and u_(n+1) = f(u_n).

Find u_n + u_(n+1) for n = 10^12.
Give your answer with 9 digits after the decimal point.

-----

f(n) starts to alternate between 2 values and converges quickly.

"""

from math import floor


def f(x: float) -> float:
    """
    Computes f(x) = ⌊2^30.403243784 - x^2⌋ * 10^(-9)

    [Doctest]
    >>> f(0)
    -1

    >>> f(3)
    0.002773437

    >>> f(-1)
    0.7100000000000001

    """
    if x == 0:
        return -1
    else:
        return floor(2 ** (30.403243784 - x**2)) * (10 ** (-9))


def solution(n: int = 10**12) -> float:
    """
    Computes u_n + u_(n+1) as defined in the statement

    Compute the first 100000 values of the sequence u
    The sequence converges and alternates between 2 values
    These 2 values can be used to interpolate u_n for larger values of n
    The sum of u_n + u_(n+1) converges for larger values of n

    >>> solution(0)
    -0.29

    >>> solution(1)
    1.711242148

    >>> solution(10)
    1.710098289

    """
    u = -1
    for _i in range(1, min(10**5, n) + 1):
        u = f(u)
    return round(u + f(u), 9)


if __name__ == "__main__":
    print(f"{solution(10) = }")
