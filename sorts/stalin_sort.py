"""
Stalin Sort algorithm: Removes elements that are out of order.
Elements that are not greater than or equal to the previous element are discarded.
Reference: https://medium.com/@kaweendra/the-ultimate-sorting-algorithm-6513d6968420
"""


def stalin_sort(sequence: list[int]) -> list[int]:
    """
    Sorts a list using the Stalin sort algorithm.

    >>> stalin_sort([4, 3, 5, 2, 1, 7])
    [4, 5, 7]

    >>> stalin_sort([1, 2, 3, 4])
    [1, 2, 3, 4]

    >>> stalin_sort([4, 5, 5, 2, 3])
    [4, 5, 5]

    >>> stalin_sort([6, 11, 12, 4, 1, 5])
    [6, 11, 12]

    >>> stalin_sort([5, 0, 4, 3])
    [5]

    >>> stalin_sort([5, 4, 3, 2, 1])
    [5]

    >>> stalin_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]

    >>> stalin_sort([1, 2, 8, 7, 6])
    [1, 2, 8]
    """
    if any(x < 0 for x in sequence):
        raise ValueError("Sequence must only contain non-negative integers")

    result = [sequence[0]]
    for i in range(1, len(sequence)):
        if sequence[i] >= result[-1]:
            result.append(sequence[i])

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
