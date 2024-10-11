"""
Adaptive Merge Sort Algorithm
@see https://www.tutorialspoint.com/adaptive-merging-and-sorting-in-data-structure
"""


def adaptive_merge_sort(sequence: list) -> list:
    """
    Sorts a list using the Adaptive Merge Sort algorithm.

    :param sequence: list of elements to be sorted
    :return: sorted list

    >>> adaptive_merge_sort([12, 11, 13, 5, 6, 7])
    [5, 6, 7, 11, 12, 13]

    >>> adaptive_merge_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> adaptive_merge_sort(['zebra', 'apple', 'mango', 'banana'])
    ['apple', 'banana', 'mango', 'zebra']
    """
    if len(sequence) < 2:
        return sequence

    aux = sequence[:]
    adaptive_merge_sort_helper(sequence, aux, 0, len(sequence) - 1)
    return sequence


def adaptive_merge_sort_helper(array: list, aux: list, low: int, high: int):
    if high <= low:
        return

    mid = (low + high) // 2

    adaptive_merge_sort_helper(aux, array, low, mid)
    adaptive_merge_sort_helper(aux, array, mid + 1, high)

    if array[mid] <= array[mid + 1]:
        array[low : high + 1] = aux[low : high + 1]
        return

    merge(array, aux, low, mid, high)


def merge(array: list, aux: list, low: int, mid: int, high: int):
    i, j = low, mid + 1

    for k in range(low, high + 1):
        if i > mid:
            aux[k] = array[j]
            j += 1
        elif j > high:
            aux[k] = array[i]
            i += 1
        elif array[j] < array[i]:
            aux[k] = array[j]
            j += 1
        else:
            aux[k] = array[i]
            i += 1
