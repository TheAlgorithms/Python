from typing import List


def merge(
    g_array: List[int], low: int, mid1: int, mid2: int, high: int, dest_array: List[int]
) -> None:
    """
    Merge the sorted subarrays [low, mid1), [mid1, mid2), and [mid2, high) into a single sorted array.

    :param g_array: The original array to be merged.
    :param low: The index of the lower bound of the current subarray.
    :param mid1: The first midpoint index.
    :param mid2: The second midpoint index.
    :param high: The index of the upper bound (exclusive) of the current subarray.
    :param dest_array: An auxiliary array used for merging.
    :return: None
    """
    i = low
    j = mid1
    k = mid2
    l = low

    while (i < mid1) and (j < mid2) and (k < high):
        if g_array[i] < g_array[j]:
            if g_array[i] < g_array[k]:
                dest_array[l] = g_array[i]
                l += 1
                i += 1
            else:
                dest_array[l] = g_array[k]
                l += 1
                k += 1
        else:
            if g_array[j] < g_array[k]:
                dest_array[l] = g_array[j]
                l += 1
                j += 1
            else:
                dest_array[l] = g_array[k]
                l += 1
                k += 1

    while (i < mid1) and (j < mid2):
        if g_array[i] < g_array[j]:
            dest_array[l] = g_array[i]
            l += 1
            i += 1
        else:
            dest_array[l] = g_array[j]
            l += 1
            j += 1

    while (j < mid2) and (k < high):
        if g_array[j] < g_array[k]:
            dest_array[l] = g_array[j]
            l += 1
            j += 1
        else:
            dest_array[l] = g_array[k]
            l += 1
            k += 1

    while (i < mid1) and (k < high):
        if g_array[i] < g_array[k]:
            dest_array[l] = g_array[i]
            l += 1
            i += 1
        else:
            dest_array[l] = g_array[k]
            l += 1
            k += 1

    while i < mid1:
        dest_array[l] = g_array[i]
        l += 1
        i += 1

    while j < mid2:
        dest_array[l] = g_array[j]
        l += 1
        j += 1

    while k < high:
        dest_array[l] = g_array[k]
        l += 1
        k += 1


def merge_sort_3way_rec(
    g_array: List[int], low: int, high: int, dest_array: List[int]
) -> None:
    """
    Recursive function to perform 3-way merge sort on the given array.

    :param g_array: The original array to be sorted.
    :param low: The index of the lower bound of the current subarray.
    :param high: The index of the upper bound (exclusive) of the current subarray.
    :param dest_array: An auxiliary array used for merging.
    :return: None
    """
    if high - low < 2:
        return

    mid1 = low + ((high - low) // 3)
    mid2 = low + 2 * ((high - low) // 3) + 1

    merge_sort_3way_rec(dest_array, low, mid1, g_array)
    merge_sort_3way_rec(dest_array, mid1, mid2, g_array)
    merge_sort_3way_rec(dest_array, mid2, high, g_array)

    merge(dest_array, low, mid1, mid2, high, g_array)


def merge_sort_3way(g_array: List[int], size: int) -> List[int]:
    """
    Perform 3-way merge sort on the given array.

    :param g_array: List of integers to be sorted.
    :param size: The size of the array.
    :return: A new list containing the sorted elements.
    """
    if size == 0:
        return []

    g_array_copy = g_array.copy()
    merge_sort_3way_rec(g_array_copy, 0, size, g_array)
    return g_array_copy


data = [10, -2, -5, 8, 31, 2, 1, 9, 7, 3]
sorted_data = merge_sort_3way(data, 10)
print("After 3-way merge sort:", sorted_data)
