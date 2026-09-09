"""
Code contributed by Honey Sharma
Source: https://en.wikipedia.org/wiki/Cycle_sort
"""

from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


def cycle_sort[T: Comparable](array: list[T]) -> list[T]:
    """
    >>> cycle_sort([4, 3, 2, 1])
    [1, 2, 3, 4]

    >>> cycle_sort([-4, 20, 0, -50, 100, -1])
    [-50, -4, -1, 0, 20, 100]

    >>> cycle_sort([-.1, -.2, 1.3, -.8])
    [-0.8, -0.2, -0.1, 1.3]

    >>> cycle_sort([])
    []

    >>> cycle_sort(["d", "a", "c", "b"])
    ['a', 'b', 'c', 'd']
    >>> cycle_sort([2.5, -1.0, 0.0])
    [-1.0, 0.0, 2.5]
"""
    array_len = len(array)
    for cycle_start in range(array_len - 1):
        item = array[cycle_start]

        pos = cycle_start
        for i in range(cycle_start + 1, array_len):
            if array[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item == array[pos]:
            pos += 1

        array[pos], item = item, array[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, array_len):
                if array[i] < item:
                    pos += 1

            while item == array[pos]:
                pos += 1

            array[pos], item = item, array[pos]

    return array


if __name__ == "__main__":
    assert cycle_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert cycle_sort([0, 1, -10, 15, 2, -2]) == [-10, -2, 0, 1, 2, 15]
