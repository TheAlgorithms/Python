"""
A Python implementation for finding number of
derangements possible for k objects
https://en.wikipedia.org/wiki/Derangement
"""


def derangement(objects: int) -> int:
    """
    Calculates the number of derangements of k objects.
    :param objects:the number of objects ( -1 < objects < 1560 )
    :return :the number of derangements
    :raises :ValueError: If objects is negative.

    Examples:
    >>> derangement(3)
    2
    >>> derangement(5)
    44
    >>> derangement(10)
    1334961
    """
    if objects < 0:
        raise ValueError("k must be a non-negative integer. Retry")

    # Base cases
    if objects == 0:
        return 0
    if objects == 1:
        return 0

    # Initialize the derangement counts
    derange_1 = 1
    derange_2 = 0
    answer = 1

    # Calculate derangements using dynamic programming
    # Answer: F(n) = (n - 1) * ( F(n - 1) + F(n - 2) )
    for i in range(3, objects + 1):
        answer = (i - 1) * (derange_1 + derange_2)
        derange_2 = derange_1
        derange_1 = answer

    return answer
