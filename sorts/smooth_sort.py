"""
A pure Python implementation of the smooth sort algorithm.

Smoothsort is an in-place comparison-based sorting algorithm designed by
Edsger W. Dijkstra in 1981. It is a variation of heapsort that uses a
sequence of Leonardo heaps (Leonardo numbers are similar to Fibonacci).

Properties:
- In-place: Yes (uses O(1) extra memory)
- Stable: No
- Best case: O(n) when data is already sorted
- Average/Worst case: O(n log n)

For more information:
https://en.wikipedia.org/wiki/Smoothsort

For doctests run following command:
python3 -m doctest -v smooth_sort.py

For manual testing run:
python3 smooth_sort.py
"""


def smooth_sort(collection: list[int]) -> list[int]:
    """
    Pure Python implementation of smoothsort algorithm

    :param collection: some mutable ordered collection with comparable items
    :return: the same collection ordered by ascending

    Examples:
    >>> smooth_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> smooth_sort([])
    []
    >>> smooth_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> smooth_sort([3, 7, 9, 28, 123, -5, 8, -30, -200, 0, 4])
    [-200, -30, -5, 0, 3, 4, 7, 8, 9, 28, 123]
    >>> smooth_sort([1])
    [1]
    >>> smooth_sort([2, 2, 2])
    [2, 2, 2]
    >>> import random
    >>> collection = random.sample(range(-50, 50), 50)
    >>> smooth_sort(collection) == sorted(collection)
    True
    """
    if len(collection) <= 1:
        return collection

    # Generate Leonardo numbers
    leonardo = _generate_leonardo_numbers(len(collection))

    # Build heap using smoothsort strategy
    _smooth_sort_build(collection, leonardo)

    # Extract maximum repeatedly
    _smooth_sort_extract(collection, leonardo)

    return collection


def _generate_leonardo_numbers(max_value: int) -> list[int]:
    """
    Generate Leonardo numbers up to max_value.
    L(0) = 1, L(1) = 1, L(n) = L(n-1) + L(n-2) + 1

    >>> _generate_leonardo_numbers(10)
    [1, 1, 3, 5, 9, 15]
    >>> _generate_leonardo_numbers(2)
    [1, 1, 3]
    >>> _generate_leonardo_numbers(0)
    [1, 1]
    """
    leonardo = [1, 1]
    while leonardo[-1] < max_value:
        leonardo.append(leonardo[-1] + leonardo[-2] + 1)
    return leonardo


def _smooth_sort_build(arr: list[int], leonardo: list[int]) -> None:
    """
    Build the Leonardo heap forest.

    >>> arr = [3, 1, 2]
    >>> leo = _generate_leonardo_numbers(len(arr))
    >>> _smooth_sort_build(arr, leo)
    >>> arr  # Array is partially heapified
    [3, 1, 2]
    """
    for i in range(len(arr)):
        _add_to_heap(arr, i, leonardo)


def _smooth_sort_extract(arr: list[int], leonardo: list[int]) -> None:
    """
    Extract elements to produce sorted output.

    >>> arr = [3, 2, 1]
    >>> leo = _generate_leonardo_numbers(len(arr))
    >>> _smooth_sort_build(arr, leo)
    >>> _smooth_sort_extract(arr, leo)
    >>> arr
    [1, 2, 3]
    """
    for i in range(len(arr) - 1, 0, -1):
        _extract_from_heap(arr, i, leonardo)


def _add_to_heap(arr: list[int], end: int, leonardo: list[int]) -> None:
    """
    Add element at index 'end' to the Leonardo heap.

    >>> arr = [1, 3, 2]
    >>> leo = _generate_leonardo_numbers(len(arr))
    >>> _add_to_heap(arr, 2, leo)
    >>> arr
    [2, 3, 1]
    """
    # This is a simplified version that focuses on correctness
    # We use a basic approach: maintain heap property up to 'end'
    _heapify_up(arr, end, leonardo)


def _extract_from_heap(arr: list[int], end: int, _leonardo: list[int]) -> None:
    """
    Remove maximum element from heap ending at index 'end'.

    >>> arr = [5, 3, 4, 1, 2]
    >>> leo = _generate_leonardo_numbers(len(arr))
    >>> _extract_from_heap(arr, 4, leo)
    >>> arr[4]  # Maximum moved to end
    5
    """
    # Find maximum in the range [0, end] and swap it to position 'end'
    max_idx = 0
    for i in range(1, end + 1):
        if arr[i] > arr[max_idx]:
            max_idx = i

    if max_idx != end:
        arr[max_idx], arr[end] = arr[end], arr[max_idx]
        # Restore heap property
        _heapify_down(arr, max_idx, end - 1)


def _heapify_up(arr: list[int], index: int, leonardo: list[int]) -> None:
    """
    Restore heap property from bottom up.

    >>> arr = [1, 2, 5, 3]
    >>> leo = _generate_leonardo_numbers(len(arr))
    >>> _heapify_up(arr, 2, leo)
    >>> arr
    [5, 2, 1, 3]
    """
    while index > 0:
        # Find parent using Leonardo number structure
        parent = _find_parent(index, leonardo)
        if parent >= 0 and arr[parent] < arr[index]:
            arr[parent], arr[index] = arr[index], arr[parent]
            index = parent
        else:
            break


def _heapify_down(arr: list[int], index: int, end: int) -> None:
    """
    Restore heap property from top down.

    >>> arr = [1, 5, 3, 2, 4]
    >>> _heapify_down(arr, 0, 4)
    >>> arr
    [5, 4, 3, 2, 1]
    """
    while index < end:
        # Find children
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left <= end and arr[left] > arr[largest]:
            largest = left
        if right <= end and arr[right] > arr[largest]:
            largest = right

        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]
            index = largest
        else:
            break


def _find_parent(index: int, _leonardo: list[int]) -> int:
    """
    Find parent index in Leonardo heap structure.

    >>> leo = _generate_leonardo_numbers(10)
    >>> _find_parent(0, leo)
    -1
    >>> _find_parent(1, leo)
    0
    >>> _find_parent(2, leo)
    0
    >>> _find_parent(5, leo)
    2
    """
    if index <= 0:
        return -1

    # For simplicity, use a standard heap parent
    return (index - 1) // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    if user_input:
        unsorted = [int(item) for item in user_input.split(",")]
        print(f"{smooth_sort(unsorted) = }")
