"""
This is a pure Python implementation of the library sort algorithm.

For doctests run following command:
python -m doctest -v library_sort.py
or
python3 -m doctest -v library_sort.py
For manual testing run:
python library_sort.py
"""


def library_sort(collection: list) -> list:
    """
    Sorts the given collection in ascending order using the Library Sort algorithm.

    :param collection: A mutable ordered collection with comparable items.
    :return: The same collection ordered by ascending.

    Examples:
    >>> library_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> library_sort([])
    []
    >>> library_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def insertion_sort(arr):
        """
        Sorts a list using the Insertion Sort algorithm.

        :param arr: A mutable list with comparable items.
        :return: The same list ordered in ascending order.

        Examples:
        >>> insertion_sort([5, 3, 2, 4, 1])
        [1, 2, 3, 4, 5]
        >>> insertion_sort([0])
        [0]
        >>> insertion_sort([])
        []
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    if len(collection) <= 1:
        return collection

    mid = len(collection) // 2
    left = library_sort(collection[:mid])
    right = library_sort(collection[mid:])

    if left[-1] <= right[0]:
        return left + right

    insertion_sort(left)
    insertion_sort(right)

    return library(left, right)


def library(left: list, right: list) -> list:
    """
    Merges two sorted collections into a single sorted collection.

    :param left: A sorted collection
    :param right: A sorted collection
    :return: A merged and sorted collection

    Examples:
    >>> library([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> library([1], [2])
    [1, 2]
    >>> library([], [1, 2, 3])
    [1, 2, 3]
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    sorted_list = library_sort(unsorted)
    print(*sorted_list, sep=",")
