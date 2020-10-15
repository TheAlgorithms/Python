"""
Project Euler Problem 77: https://projecteuler.net/problem=77

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?
"""

primes = set(range(3, 100, 2))
primes.add(2)
for i in range(3, 100, 2):
    if i not in primes:
        continue
    primes.difference_update(set(range(i * i, 100, i)))

CACHE_PARTITION = {0: {1}}


def partition(n: int) -> set:
    """
    Return a set of integers corresponding to unique prime partitions of n.
    The unique prime partitions can be represented as unique prime decompositions,
    e.g. (7+3) <-> 7*3 = 12, (3+3+2+2) = 3*3*2*2 = 36
    >>> partition(10)
    {32, 36, 21, 25, 30}
    >>> partition(15)
    {192, 160, 105, 44, 112, 243, 180, 150, 216, 26, 125, 126}
    """
    if n < 0:
        return set()
    if n in CACHE_PARTITION:
        return CACHE_PARTITION[n]

    ret = set()
    for prime in primes:
        if prime > n:
            continue
        for sub in partition(n - prime):
            ret.add(sub * prime)

    CACHE_PARTITION[n] = ret
    return ret


def solution(m: int = 5000) -> int:
    """
    Return the smallest integer that can be written as the sum of primes in over
    m unique ways.
    >>> solution(500)
    45
    """
    for n in range(1, 100):
        if len(partition(n)) > m:
            return n
    return 0


if __name__ == "__main__":
    print(f"{solution() = }")
