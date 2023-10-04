"""
Project Euler Problem 551: https://projecteuler.net/problem=551

Let a(0), a(1),... be an integer sequence defined by:
     a(0) = 1
     for n >= 1, a(n) is the sum of the digits of all preceding terms

The sequence starts with 1, 1, 2, 4, 8, ...
You are given a(10^6) = 31054319.

Find a(10^15)

DISCLAIMER

The statement of the problem in the web is wrong, for n= 6 the solutions is 32 instead of 23 as it is presented

"""


def solution(n: int = 10**15) -> int:
    """
    if we evaluate the  sequence we can see than

    for n = 0 solution is 1 by default
    then n = 1 solution is 1 thats is equal to 2⁰
    for n = 2 solution is 2 thats is equal to 2¹
    for n = 3 solution is 4 thats is equal to 2²
    for n = 4 solution is 8 thats is equal to 2³

    and so long, then every value for n > 1 its equals to 2^n-1
    ...
    >>> solution(10)
    512
    """

    ...
    # calculations
    ...

    return 1 if (n == 0) else 2 ** (n - 1)


if __name__ == "__main__":
    print(f"{solution() = }")
