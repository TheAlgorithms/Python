"""
Source: https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort

This is a non-parallelized implementation of odd-even transposition sort.

Normally the swaps in each set happen simultaneously, without that the algorithm
is no better than bubble sort.

For doctests run following command:
python3 -m doctest -v odd_even_transposition_single_threaded.py

For manual testing run:
python3 odd_even_transposition_single_threaded.py
"""

from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


def odd_even_transposition[T: Comparable](collection: list[T]) -> list[T]:
    """
    Sort a list in place using the odd-even transposition sort algorithm.

    The algorithm alternates between comparing-and-swapping even-indexed and
    odd-indexed adjacent pairs until the collection is fully sorted.  Because
    each pass compares a disjoint set of pairs, the passes can be parallelized;
    this implementation walks the pairs sequentially.

    :param collection: a mutable ordered collection with comparable items
    :return: the same collection, sorted in ascending order

    Examples:
    >>> odd_even_transposition([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> odd_even_transposition([13, 11, 18, 0, -1]) == sorted([13, 11, 18, 0, -1])
    True
    >>> odd_even_transposition([-.1, 1.1, .1, -2.9]) == sorted([-.1, 1.1, .1, -2.9])
    True
    >>> odd_even_transposition([])
    []
    >>> odd_even_transposition([3, 3, 1, 2, 2, 1])
    [1, 1, 2, 2, 3, 3]
    >>> odd_even_transposition(['c', 'a', 'b']) == sorted(['c', 'a', 'b'])
    True
    >>> odd_even_transposition([3.3, 1.1, 2.2]) == sorted([3.3, 1.1, 2.2])
    True
    >>> values = [4, 2, 7, 1]
    >>> result = odd_even_transposition(values)
    >>> result is values
    True
    >>> values
    [1, 2, 4, 7]
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> odd_even_transposition(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> odd_even_transposition(collection) == sorted(collection)
    True
    >>> odd_even_transposition([1, "a"])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    arr_size = len(collection)
    for _ in range(arr_size):
        for i in range(_ % 2, arr_size - 1, 2):
            if collection[i + 1] < collection[i]:
                collection[i], collection[i + 1] = collection[i + 1], collection[i]

    return collection


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    arr = list(range(10, 0, -1))
    print(f"Original: {arr}. Sorted: {odd_even_transposition(arr)}")
