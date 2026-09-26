from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


def quick_sort[T: Comparable](data: list[T]) -> list[T]:
    """
    >>> for data in ([2, 1, 0], [2.2, 1.1, 0], "quick_sort"):
    ...     quick_sort(data) == sorted(data)
    True
    True
    True

    >>> quick_sort([1, "a"])
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'str' and 'int'
    """
    if len(data) <= 1:
        return data
    else:
        return [
            *quick_sort([e for e in data[1:] if e <= data[0]]),
            data[0],
            *quick_sort([e for e in data[1:] if e > data[0]]),
        ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
