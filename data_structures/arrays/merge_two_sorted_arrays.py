
"""
    https://en.wikipedia.org/wiki/Merge_algorithm

    Merge two sorted arrays.

    Args:
        nums1: The first array.
        nums2: The second array.
    
    Returns:
        The merged sorted array.

    Examples:
        >>> merge_two_sorted_arrays([1,5,7], [0,4,9])
        [0,1,4,5,7,9]

        >>> merge_two_sorted_arrays([-11,5,45], [0,5,9])
        [-11,0,5,5,9,45]    
"""

def merge_two_sorted_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    
    if not nums1 and not nums2:
        raise ValueError("Both input arrays are empty.")

    # Initialize two pointers and an array to store the merged array.
    i, j = 0, 0
    merged = []

    # Merge the two arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Merge remaining elements
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Merge remaining elements
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    