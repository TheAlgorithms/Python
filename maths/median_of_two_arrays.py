from __future__ import annotations


def median_of_two_arrays(nums1: list[float], nums2: list[float]) -> float:
    """
    Time-Complexity - O(min(log M, log N)): Since we are applying binary search on the smaller sized array
    Space-Complexity - O(1)

    >>> median_of_two_arrays([1, 2], [3])
    2
    >>> median_of_two_arrays([0, -1.1], [2.5, 1])
    0.5
    >>> median_of_two_arrays([], [2.5, 1])
    1.75
    >>> median_of_two_arrays([], [0])
    0
    >>> median_of_two_arrays([], [])
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    """
    a = nums1
    b = nums2
    if len(nums1) > len(nums2):
        a, b = b, a
    total_length = len(a) + len(b)
    half = total_length // 2
    low = 0
    high = len(a) - 1
    while True:
        mid = (low + high) // 2
        partition = half - mid - 2
        a_leftmin = a[mid] if mid >= 0 else float("-inf")
        a_rightmin = a[mid + 1] if (mid + 1) < len(a) else float("inf")
        b_leftmax = b[partition] if partition >= 0 else float("-inf")
        b_rightmax = b[partition + 1] if (partition + 1) < len(b) else float("inf")
        # partition is correct
        if a_leftmin <= b_rightmax and b_leftmax <= a_rightmin:
            # odd
            if total_length % 2:
                return min(a_rightmin, b_rightmax)
            # even
            return (max(a_leftmin, b_leftmax) + min(a_rightmin, b_rightmax)) / 2
        elif a_leftmin > b_rightmax:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    array_1 = [float(x) for x in input("Enter the elements of first array: ").split()]
    array_2 = [float(x) for x in input("Enter the elements of second array: ").split()]
    print(f"The median of two arrays is: {median_of_two_arrays(array_1, array_2)}")
