from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


def bubble_sort_recursive[T: Comparable](arr: list[T]) -> list[T]:
    """
    Sorts a collection of comparable items using the recursive Bubble Sort algorithm.

    >>> bubble_sort_recursive([5, 1, 4, 2, 8])
    [1, 2, 4, 5, 8]
    >>> bubble_sort_recursive([])
    []
    >>> bubble_sort_recursive([1])
    [1]
    >>> bubble_sort_recursive([3, 3, 2, 1])
    [1, 2, 3, 3]
    >>> bubble_sort_recursive([-1, 5, 0, -2])
    [-2, -1, 0, 5]
    >>> bubble_sort_recursive(["c", "a", "b"])
    ['a', 'b', 'c']
    >>> bubble_sort_recursive([2.5, -1, 0.0])
    [-1, 0.0, 2.5]
    >>> bubble_sort_recursive([1, "a"])
    Traceback (most recent call last):
        ...
    TypeError: '>' not supported between instances of 'int' and 'str'
    """
    n = len(arr)
    if n <= 1:
        return arr

    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True

    if not swapped:
        return arr

    return [*bubble_sort_recursive(arr[:-1]), arr[-1]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
