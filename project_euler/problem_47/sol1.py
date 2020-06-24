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
    Function to find unique prime factors of an integer.
    Tests include sorting because only the set really matters,
    not the order in which it is produced.
    >>> set(sorted(unique_prime_factors(14)))
    {2, 7}
    >>> set(sorted(unique_prime_factors(644)))
    {2, 23, 7}
    >>> set(sorted(unique_prime_factors(646)))
    {17, 2, 19}
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


@lru_cache(maxsize=5)
def upf_len(num: int) -> int:
    """
    Helper function to memoize upf() length results for a given value.
    >>> upf_len(14)
    2
    """
    return len(unique_prime_factors(num))


def equality(iterable: list) -> bool:
    """
    Check equality of ALL elements in an interable.
    >>> equality([1,2,3,4])
    False
    >>> equality([2,2,2,2])
    True
    >>> equality([1, 2, 3, 2, 1])
    True
    """
    return len(set(iterable)) in (0, 1)
        return iterable[1:] == iterable[:-1]


def run(n: int) -> list:
    """
    Function that runs core process to find problem solution.
    >>> run(3)
    [644, 645, 646]
    """

    i = 2


    while True:
        # Increment each value of a generated range
        group = list(map(lambda x, y=i: y + x, [i for i in range(n)]))

        # Run elements through out unique_prime_factors function
        # Append our target number to the end.
        checker = [upf_len(x) for x in group]
        checker.append(n)

        # If all numbers in the list are equal, increment our success variable
        # to exit the while loop and return the current group of numbers.
        if equality(checker):
            return group
        i += 1


def solution(n: int = 4) -> int:
    """Returns the first value of the first four consecutive integers to have four
    distinct prime factors each.
    >>> solution()
    134043
    """
    results = run(N)
    return results[0] if len(results) else None
        return results[0]


if __name__ == "__main__":
    print(solution())
