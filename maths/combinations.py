"""
https://en.wikipedia.org/wiki/Combination
"""
from math import factorial


def combinations(n: int, k: int) -> int:
    """
    Returns the number of different combinations of k length which can
    be made from n values, where n >= k.

    Examples:
    >>> combinations(10,5)
    252

    >>> combinations(6,3)
    20

    >>> combinations(20,5)
    15504

    >>> combinations(52, 5)
    2598960

    >>> combinations(0, 0)
    1

    >>> combinations(-4, -5)
    ...
    Traceback (most recent call last):
    ValueError: Please enter positive integers for n and k where n >= k
    """

    # If either of the conditions are true, the function is being asked
    # to calculate a factorial of a negative number, which is not possible
    if n < k or k < 0:
        raise ValueError("Please enter positive integers for n and k where n >= k")
    return factorial(n) // (factorial(k) * factorial(n - k))


if __name__ == "__main__":
    print(
        "The number of five-card hands possible from a standard",
        f"fifty-two card deck is: {combinations(52, 5)}\n",
    )

    print(
        "If a class of 40 students must be arranged into groups of",
        f"4 for group projects, there are {combinations(40, 4)} ways",
        "to arrange them.\n",
    )

    print(
        "If 10 teams are competing in a Formula One race, there",
        f"are {combinations(10, 3)} ways that first, second and",
        "third place can be awarded.",
    )
