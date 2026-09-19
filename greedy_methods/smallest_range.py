"""
smallest_range function takes a list of sorted integer lists and finds the smallest
range that includes at least one number from each list, using a min heap for efficiency.
"""

from heapq import heappop, heappush
from sys import maxsize


def smallest_range(nums: list[list[int]]) -> list[int]:
    """
    Find the smallest range from each list in nums.

    Uses min heap for efficiency. The range includes at least one number from each list.

    Args:
        `nums`: List of k sorted integer lists.

    Returns:
        list: Smallest range as a two-element list.

    Examples:

    >>> smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
    [20, 24]
    >>> smallest_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    [1, 1]
    >>> smallest_range(((1, 2, 3), (1, 2, 3), (1, 2, 3)))
    [1, 1]
    >>> smallest_range(((-3, -2, -1), (0, 0, 0), (1, 2, 3)))
    [-1, 1]
    >>> smallest_range([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [3, 7]
    >>> smallest_range([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    [0, 0]
    >>> smallest_range([[], [], []])
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """

    min_heap: list[tuple[int, int, int]] = []
    current_max = -maxsize - 1

    for i, items in enumerate(nums):
        heappush(min_heap, (items[0], i, 0))
        current_max = max(current_max, items[0])

    # Initialize smallest_range with large integer values
    smallest_range = [-maxsize - 1, maxsize]

    while min_heap:
        current_min, list_index, element_index = heappop(min_heap)

        if current_max - current_min < smallest_range[1] - smallest_range[0]:
            smallest_range = [current_min, current_max]

        if element_index == len(nums[list_index]) - 1:
            break

        next_element = nums[list_index][element_index + 1]
        heappush(min_heap, (next_element, list_index, element_index + 1))
        current_max = max(current_max, next_element)

    return smallest_range


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{smallest_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]])}")  # Output: [1, 1]
