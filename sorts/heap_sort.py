import doctest

"""
Heap sort in Python

This is a pure Python implementation of the heap sort algorithm.

For doctests run following command:
python -m doctest -v heap_sort.py
or
python3 -m doctest -v heap_sort.py

For manual testing run:
python heap_sort.py

"""


def heapify(unsorted, n, i):
    """
    Heapify subtree rooted at index i.

    n is size of heap.

    >>> unsorted = [3, 2, 1, 5, 6, 4]
    >>> n = len(unsorted)
    >>> i = 0
    >>> heapify(unsorted, n, i)
    >>> unsorted
    [6, 5, 1, 3, 2, 4]
    """

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and unsorted[i] < unsorted[left]:
        largest = left

    if right < n and unsorted[largest] < unsorted[right]:
        largest = right

    if largest != i:
        unsorted[i], unsorted[largest] = unsorted[largest], unsorted[i]
        heapify(unsorted, n, largest)


def heapSort(unsorted):  # noqa: N802
    """
    Heap sort an array.

    >>> unsorted = [3, 2, 1, 5, 6, 4]
    >>> heapSort(unsorted)
    >>> unsorted
    [1, 2, 3, 4, 5, 6]
    """

    n = len(unsorted)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(unsorted, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        unsorted[i], unsorted[0] = unsorted[0], unsorted[i]
        heapify(unsorted, i, 0)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma: ").strip()
    unsorted = [int(x) for x in user_input.split(",")]
    heapSort(unsorted)
    print(unsorted)


doctest.testmod(verbose=True)
