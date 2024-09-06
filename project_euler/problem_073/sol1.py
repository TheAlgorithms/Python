"""
Project Euler Problem 73: https://projecteuler.net/problem=73

Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size,
we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set
of reduced proper fractions for d ≤ 12,000?
"""

from math import gcd


def slow_solution(max_d: int = 12_000) -> int:
    """
    Returns number of fractions lie between 1/3 and 1/2 in the sorted set
    of reduced proper fractions for d ≤ max_d

    >>> slow_solution(4)
    0

    >>> slow_solution(5)
    1

    >>> slow_solution(8)
    3
    """

    fractions_number = 0
    for d in range(max_d + 1):
        for n in range(d // 3 + 1, (d + 1) // 2):
            if gcd(n, d) == 1:
                fractions_number += 1
    return fractions_number


def solution(max_d: int = 12_000) -> int:
    """
    Returns number of fractions lie between 1/3 and 1/2 in the sorted set
    of reduced proper fractions for d ≤ max_d

    >>> solution(4)
    0

    >>> solution(5)
    1

    >>> solution(8)
    3
    """

    fractions_number = 0
    for d in range(max_d + 1):
        if d % 2 == 0:
            n_start = d // 3 + 2 if (d // 3 + 1) % 2 == 0 else d // 3 + 1
            for n in range(n_start, (d + 1) // 2, 2):
                if gcd(n, d) == 1:
                    fractions_number += 1
        else:
            for n in range(d // 3 + 1, (d + 1) // 2):
                if gcd(n, d) == 1:
                    fractions_number += 1
    return fractions_number


def benchmark() -> None:
    """
    Benchmarks
    """
    # Running performance benchmarks...
    # slow_solution : 21.02750190000006
    # solution      : 15.79036830000041

    from timeit import timeit

    print("Running performance benchmarks...")

    print(f"slow_solution : {timeit('slow_solution()', globals=globals(), number=10)}")
    print(f"solution      : {timeit('solution()', globals=globals(), number=10)}")


if __name__ == "__main__":
    print(f"{solution() = }")
    benchmark()
