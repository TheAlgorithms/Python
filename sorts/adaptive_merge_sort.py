"""
Adaptive Merge Sort implementation.
https://en.wikipedia.org/wiki/Merge_sort
"""

def adaptive_merge_sort(sequence: list) -> list:
    """
    >>> adaptive_merge_sort([12, 11, 13, 5, 6, 7])
    [5, 6, 7, 11, 12, 13]

    >>> adaptive_merge_sort([4, 3, 2, 1])
    [1, 2, 3, 4]

    >>> adaptive_merge_sort(["apple", "zebra", "mango", "banana"])
    ['apple', 'banana', 'mango', 'zebra']
    """
    if len(sequence) < 2:
        return sequence

    aux = sequence[:]
    adaptive_merge_sort_recursive(sequence, aux, 0, len(sequence) - 1)
    return sequence

def adaptive_merge_sort_recursive(arr: list, aux: list, low: int, high: int) -> None:
    if high <= low:
        return

    mid = (low + high) // 2
    adaptive_merge_sort_recursive(aux, arr, low, mid)
    adaptive_merge_sort_recursive(aux, arr, mid + 1, high)

    if arr[mid] <= arr[mid + 1]:
        arr[low:high + 1] = aux[low:high + 1]
        return

    merge(arr, aux, low, mid, high)

def merge(arr: list, aux: list, low: int, mid: int, high: int) -> None:
    i, j = low, mid + 1

    for k in range(low, high + 1):
        if i > mid:
            aux[k] = arr[j]
            j += 1
        elif j > high:
            aux[k] = arr[i]
            i += 1
        elif arr[j] < arr[i]:
            aux[k] = arr[j]
            j += 1
        else:
            aux[k] = arr[i]
            i += 1


if __name__ == "__main__":
    assert adaptive_merge_sort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13]
    assert adaptive_merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert adaptive_merge_sort(["apple", "zebra", "mango", "banana"]) == ['apple', 'banana', 'mango', 'zebra']
