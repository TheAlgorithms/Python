"""
Median of Medians Algorithm
Guarantees O(n) worst-case time complexity for finding the k-th smallest element.
Reference: https://en.wikipedia.org/wiki/Median_of_medians
"""


def partition(arr: list, pivot: int) -> tuple[list, list, list]:
    """
    Partition array into elements less than, equal to, and greater than pivot.

    >>> partition([3, 1, 4, 1, 5], 3)
    ([1, 1], [3], [4, 5])
    >>> partition([7, 7, 7], 7)
    ([], [7, 7, 7], [])
    """
    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]
    return low, equal, high


def median_of_medians(arr: list, rank: int) -> int:
    """
    Find the k-th smallest element in an unsorted list using Median of Medians.

    Args:
        arr: List of comparable elements
        rank: 1-based index of the desired smallest element

    Returns:
        The k-th smallest element in arr

    Raises:
        ValueError: If rank is out of range

    >>> median_of_medians([3, 1, 4, 1, 5, 9, 2, 6], 3)
    2
    >>> median_of_medians([7, 2, 10, 5], 1)
    2
    >>> median_of_medians([1, 2, 3, 4, 5], 5)
    5
    """
    if not 1 <= rank <= len(arr):
        raise ValueError(f"rank={rank} is out of range for array of length {len(arr)}")

    if len(arr) <= 5:
        return sorted(arr)[rank - 1]

    chunks = [arr[i : i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    pivot = median_of_medians(medians, len(medians) // 2 + 1)

    low, equal, high = partition(arr, pivot)

    if rank <= len(low):
        return median_of_medians(low, rank)
    elif rank <= len(low) + len(equal):
        return pivot
    else:
        return median_of_medians(high, rank - len(low) - len(equal))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
