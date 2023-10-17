"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solution(n: int = 1000) -> int:
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
    """

     n -= 1  # We subtract 1 to consider numbers below n
    sum_of_multiples = lambda k: (k * (k + 1)) // 2  # Sum of multiples of k
    terms_3 = n // 3
    terms_5 = n // 5
    terms_15 = n // 15

    total = (
        3 * sum_of_multiples(terms_3) +
        5 * sum_of_multiples(terms_5) -
        15 * sum_of_multiples(terms_15)
    )

    return total


if __name__ == "__main__":
    print(f"{solution() = }")
