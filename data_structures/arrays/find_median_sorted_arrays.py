"""
https://atharayil.medium.com/median-of-two-sorted-arrays-day-36-python-fcbd2dbbb668
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two sorted integer arrays.

    :param nums1: The first sorted array (must be integers).
    :param nums2: The second sorted array (must be integers).
    :return: The median of the combined sorted arrays.
    :raises ValueError: if both are empty, not sorted, or contain non-integer values.

    >>> find_median_sorted_arrays([1, 3], [2])
    2.0
    >>> find_median_sorted_arrays([1, 2], [3, 4])
    2.5
    >>> find_median_sorted_arrays([1, 3, 5], [2, 4, 6])
    3.5
    >>> find_median_sorted_arrays([1, 2, 3], [4, 5, 6, 7])
    4.0
    >>> find_median_sorted_arrays([], [2, 3])
    2.5
    >>> find_median_sorted_arrays([-2, -1], [0, 2])
    -0.5
    >>> find_median_sorted_arrays([1.5, 2.5], [3.0, 4.0]) # Contains a float
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must be sorted and contain only integer values
    >>> find_median_sorted_arrays([3, 2, 1], [4, 5, 6]) # Not sorted
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must be sorted and contain only integer values
    >>> find_median_sorted_arrays([1, 2, 'a'], [3, 4, 5]) # Contains a character
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must be sorted and contain only integer values
    >>> find_median_sorted_arrays(['a', 'b', 'c'], [3, 4, 5]) # Contains a character
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must be sorted and contain only integer values
    """
    # Check if both input arrays are empty
    if not nums1 and not nums2:
        raise ValueError("Input arrays are empty")

    # Check if arrays are sorted and contain only integer values
    for array in [nums1, nums2]:
        if any(not isinstance(x, int) for x in array) or any(
            array[i] > array[i + 1] for i in range(len(array) - 1)
        ):
            raise ValueError(
                "Input arrays must be sorted and contain only integer values"
            )

    # Combine and sort the arrays
    combined = sorted(nums1 + nums2)

    # Calculate the median
    mid = len(combined) // 2
    if len(combined) % 2 == 0:
        return float((combined[mid - 1] + combined[mid]) / 2.0)
    else:
        return float(combined[mid])


# Example usage
if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print("Median of Example 1:", find_median_sorted_arrays(nums1, nums2))

    nums1 = [-4, -2]
    nums2 = [3, 4]
    print("Median of Example 2:", find_median_sorted_arrays(nums1, nums2))
