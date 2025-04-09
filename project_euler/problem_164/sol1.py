"""
Project Euler Problem 164: https://projecteuler.net/problem=164

Three Consecutive Digital Sum Limit

How many 20 digit numbers n (without any leading zero) exist such that no three
consecutive digits of n have a sum greater than 9?

Brute-force recursive solution with caching of intermediate results.

>>> solution(10)
21838806
"""


def solve(
    digit: int, prev: int, prev2: int, sum_max: int, first: bool, cache: dict[str, int]
) -> int:
    """
    Solve for remaining 'digit' digits, with previous 'prev' number, and
    previous-previous 'prev2' number, total sum of 'sum_max'.
    Pass around 'cache' to store/reuse intermediate results.

    >>> solve(1, 0, 0, 9, True, {})
    9
    >>> solve(1, 0, 0, 9, False, {})
    10
    """
    if digit == 0:
        return 1
    comb = 0
    cache_str = f"{digit},{prev},{prev2}"
    if cache_str in cache:
        return cache[cache_str]
    for v in range(sum_max - prev - prev2 + 1):
        if first and v == 0:
            continue
        comb += solve(digit - 1, v, prev, sum_max, False, cache)
    cache[cache_str] = comb
    return comb


def solution(n_digits: int = 20) -> int:
    """
    Solves the problem for n_digits number of digits.

    >>> solution(2)
    45
    """
    sum_max = 9
    cache: dict[str, int] = {}
    ans = solve(n_digits, 0, 0, sum_max, True, cache)

    return ans


if __name__ == "__main__":
    print(f"{solution(10) = }")
