"""
This is a pure Python implementation of the merge sort algorithm.

For doctests run following command:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py
For manual testing run:
python merge_sort.py
"""

from typing import Protocol, TypeVar

# CHANGED: Added Comparable Protocol.
# WHY: Merge sort is a comparison-based sorting algorithm, so it should
# support any type of item that can be compared using the < operator,
# not only integers.


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


# CHANGED: Added a TypeVar bounded to Comparable.
# WHY: This preserves the input element type while ensuring that the
# elements support comparison.


T = TypeVar("T", bound=Comparable)

# CHANGED: list[int] -> list[T]
# WHY: Merge sort can sort any comparable items such as ints, strings,
# and floats.


def merge_sort(collection: list[T]) -> list[T]:
    """
    Sorts a list using the merge sort algorithm.

    :param collection: A collection with comparable items.
    :return: The collection ordered in ascending order.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_sort([])
    []

    >>> merge_sort([-2, -45, -5])
    [-45, -5, -2]

    # CHANGED: Added a string example.
    # WHY: Proves merge_sort works with comparable non-integer types.
    >>> merge_sort(["c", "a", "b"])
    ['a', 'b', 'c']

    # CHANGED: Added a float example.
    # WHY: Further proves the algorithm is not restricted to integers.
    >>> merge_sort([2.5, -1.0, 0.0])
    [-1.0, 0.0, 2.5]
    """

    def merge(left: list[T], right: list[T]) -> list[T]:
        """
        Merge two sorted lists into a single sorted list.

        :param left: Left collection
        :param right: Right collection
        :return: Merged result
        """
        result: list[T] = []
        while left and right:
            # CHANGED: Use only < instead of <=.
            # WHY: Comparable guarantees the < operator. Requiring <=
            # would unnecessarily require comparable objects to implement
            # an additional comparison method.
            if right[0] < left[0]:
                result.append(right.pop(0))
            else:
                result.append(left.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(collection) <= 1:
        return collection
    mid_index = len(collection) // 2
    return merge(merge_sort(collection[:mid_index]), merge_sort(collection[mid_index:]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item) for item in user_input.split(",")]
        sorted_list = merge_sort(unsorted)
        print(*sorted_list, sep=",")
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
