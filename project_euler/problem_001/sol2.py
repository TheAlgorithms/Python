"""
Project Euler Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples(k):
    """
    Calculate the sum of the first 'k' natural numbers,
    which are multiples of a given number 'k'.

    Args:
    k (int): The number of which multiples are to be summed.

    Returns:
    int: The sum of multiples of 'k'.
    """
    return (k * (k + 1)) // 2


def solution(n: int = 1000) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below n.

    Args:
    n (int): The upper limit for finding multiples.

    Returns:
    int: The sum of multiples of 3 or 5 below n.
    """
    n -= 1  # We subtract 1 to consider numbers below n
    terms_3 = n // 3
    terms_5 = n // 5
    terms_15 = n // 15

    total = (
        3 * sum_of_multiples(terms_3)
        + 5 * sum_of_multiples(terms_5)
        - 15 * sum_of_multiples(terms_15)
    )

    return total


if __name__ == "__main__":
    print(f"{solution() = }")
