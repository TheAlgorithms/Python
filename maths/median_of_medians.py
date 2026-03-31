"""
Median of Medians Algorithm
Guarantees O(n) worst-case time complexity for finding the k-th smallest element.
Reference: https://en.wikipedia.org/wiki/Median_of_medians
"""


def partition(arr: list, pivot: int) -> tuple:
    """Partition array into elements less than, equal to, and greater than pivot."""
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    return low, equal, high


def median_of_medians(arr: list, k: int) -> int:
    """
    Find the k-th smallest element in an unsorted list using Median of Medians.

    Args:
        arr: List of comparable elements
        k: 1-based index of the desired smallest element

    Returns:
        The k-th smallest element in arr

    Raises:
        ValueError: If k is out of range

    Examples:
        >>> median_of_medians([3, 1, 4, 1, 5, 9, 2, 6], 3)
        2
        >>> median_of_medians([7, 2, 10, 5], 1)
        2
        >>> median_of_medians([1, 2, 3, 4, 5], 5)
        5
    """
    if not 1 <= k <= len(arr):
        raise ValueError(f"k={k} is out of range for array of length {len(arr)}")

    # Base case
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Step 1: Divide into chunks of 5 and find median of each chunk
    chunks = [arr[i : i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    # Step 2: Recursively find median of medians
    pivot = median_of_medians(medians, len(medians) // 2 + 1)

    # Step 3: Partition around pivot
    low, equal, high = partition(arr, pivot)

    # Step 4: Recurse into the correct partition
    if k <= len(low):
        return median_of_medians(low, k)
    elif k <= len(low) + len(equal):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(equal))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    sample = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Array: {sample}")
    for i in range(1, len(sample) + 1):
        print(f"  {i}-th smallest: {median_of_medians(sample, i)}")