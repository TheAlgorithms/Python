"""
Combinatoric selections

Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
"""

from functools import lru_cache


def unique_prime_factors(n: int) -> set:
    """
    Find unique prime factors of an integer.
    Tests include sorting because only the set really matters,
    not the order in which it is produced.
    >>> sorted(set(unique_prime_factors(14)))
    [2, 7]
    >>> sorted(set(unique_prime_factors(644)))
    [2, 7, 23]
    >>> sorted(set(unique_prime_factors(646)))
    [2, 17, 19]
    """
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


@lru_cache
def upf_len(num: int) -> int:
    """
    Memoize upf() length results for a given value.
    >>> upf_len(14)
    2
    """
    return len(unique_prime_factors(num))


def equality(iterable: list) -> bool:
    """
    Check equality of ALL elements in an interable.
    >>> equality([1, 2, 3, 4])
    False
    >>> equality([2, 2, 2, 2])
    True
    >>> equality([1, 2, 3, 2, 1])
    False
    """
    return len(set(iterable)) in (0, 1)


def run(n: int) -> list:
    """
    Runs core process to find problem solution.
    >>> run(3)
    [644, 645, 646]
    """

    # Incrementor variable for our group list comprehension.
    # This serves as the first number in each list of values
    # to test.
    base = 2

    while True:
        # Increment each value of a generated range
        group = [base + i for i in range(n)]

        # Run elements through out unique_prime_factors function
        # Append our target number to the end.
        checker = [upf_len(x) for x in group]
        checker.append(n)

        # If all numbers in the list are equal, return the group variable.
        if equality(checker):
            return group

        # Increment our base variable by 1
        base += 1


def solution(n: int = 4) -> int:
    """Return the first value of the first four consecutive integers to have four
    distinct prime factors each.
    >>> solution()
    134043
    """
    results = run(n)
    return results[0] if len(results) else None


if __name__ == "__main__":
    print(solution())
