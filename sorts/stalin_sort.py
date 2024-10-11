"""
Stalin Sort algorithm: Removes elements that are out of order.
Elements that are not greater than or equal to the previous element are discarded.
Reference: https://medium.com/@kaweendra/the-ultimate-sorting-algorithm-6513d6968420
"""

from typing import List


def stalin_sort(sequence: List[int]) -> List[int]:
    """
    Sorts a list using the Stalin sort algorithm.

    Parameters:
        sequence (List[int]): A list of non-negative integers.

    Returns:
        List[int]: A sorted list according to Stalin Sort.

    Raises:
        TypeError: If the sequence contains non-integers or negative integers.

    Examples:
    >>> stalin_sort([6, 11, 12, 4, 1, 5])
    [6, 11, 12]

    >>> stalin_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    [9]

    >>> stalin_sort([5, 0, 4, 3])
    [5]

    >>> stalin_sort([8, 2, 1])
    [8]

    >>> stalin_sort([1, .9, 0.0, 0, -1, -.9])
    Traceback (most recent call last):
        ...
    TypeError: Sequence must be a list of non-negative integers

    >>> stalin_sort("Hello world")
    Traceback (most recent call last):
        ...
    TypeError: Sequence must be a list of non-negative integers
    """
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("Sequence must be a list of non-negative integers")

    if not sequence:
        return []
    result = [sequence[0]]

    for item in sequence[1:]:
        if item >= result[-1]:
            result.append(item)

    return result


if __name__ == "__main__":
    assert stalin_sort([5, 4, 3, 2, 1]) == [5]
    assert stalin_sort([7, 9, 4, 3, 5]) == [7, 9]
    assert stalin_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
