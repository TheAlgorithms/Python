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
        elif array[i] <= array[j]:
            aux[k] = array[i]
            i += 1
        else:
            aux[k] = array[j]
            j += 1

    for k in range(low, high + 1):
        array[k] = aux[k]

    print(f"After merge: {array[low:high + 1]}")
