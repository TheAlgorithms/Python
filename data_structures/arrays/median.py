def findMedianSortedArrays(nums1, nums2):
    """
    Given two sorted arrays, nums1 and nums2, find the median element of the two merged arrays.

    :param nums1: List[int]
        The first sorted array.
    :param nums2: List[int]
        The second sorted array.
    :return: float
        The median of the merged arrays.
    """
    # Merge the two arrays
    merged = sorted(nums1 + nums2)

    # Find the median
    n = len(merged)
    if n % 2 == 0:
        # If the length is even, take the average of the middle elements
        mid1 = merged[n // 2 - 1]
        mid2 = merged[n // 2]
        median = (mid1 + mid2) / 2.0
    else:
        # If the length is odd, the median is the middle element
        median = merged[n // 2]

    return median

# Example usage:
nums1 = [1, 3]
nums2 = [2]
median_value = findMedianSortedArrays(nums1, nums2)
print("Median:", median_value)
