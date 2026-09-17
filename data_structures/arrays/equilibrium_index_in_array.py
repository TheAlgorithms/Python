"""
Find the Equilibrium Index of an Array.

Reference:
https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

Python doctest can be run with:

python -m doctest -v equilibrium_index_in_array.py

Given an array arr of size n, return an equilibrium index
if one exists, otherwise return -1.

An equilibrium index is an index where the sum of all
elements to the left equals the sum of all elements
to the right.

Examples:

    >>> equilibrium_index([-7, 1, 5, 2, -4, 3, 0])
    3

    >>> equilibrium_index([1, 2, 3, 4, 5])
    -1

    >>> equilibrium_index([1, 1, 1, 1, 1])
    2

    >>> equilibrium_index([2, 4, 6, 8, 10, 3])
    -1
"""


def equilibrium_index(arr: list[int]) -> int:
    """
    Find the first equilibrium index of an array.

    Args:
        arr: The input array of integers.

    Returns:
        The first equilibrium index, or -1 if none exists.

    Examples:
        >>> equilibrium_index([])
        -1

        >>> equilibrium_index([5])
        0

        >>> equilibrium_index([-7, 1, 5, 2, -4, 3, 0])
        3

        >>> equilibrium_index([1, 2, 3, 4, 5])
        -1

        >>> equilibrium_index([1, 1, 1, 1, 1])
        2

        >>> equilibrium_index([0, 0, 0])
        0

        >>> equilibrium_index([-1, -1, -1])
        1

        >>> equilibrium_index([1, -1, 0])
        2

    Time Complexity:
        O(n), where n is the length of the array.

    Space Complexity:
        O(1), using only constant extra space.
    """
    total_sum = sum(arr)
    left_sum = 0

    for i, value in enumerate(arr):
        total_sum -= value

        if left_sum == total_sum:
            return i

        left_sum += value

    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
