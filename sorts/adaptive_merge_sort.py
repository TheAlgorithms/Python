def adaptive_merge_sort(sequence: list) -> list:
    if len(sequence) < 2:
        return sequence

    aux = sequence[:]
    print(f"Initial sequence: {sequence}")
    adaptive_merge_sort_helper(sequence, aux, 0, len(sequence) - 1)
    print(f"Sorted sequence: {sequence}")
    return sequence


def adaptive_merge_sort_helper(array: list, aux: list, low: int, high: int) -> None:
    if high <= low:
        return

    mid = (low + high) // 2
    print(f"Sorting: array[{low}:{mid + 1}] and array[{mid + 1}:{high + 1}]")

    adaptive_merge_sort_helper(aux, array, low, mid)
    adaptive_merge_sort_helper(aux, array, mid + 1, high)

    if array[mid] <= array[mid + 1]:
        print(f"Skipping merge as array[{mid}] <= array[{mid + 1}]")
        array[low : high + 1] = aux[low : high + 1]
        return

    merge(array, aux, low, mid, high)


def merge(array: list, aux: list, low: int, mid: int, high: int) -> None:
    print(f"Merging: array[{low}:{mid + 1}] and array[{mid + 1}:{high + 1}]")

    i, j = low, mid + 1
    for k in range(low, high + 1):
        if i > mid or j > high:
            if i > mid:
                aux[k] = array[j]
                j += 1
            else:
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


# Example usage
if __name__ == "__main__":
    print(adaptive_merge_sort([4, 3, 1, 2]))
