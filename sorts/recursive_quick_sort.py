from __future__ import annotations

from typing import Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def quick_sort[T: Comparable](data: list[T]) -> list[T]:
    """
    >>> for data in ([2, 1, 0], [2.2, 1.1, 0], "quick_sort"):
    ...     quick_sort(data) == sorted(data)
    True
    True
    True

    >>> quick_sort(["c", "a", "b"])
    ['a', 'b', 'c']

    >>> quick_sort([2.5, -1, 0.0])
    [-1, 0.0, 2.5]

    >>> quick_sort([1, "a"])
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'int' and 'str'
    """
    if len(data) <= 1:
        return data
    else:
        return [
            *quick_sort([e for e in data[1:] if not data[0] < e]),
            data[0],
            *quick_sort([e for e in data[1:] if data[0] < e]),
        ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
