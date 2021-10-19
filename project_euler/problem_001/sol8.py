"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solution(limit: int = 1000) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    >>> solution()
    233168
    """

    multiples_of_3 = set(range(3, limit, 3))
    multiples_of_5 = set(range(5, limit, 5))
    # Union of two sets — only unique values are preserved
    result = sum(multiples_of_3 | multiples_of_5)

    return result


if __name__ == "__main__":
    print(f"{solution() = }")
