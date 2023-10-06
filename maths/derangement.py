"""
A Python implementation for finding number of
derangements possible for k objects
https://en.wikipedia.org/wiki/Derangement
"""

def derangement(k: int) -> int:
    """
    Calculates the number of derangements of k objects.
    :param k:the number of objects ( -1 < k < 1560 )
    :return :the number of derangements
    :raises :ValueError: If k is negative.

    Examples:
        >>> derangements(3)
        2
        >>> derangements(5)
        44
        >>> derangements(10)
        1334961
    """
    if k < 0:
        raise ValueError("k must be a non-negative integer. Retry")

    # Base cases
    if k == 0:
        return 0
    if k == 1:
        return 0

    # Initialize the derangement counts
    derange_1 = 1
    derange_2 = 0
    answer = 1

    # Calculate derangements using dynamic programming
    # Answer: F(n) = (n - 1) * ( F(n - 1) + F(n - 2) )
    for i in range(3, k + 1):
        answer = (i - 1) * (derange_1 + derange_2)
        derange_2 = derange_1
        derange_1 = answer

    return answer
