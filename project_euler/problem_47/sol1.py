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


def unique_prime_factors(n):
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


# Tests based on given problem solutions
def test_upf():
    assert (unique_prime_factors(14) == set([2, 7])), "Error: unique_prime_factors(14)"
    assert (unique_prime_factors(15) == set([3, 5])), "Error: unique_prime_factors(15)"
    assert (unique_prime_factors(644) == set([2, 7, 23])), "Error: unique_prime_factors(644)"
    assert (unique_prime_factors(645) == set([3, 5, 43])), "Error: unique_prime_factors(645)"
    assert (unique_prime_factors(646) == set([2, 17, 19])), "Error: unique_prime_factors(646)"


@lru_cache(maxsize=5)
def upf_len(num):
    """Helper function to memoize upf() length results for a given value."""
    return len(unique_prime_factors(num))
    


def equality(iterable):
    """Check equality of all elements in hashable interable."""
    if iterable[:1]:
        return iterable[1:] == iterable[:-1]


def run(n):
    """Run core process to find solution."""
    
    i = 2
    
    success = 0
    
    out = []
    
    while success < 1:
        # Increment each value of a generated range
        group = list(map(lambda x, y=i: y + x, [i for i in range(n)]))

        # Run elements through out unique_prime_factors function
        # Append our target number to the end.
        checker = list(map(upf_len, group))
        checker.append(n)

        # If all numbers in the list are euqal, increment our success variable
        # to exit the while loop and return the current group of numbers.
        if equality(checker):
            success += 1
            return group
        i += 1

def solution(N=4):
    """Returns the first value of the first four consecutive integers to have four distinct prime factors each.
    >>> solution()
    134043
    """
    results = run(N)
    if len(results) > 0:
        return results[0]


if __name__ == "__main__":
    test_upf()
    print(solution())        
