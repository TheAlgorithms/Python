"""
Project Euler Problem 164: https://projecteuler.net/problem=164

Three Consecutive Digital Sum Limit

How many 20 digit numbers n (without any leading zero) exist such that no three
consecutive digits of n have a sum greater than 9?

Brute-force recursive solution with caching of intermediate results.
"""


def solve(
    digit: int, prev1: int, prev2: int, sum_max: int, first: bool, cache: dict[str, int]
) -> int:
    """
    Solve for remaining 'digit' digits, with previous 'prev1' digit, and
    previous-previous 'prev2' digit, total sum of 'sum_max'.
    Pass around 'cache' to store/reuse intermediate results.

    >>> solve(digit=1, prev1=0, prev2=0, sum_max=9, first=True, cache={})
    9
    >>> solve(digit=1, prev1=0, prev2=0, sum_max=9, first=False, cache={})
    10
    """
    if digit == 0:
        return 1

    cache_str = f"{digit},{prev1},{prev2}"
    if cache_str in cache:
        return cache[cache_str]

    comb = 0
    for curr in range(sum_max - prev1 - prev2 + 1):
        if first and curr == 0:
            continue

        comb += solve(
            digit=digit - 1,
            prev1=curr,
            prev2=prev1,
            sum_max=sum_max,
            first=False,
            cache=cache,
        )

    cache[cache_str] = comb
    return comb


def solution(n_digits: int = 20) -> int:
    """
    Solves the problem for n_digits number of digits.

    >>> solution(2)
    45
    >>> solution(10)
    21838806
    """
    cache: dict[str, int] = {}
    return solve(digit=n_digits, prev1=0, prev2=0, sum_max=9, first=True, cache=cache)


if __name__ == "__main__":
    print(f"{solution(10) = }")
