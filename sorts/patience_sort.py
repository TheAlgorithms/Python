from __future__ import annotations

from bisect import bisect_left
from functools import total_ordering
from heapq import merge

"""
A pure Python implementation of the patience sort algorithm.

For more information: https://en.wikipedia.org/wiki/Patience_sorting

This algorithm is based on the card game patience.

This version can sort integers, floats, and strings using
mixed_patience_sort().

For doctests run the following command:
python3 -m doctest -v patience_sort.py

For manual testing run:
python3 patience_sort.py
"""


@total_ordering
class Stack(list):
    def __lt__(self, other):
        return self[-1] < other[-1]

    def __eq__(self, other):
        return self[-1] == other[-1]


def patience_sort(collection: list) -> list:
    """Sort a collection using the patience sort algorithm.
    :param collection: A mutable ordered collection containing comparable items.
    :return: The same collection ordered in ascending order.
    Examples:
    >>> patience_sort([1, 9, 5, 21, 17, 6])
    [1, 5, 6, 9, 17, 21]

    >>> patience_sort([])
    []

    >>> patience_sort([-3, -17, -48])
    [-48, -17, -3]
    """
    stacks: list[Stack] = []

    # Place each element on the first suitable stack, following
    # the rules of the patience sort algorithm.
    for element in collection:
        new_stack:  list = Stack([element])
        stack_index:  list = bisect_left(stacks, new_stack)

        if stack_index != len(stacks):
            stacks[stack_index].append(element)
        else:
            stacks.append(new_stack)

    # Merge the stacks to produce the final sorted collection.
    collection[:] = merge(*(reversed(stack) for stack in stacks))
    return collection


def mixed_patience_sort(collection: list) -> list:
    """Sort integers, floats, and strings using patience sort.

    Numbers are sorted by magnitude and placed before strings.
    Strings are sorted alphabetically according to Python's
    standard string ordering.

    :param collection: A mutable collection containing integers,
        floats, and strings.
    :return: The same collection with numbers followed by strings.

    Examples:
    >>> mixed_patience_sort([1, 9, 3.64, "Apple", "letter", 23.65])
    [1, 3.64, 9, 23.65, 'Apple', 'letter']

    >>> mixed_patience_sort(["banana", "Apple", "letter"])
    ['Apple', 'banana', 'letter']

    >>> mixed_patience_sort([3.5, 1, 8.2])
    [1, 3.5, 8.2]

    >>> mixed_patience_sort([])
    []

    >>> mixed_patience_sort([1, {"name": "Obed"}])
    Traceback (most recent call last):
    ValueError: Only integers, floats, and strings are allowed.
    """
    number_items: list[int | float] = []
    string_items: list[str] = []

    for element in collection:
        if isinstance(element, (int, float)):
            number_items.append(element)
        elif isinstance(element, str):
            string_items.append(element)
        else:
            raise ValueError("Only integers, floats, and strings are allowed.")

    sorted_numbers:  int = patience_sort(number_items)
    sorted_strings:  str = patience_sort(string_items)

    collection[:] = sorted_numbers + sorted_strings
    return collection


def convert_item(item: str) -> int | float | str:
    """Convert a string into an integer, float, or string.

    :param item: The input string to convert.
    :return: An integer, float, or the original string.

    Examples:
    >>> convert_item("25")
    25

    >>> convert_item("3.14")
    3.14

    >>> convert_item("Apple")
    'Apple'
    """
    item = item.strip()

    try:
        return int(item)
    except ValueError:
        try:
            return float(item)
        except ValueError:
            return item


if __name__ == "__main__":
    user_input:  str| int|float = input("Enter integers, floats, and strings separated by commas:\n").strip()
    unsorted: str| int|float = [convert_item(item) for item in user_input.split(",")]
    print(mixed_patience_sort(unsorted))
