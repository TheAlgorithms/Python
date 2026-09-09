
from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


def double_sort[T: Comparable](collection: list[T]) -> list[T]:
    """This sorting algorithm sorts an array using the principle of bubble sort,
    but does it both from left to right and right to left.
    Hence, it's called "Double sort"
    :param collection: mutable ordered sequence of elements
    :return: the same collection in ascending order
    Examples:
    >>> double_sort([-1 ,-2 ,-3 ,-4 ,-5 ,-6 ,-7])
    [-7, -6, -5, -4, -3, -2, -1]
    >>> double_sort([])
    []
    >>> double_sort([-1 ,-2 ,-3 ,-4 ,-5 ,-6])
    [-6, -5, -4, -3, -2, -1]
    >>> double_sort([-3, 10, 16, -42, 29]) == sorted([-3, 10, 16, -42, 29])
    True
    
    >>> double_sort(["d", "a", "c", "b"])
    ['a', 'b', 'c', 'd']
    >>> double_sort([2.5, -1.0, 0.0])
    [-1.0, 0.0, 2.5]
"""
    no_of_elements = len(collection)
    for _ in range(
        int(((no_of_elements - 1) / 2) + 1)
    ):  # we don't need to traverse to end of list as
        for j in range(no_of_elements - 1):
            # apply the bubble sort algorithm from left to right (or forwards)
            if collection[j + 1] < collection[j]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
            # apply the bubble sort algorithm from right to left (or backwards)
            if collection[no_of_elements - 1 - j] < collection[no_of_elements - 2 - j]:
                (
                    collection[no_of_elements - 1 - j],
                    collection[no_of_elements - 2 - j],
                ) = (
                    collection[no_of_elements - 2 - j],
                    collection[no_of_elements - 1 - j],
                )
    return collection


if __name__ == "__main__":
    # allow the user to input the elements of the list on one line
    unsorted = [int(x) for x in input("Enter the list to be sorted: ").split() if x]
    print("the sorted list is")
    print(f"{double_sort(unsorted) = }")
