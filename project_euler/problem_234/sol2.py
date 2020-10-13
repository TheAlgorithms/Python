"""
For an integer n ≥ 4, we define the lower prime square root of n, denoted by lps(n), as
the largest prime ≤ √n and the upper prime square root of n, ups(n), as the smallest
prime ≥ √n.

So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) = 37.
Let us call an integer n ≥ 4 semidivisible, if one of lps(n) and ups(n) divides n,
but not both.

The sum of the semidivisible numbers not exceeding 15 is 30, the numbers are 8,
10 and 12.
15 is not semidivisible because it is a multiple of both lps(15) = 3 and ups(15) = 5.
As a further example, the sum of the 92 semidivisible numbers up to 1000 is 34825.

What is the sum of all semidivisible numbers not exceeding 999966663333?
"""


from __future__ import annotations

import itertools
from math import ceil
from typing import Iterator


def sieve(limit: int) -> Iterator[int]:
    """
    Return an iterable of all the primes less than or equal to limit in ascending order.
    >>> list(sieve(5))
    [2, 3, 5]
    >>> list(sieve(50))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    primes = [False for _ in range(limit + 1)]
    primes[2] = True
    primes[3] = True
    for i in range(3, limit + 1, 2):
        primes[i] = True
    for i in range(3, limit + 1, 2):
        if not primes[i]:
            continue
        for j in range(i * i, limit + 1, i):
            primes[j] = False

    return itertools.compress(itertools.count(), primes)


def pairwise(iterable: Iterator[int]) -> Iterator[tuple]:
    """
    Returns an iterator of paired items, overlapping, from the original.
    Taken from the list of itertools recipes at
    https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.pairwise
    >>> list(pairwise([1,2,3,4]))
    [(1, 2), (2, 3), (3, 4)]
    >>> list(pairwise([2,3,5,7,11]))
    [(2, 3), (3, 5), (5, 7), (7, 11)]
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def arithmetic_sum(start: int, end: int, step: int) -> int:
    """
    Equivalent to sum(range(start, end, step)).
    >>> arithmetic_sum(5,55,6)
    261
    >>> arithmetic_sum(1,10,1)
    45
    """
    n = (end - start - 1) // step + 1
    return (n * start) + (n * (n - 1) // 2) * step


def sum_mults_in_range(start: int, end: int, prime: int) -> int:
    """
    Equivalent to sum(num for num in range(start, end, prime) if num % prime == 0)
    >>> sum_mults_in_range(170,289,13)
    2106
    >>> sum_mults_in_range(170,289,14)
    1848
    """
    start = ceil(start / prime) * prime
    return arithmetic_sum(start, end, prime)


def solution(limit: int = 999966663333) -> int:
    """
    Return the sum of all semidivisible numbers not exceeding limit.
    >>> solution(1000)
    34825
    >>> solution(10000)
    1134942
    >>> solution(100000)
    36393008
    """
    ret = 0
    pr_lim = int(limit ** 0.5) + 10

    for prime1, prime2 in pairwise(sieve(pr_lim)):
        lower = prime1 * prime1
        upper = prime2 * prime2
        # prime1 = lps(n) for lower <= n < upper
        # prime2 = ups(n) for lower <= n < upper

        if lower >= limit:
            break

        # numbers divisible by prime1
        ret += sum_mults_in_range(lower + 1, min(upper, limit + 1), prime1)

        # numbers divisible by prime2
        ret += sum_mults_in_range(lower + 1, min(upper, limit + 1), prime2)

        # subtract numbers counted twice(divisible by prime1 * prime2)
        ret -= 2 * sum_mults_in_range(lower + 1, min(upper, limit + 1), prime1 * prime2)

    return ret


if __name__ == "__main__":
    print(solution())
