"""
https://www.enjoyalgorithms.com/blog/median-of-two-sorted-arrays
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two arrays.

    Args:
        nums1: The first array.
        nums2: The second array.

    Returns:
    The median of the two arrays.

    Examples:
        >>> find_median_sorted_arrays([1, 3], [2])
        2.0

        >>> find_median_sorted_arrays([1, 2], [3, 4])
        2.5

        >>> find_median_sorted_arrays([0, 0], [0, 0])
        0.0

        >>> find_median_sorted_arrays([], [])
        Traceback (most recent call last):
            ...
        ValueError: Both input arrays are empty.

        >>> find_median_sorted_arrays([], [1])
        1.0

        >>> find_median_sorted_arrays([-1000], [1000])
        0.0

        >>> find_median_sorted_arrays([-1.1, -2.2], [-3.3, -4.4])
        -2.75
    """
    if not nums1 and not nums2:
        raise ValueError("Both input arrays are empty.")

    # Merge the arrays into a single sorted array.
    merged = sorted(nums1 + nums2)
    total = len(merged)

    if total % 2 == 1:  # If the total number of elements is odd
        return float(merged[total // 2])  # then return the middle element

    # If the total number of elements is even, calculate
    # the average of the two middle elements as the median.
    middle1 = merged[total // 2 - 1]
    middle2 = merged[total // 2]
    return (float(middle1) + float(middle2)) / 2.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
