def adaptive_merge_sort(sequence: list) -> list:
    """
    Sorts a list using the Adaptive Merge Sort algorithm.

    >>> adaptive_merge_sort([4, 3, 1, 2])
    Initial sequence: [4, 3, 1, 2]
    Sorting: array[0:2] and array[2:4]
    Sorting: array[0:1] and array[1:2]
    Merging: array[0:1] and array[1:2]
    After merge: [3, 4]
    Sorting: array[2:3] and array[3:4]
    Skipping merge as array[2] <= array[3]
    Merging: array[0:2] and array[2:4]
    After merge: [1, 2, 3, 4]
    Sorted sequence: [1, 2, 3, 4]
    [1, 2, 3, 4]
    """
    if len(sequence) < 2:
        return sequence

    aux = sequence[:]
    print(f"Initial sequence: {sequence}")
    adaptive_merge_sort_helper(sequence, aux, 0, len(sequence) - 1)
    print(f"Sorted sequence: {sequence}")
    return sequence


def adaptive_merge_sort_helper(array: list, aux: list, low: int, high: int) -> None:
    """
    Helper function for Adaptive Merge Sort algorithm.

    >>> adaptive_merge_sort_helper([4, 3, 1, 2], [4, 3, 1, 2], 0, 3)
    Sorting: array[0:2] and array[2:4]
    Sorting: array[0:1] and array[1:2]
    Merging: array[0:1] and array[1:2]
    After merge: [3, 4]
    Sorting: array[2:3] and array[3:4]
    Skipping merge as array[2] <= array[3]
    Merging: array[0:2] and array[2:4]
    After merge: [1, 2, 3, 4]
    """
    if high <= low:
        return

    mid = (low + high) // 2
    print(f"Sorting: array[{low}:{mid + 1}] and array[{mid + 1}:{high + 1}]")

    adaptive_merge_sort_helper(aux, array, low, mid)
    adaptive_merge_sort_helper(aux, array, mid + 1, high)

    if array[mid] <= array[mid + 1]:
        print(f"Skipping merge as array[{mid}] <= array[{mid + 1}]")
        array[low:high + 1] = aux[low:high + 1]
        return

    merge(array, aux, low, mid, high)


def merge(array: list, aux: list, low: int, mid: int, high: int) -> None:
    """
    Merges two sorted subarrays of the main array.

    >>> merge([4, 3, 1, 2], [4, 3, 1, 2], 0, 1, 3)
    Merging: array[0:2] and array[2:4]
    After merge: [1, 2, 3, 4]
    """
    print(f"Merging: array[{low}:{mid + 1}] and array[{mid + 1}:{high + 1}]")

    i, j = low, mid + 1
    for k in range(low, high + 1):
        if i > mid:
            aux[k] = array[j]
            j += 1
        elif j > high:
            aux[k] = array[i]
            i += 1
        elif array[i] <= array[j]:  # Keep stable by using <=
            aux[k] = array[i]
            i += 1
        else:
            aux[k] = array[j]
            j += 1

    for k in range(low, high + 1):
        array[k] = aux[k]

    print(f"After merge: {array[low:high + 1]}")


# Example usage
if __name__ == "__main__":
    print(adaptive_merge_sort([4, 3, 1, 2]))
