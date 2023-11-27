"""
https://atharayil.medium.com/median-of-two-sorted-arrays-day-36-python-fcbd2dbbb668
"""

def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Finds the median of two sorted arrays.

    :param nums1: The first sorted array.
    :param nums2: The second sorted array.
    :return: The median of the combined sorted arrays.
    :raises ValueError: If both input arrays are empty.

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

    """
    # Check if both input arrays are empty
    if not nums1 and not nums2:
        raise ValueError("Input arrays are not valid")

    # If one is empty, find the median of the non-empty array
    if not nums1 or not nums2:
        combined = nums1 if nums1 else nums2
        mid = len(combined) // 2
        if len(combined) % 2 == 0:
            return (combined[mid - 1] + combined[mid]) / 2.0
        else:
            return combined[mid]

    # Make sure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2

    left, right = 0, m
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = half - partition1

        max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float("inf") if partition1 == m else nums1[partition1]

        max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float("inf") if partition2 == n else nums2[partition2]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if total % 2 == 0:
                return float(
                    (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                )
            else:
                return float(min(min_right1, min_right2))
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1

    # If the loop exits without returning, the input arrays are not valid
    raise ValueError("Input arrays are not valid")


# Example
if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print("Median of Example 1:", find_median_sorted_arrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Median of Example 2:", find_median_sorted_arrays(nums1, nums2))
