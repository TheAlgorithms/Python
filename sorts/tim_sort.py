from typing import Any


def binary_search(lst: list[Any], item: Any, start: int, end: int) -> int:
    """Find the insertion position for *item* in a sorted sublist using binary search.

    Returns the index where *item* should be inserted to maintain sorted order
    in ``lst[start:end+1]``.

    >>> binary_search([1, 3, 5, 7], 4, 0, 3)
    2
    >>> binary_search([1, 3, 5, 7], 0, 0, 3)
    0
    >>> binary_search([1, 3, 5, 7], 8, 0, 3)
    4
    """
    if start == end:
        return start if lst[start] > item else start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if lst[mid] < item:
        return binary_search(lst, item, mid + 1, end)
    elif lst[mid] > item:
        return binary_search(lst, item, start, mid - 1)
    else:
        return mid


def insertion_sort(lst: list[Any]) -> list[Any]:
    """Sort a list using binary insertion sort.

    For each element, use :func:`binary_search` to find its correct position
    in the already-sorted prefix, then insert it there.

    >>> insertion_sort([3, 1, 2])
    [1, 2, 3]
    >>> insertion_sort([5, 9, 10, 3, -4])
    [-4, 3, 5, 9, 10]
    """
    length = len(lst)

    for index in range(1, length):
        value = lst[index]
        pos = binary_search(lst, value, 0, index - 1)
        lst = [*lst[:pos], value, *lst[pos:index], *lst[index + 1 :]]

    return lst


def merge(left: list[Any], right: list[Any]) -> list[Any]:
    """Merge two sorted lists into a single sorted list.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [1, 2])
    [1, 2]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0], *merge(left[1:], right)]

    return [right[0], *merge(left, right[1:])]


def tim_sort(lst: list[Any] | tuple[Any, ...] | str) -> list[Any]:
    """
    >>> tim_sort("Python")
    ['P', 'h', 'n', 'o', 't', 'y']
    >>> tim_sort((1.1, 1, 0, -1, -1.1))
    [-1.1, -1, 0, 1, 1.1]
    >>> tim_sort(list(reversed(list(range(7)))))
    [0, 1, 2, 3, 4, 5, 6]
    >>> tim_sort([3, 2, 1]) == insertion_sort([3, 2, 1])
    True
    >>> tim_sort([3, 2, 1]) == sorted([3, 2, 1])
    True
    """
    length = len(lst)
    runs, sorted_runs = [], []
    new_run = [lst[0]]
    sorted_array: list[Any] = []
    i = 1
    while i < length:
        if lst[i] < lst[i - 1]:
            runs.append(new_run)
            new_run = [lst[i]]
        else:
            new_run.append(lst[i])
        i += 1
    runs.append(new_run)

    for run in runs:
        sorted_runs.append(insertion_sort(run))
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array


def main():
    """Run a demo of Timsort on a sample list and print the result."""
    lst = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
    sorted_lst = tim_sort(lst)
    print(sorted_lst)


if __name__ == "__main__":
    main()
