from typing import TypeVar

T = TypeVar("T", int, float, str)  # comparable types


def bubble_sort_iterative(collection: list[T]) -> list[T]:
    """
    Pure implementation of bubble sort algorithm in Python.

    :param collection: list of comparable elements
    :return: the same collection ordered in ascending order

    Examples:
    >>> bubble_sort_iterative([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort_iterative([])
    []
    >>> bubble_sort_iterative([-2, -45, -5])
    [-45, -5, -2]
    >>> bubble_sort_iterative([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]
    >>> bubble_sort_iterative(['d', 'a', 'b', 'e']) == sorted(['d', 'a', 'b', 'e'])
    True
    >>> bubble_sort_iterative(['z', 'a', 'y', 'b', 'x', 'c'])
    ['a', 'b', 'c', 'x', 'y', 'z']
    >>> bubble_sort_iterative([1.1, 3.3, 5.5, 7.7, 2.2, 4.4, 6.6])
    [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
    """
    length = len(collection)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True
        if not swapped:
            break
    return collection


def bubble_sort_recursive(collection: list[T]) -> list[T]:
    """
    Recursive implementation of bubble sort.

    :param collection: list of comparable elements
    :return: the same list in ascending order

    Examples:
    >>> bubble_sort_recursive([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort_recursive([])
    []
    >>> bubble_sort_recursive([-2, -45, -5])
    [-45, -5, -2]
    >>> bubble_sort_recursive([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]
    >>> bubble_sort_recursive(['d', 'a', 'b', 'e']) == sorted(['d', 'a', 'b', 'e'])
    True
    >>> bubble_sort_recursive(['z', 'a', 'y', 'b', 'x', 'c'])
    ['a', 'b', 'c', 'x', 'y', 'z']
    >>> bubble_sort_recursive([1.1, 3.3, 5.5, 7.7, 2.2, 4.4, 6.6])
    [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
    """
    length = len(collection)
    swapped = False
    for i in range(length - 1):
        if collection[i] > collection[i + 1]:
            collection[i], collection[i + 1] = collection[i + 1], collection[i]
            swapped = True

    if not swapped:
        return collection
    return bubble_sort_recursive(collection)



if __name__ == "__main__":
    import doctest
    from random import sample
    from timeit import timeit

    doctest.testmod()

    # Benchmark: Iterative seems slightly faster than recursive.
    num_runs = 10_000
    unsorted = sample(range(-50, 50), 100)
    timer_iterative = timeit(
        "bubble_sort_iterative(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nIterative bubble sort:")
    print(*bubble_sort_iterative(unsorted), sep=",")
    print(f"Processing time (iterative): {timer_iterative:.5f}s for {num_runs:,} runs")

    unsorted = sample(range(-50, 50), 100)
    timer_recursive = timeit(
        "bubble_sort_recursive(unsorted[:])", globals=globals(), number=num_runs
    )
    print("\nRecursive bubble sort:")
    print(*bubble_sort_recursive(unsorted), sep=",")
    print(f"Processing time (recursive): {timer_recursive:.5f}s for {num_runs:,} runs")
