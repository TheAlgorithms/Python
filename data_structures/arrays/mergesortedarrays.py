def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Merge two sorted arrays into a single sorted array.
    >>> merge_sorted_arrays([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """
    merged_array = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    return merged_array

if __name__ == "__main__":
    import doctest

    doctest.testmod()
