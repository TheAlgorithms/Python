from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


def adaptive_merge_sort[T: Comparable](sequence: list[T]) -> list[T]:
    """
    Sort a list in ascending order using adaptive merge sort.

    :param sequence: a mutable list of comparable items
    :return: the same list ordered by ascending

    >>> adaptive_merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> adaptive_merge_sort([])
    []
    >>> adaptive_merge_sort([7])
    [7]
    >>> adaptive_merge_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> adaptive_merge_sort([3, 3, 3])
    [3, 3, 3]
    >>> adaptive_merge_sort([4, 3, 2, 1])
    [1, 2, 3, 4]
    >>> adaptive_merge_sort(["c", "a", "b"])
    ['a', 'b', 'c']
    >>> adaptive_merge_sort([2.5, -1.0, 0.0])
    [-1.0, 0.0, 2.5]
    >>> adaptive_merge_sort([1, "a"])
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if len(sequence) < 2:
        return sequence

    aux = sequence[:]
    adaptive_merge_sort_helper(sequence, aux, 0, len(sequence) - 1)
    return sequence


def adaptive_merge_sort_helper[T: Comparable](
    array: list[T], aux: list[T], low: int, high: int
) -> None:
    if high <= low:
        return

    mid = (low + high) // 2

    adaptive_merge_sort_helper(aux, array, low, mid)
    adaptive_merge_sort_helper(aux, array, mid + 1, high)

    if not array[mid + 1] < array[mid]:
        array[low : high + 1] = aux[low : high + 1]
        return

    merge(array, aux, low, mid, high)


def merge[T: Comparable](
    array: list[T], aux: list[T], low: int, mid: int, high: int
) -> None:
    i, j = low, mid + 1

    for k in range(low, high + 1):
        if i > mid or j > high:
            if i > mid:
                aux[k] = array[j]
                j += 1
            else:
                aux[k] = array[i]
                i += 1
        elif not array[j] < array[i]:
            aux[k] = array[i]
            i += 1
        else:
            aux[k] = array[j]
            j += 1

    for k in range(low, high + 1):
        array[k] = aux[k]
