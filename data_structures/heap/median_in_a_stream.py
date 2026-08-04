"""
Median in a stream using a heap-based approach.

Reference:
https://en.wikipedia.org/wiki/Median#Running_median
"""

import heapq


def signum(a: int, b: int) -> int:
    """
    Return 1 if a > b, -1 if a < b, 0 if equal.
    """
    if a > b:
        return 1
    if a < b:
        return -1
    return 0


def call_median(
    element: int,
    max_heap: list[int],
    min_heap: list[int],
    median: int,
) -> int:
    """
    Update heaps and median based on the new element.

    Args:
        element (int): new element in stream
        max_heap (list[int]): max heap (as negative numbers)
        min_heap (list[int]): min heap
        median (int): current median

    Returns:
        int: updated median
    """
    size_diff = signum(len(max_heap), len(min_heap))

    if size_diff == 0:
        if element > median:
            heapq.heappush(min_heap, element)
            median = min_heap[0]
        else:
            heapq.heappush(max_heap, -element)
            median = -max_heap[0]
    elif size_diff == 1:
        if element > median:
            heapq.heappush(min_heap, element)
        else:
            heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -element))
        median = (-max_heap[0] + min_heap[0]) // 2
    else:  # size_diff == -1
        if element > median:
            heapq.heappush(max_heap, -heapq.heappushpop(min_heap, element))
        else:
            heapq.heappush(max_heap, -element)
        median = (-max_heap[0] + min_heap[0]) // 2

    return median


def median_in_a_stream(arr: list[int]) -> list[int]:
    """
    Return the median after each new element in the stream.

    Args:
        arr (list[int]): list of integers

    Returns:
        list[int]: running medians

    >>> median_in_a_stream([20, 14, 13, 16, 17])
    [20, 17, 14, 15, 16]
    >>> median_in_a_stream([5, 15, 1, 3])
    [5, 10, 5, 4]
    >>> median_in_a_stream([])
    Traceback (most recent call last):
    ...
    ValueError: Input list must not be empty
    """
    if not arr:
        raise ValueError("Input list must not be empty")

    max_heap: list[int] = []  # left side (as negative numbers)
    min_heap: list[int] = []  # right side
    median = arr[0]
    max_heap.append(-arr[0])
    medians: list[int] = [median]

    for element in arr[1:]:
        median = call_median(element, max_heap, min_heap, median)
        medians.append(median)

    return medians


if __name__ == "__main__":
    n = int(input("Enter number of elements: ").strip())
    arr = [int(input().strip()) for _ in range(n)]
    result = median_in_a_stream(arr)
    print("Running medians:", result)
