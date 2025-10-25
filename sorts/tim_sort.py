from typing import List, TypeVar

T = TypeVar("T")


def binary_search(arr: List[T], item: T, left: int, right: int) -> int:
    """
    Return the index where `item` should be inserted in `arr[left:right+1]`
    to keep it sorted.

    >>> binary_search([1, 3, 5, 7], 6, 0, 3)
    3
    >>> binary_search([1, 3, 5, 7], 0, 0, 3)
    0
    >>> binary_search([1, 3, 5, 7], 8, 0, 3)
    4
    """
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return left


def insertion_sort(arr: List[T]) -> List[T]:
    """
    Sort the list in-place using binary insertion sort.

    >>> insertion_sort([3, 1, 2, 4])
    [1, 2, 3, 4]
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i - 1)
        arr[:] = arr[:j] + [key] + arr[j:i] + arr[i + 1 :]
    return arr


def merge(left: List[T], right: List[T]) -> List[T]:
    """
    Merge two sorted lists into one sorted list.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def tim_sort(arr: List[T]) -> List[T]:
    """
    Simplified version of TimSort for educational purposes.

    TimSort is a hybrid stable sorting algorithm that combines merge sort
    and insertion sort. It was originally designed by Tim Peters for Python (2002).

    Source: https://en.wikipedia.org/wiki/Timsort

    >>> tim_sort("Python")
    ['P', 'h', 'n', 'o', 't', 'y']
    >>> tim_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> tim_sort([3, 2, 1]) == sorted([3, 2, 1])
    True
    >>> tim_sort([])  # empty input
    []
    """
    if not isinstance(arr, list):
        arr = list(arr)

    if not arr:
        return []

    min_run = 32
    n = len(arr)

    if n == 1:
        return arr.copy()

    runs = []
    for start in range(0, n, min_run):
        end = min(start + min_run, n)
        run = insertion_sort(arr[start:end])
        runs.append(run)

    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                new_runs.append(merge(runs[i], runs[i + 1]))
            else:
                new_runs.append(runs[i])
        runs = new_runs

    return runs[0] if runs else []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
