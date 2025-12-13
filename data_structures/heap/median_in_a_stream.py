import heapq
from typing import List


def signum(a: int, b: int) -> int:
    """
    Compare two integers.

    Returns:
        1 if a > b
       -1 if a < b
        0 if a == b
    """
    if a > b:
        return 1
    if a < b:
        return -1
    return 0


def call_median(
    element: int,
    max_heap: List[int],
    min_heap: List[int],
    median: int,
) -> int:
    """
    Insert an element into heaps and update median.
    """
    case = signum(len(max_heap), len(min_heap))

    # Case 0: both heaps have same size
    if case == 0:
        if element > median:
            heapq.heappush(min_heap, element)
            median = min_heap[0]
        else:
            heapq.heappush(max_heap, -element)
            median = -max_heap[0]

    # Case 1: max heap has more elements
    elif case == 1:
        if element > median:
            heapq.heappush(min_heap, element)
        else:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            heapq.heappush(max_heap, -element)
        median = (-max_heap[0] + min_heap[0]) // 2

    # Case -1: min heap has more elements
    else:
        if element > median:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            heapq.heappush(min_heap, element)
        else:
            heapq.heappush(max_heap, -element)
        median = (-max_heap[0] + min_heap[0]) // 2

    return median


def median_in_a_stream(numbers: List[int]) -> List[int]:
    """
    Find the median after each insertion in a stream of integers.

    Uses two heaps and follows the classic running median logic.

    Args:
        numbers: List of integers

    Returns:
        List of medians after each insertion

    Raises:
        ValueError: If the input list is empty

    >>> median_in_a_stream([20, 14, 13, 16, 17])
    [20, 17, 14, 15, 16]
    >>> median_in_a_stream([5, 15, 1, 3])
    [5, 10, 5, 4]
    >>> median_in_a_stream([])
    Traceback (most recent call last):
    ...
    ValueError: Input list must not be empty
    """
    if not numbers:
        raise ValueError("Input list must not be empty")

    max_heap: List[int] = []
    min_heap: List[int] = []
    median = 0
    result: List[int] = []

    for element in numbers:
        median = call_median(element, max_heap, min_heap, median)
        result.append(median)

    return result
