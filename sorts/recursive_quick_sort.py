"""
A pure Python implementation of a recursive quick sort.

For doctests run the following command:
    python3 -m doctest -v recursive_quick_sort.py

For manual testing run:
    python3 recursive_quick_sort.py
"""

from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...

    def __le__(self, other: Any, /) -> bool: ...

    def __gt__(self, other: Any, /) -> bool: ...


def quick_sort[T: Comparable](data: list[T]) -> list[T]:
    """Sort a list of mutually comparable items with recursive quick sort.

    Returns a new list. Items must be mutually orderable. Mixing types that
    cannot be compared raises ``TypeError`` instead of returning a silently
    wrong order.

    Examples:
    >>> quick_sort([2, 1, 0])
    [0, 1, 2]
    >>> quick_sort([2.2, 1.1, 0])
    [0, 1.1, 2.2]
    >>> quick_sort(["c", "a", "b"])
    ['a', 'b', 'c']
    >>> quick_sort([])
    []
    >>> quick_sort([2.5, -1, 0.0]) == sorted([2.5, -1, 0.0])
    True
    >>> quick_sort(list("quick_sort")) == sorted("quick_sort")
    True
    >>> import pytest
    >>> with pytest.raises(TypeError):
    ...     quick_sort([1, "a"])
    >>> for data in ([2, 1, 0], [2.2, 1.1, 0], list("quick_sort")):
    ...     quick_sort(data) == sorted(data)
    True
    True
    True
    """
    if len(data) <= 1:
        return data
    return [
        *quick_sort([item for item in data[1:] if item <= data[0]]),
        data[0],
        *quick_sort([item for item in data[1:] if item > data[0]]),
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
