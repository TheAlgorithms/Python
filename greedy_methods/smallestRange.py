"""
https://medium.com/@saiashish3760/leetcode-q632-smallest-range-covering-elements-from-k-lists-q507-496c21157914
"""

import doctest
import heapq


def smallest_range(nums):
    """
    Finds the smallest range that includes at least one number
    from each of the k lists.

    The function uses a min heap to efficiently find the smallest range.
    Each time, it pops the smallest element from the
    heap and adds the next element from the same list to
    maintain the invariant of having one element from each list in the heap.

    Args:
        nums (list of list of int): A list of k lists of sorted integers
        in non-decreasing order.

    Returns:
        list: A list containing two integers representing the smallest range.

    Examples:
    >>> smallest_range([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
    [20, 24]
    >>> smallest_range([[1,2,3], [1,2,3], [1,2,3]])
    [1, 1]
    """

    # Create a min heap to store the first element from each list
    min_heap = []
    current_max = float("-inf")

    # Initialize the heap with the first element from each list
    for i, list_ in enumerate(nums):
        heapq.heappush(min_heap, (list_[0], i, 0))
        current_max = max(current_max, list_[0])

    # Initialize the smallest range as the largest possible
    smallest_range = [float("-inf"), float("inf")]

    while min_heap:
        current_min, list_index, element_index = heapq.heappop(min_heap)

        # Update the smallest range if the current range is smaller
        if current_max - current_min < smallest_range[1] - smallest_range[0]:
            smallest_range = [current_min, current_max]

        # Break if rreaching the end of one of the lists
        if element_index == len(nums[list_index]) - 1:
            break

        # Add the next element from the same list to the heap
        next_element = nums[list_index][element_index + 1]
        heapq.heappush(min_heap, (next_element, list_index, element_index + 1))
        current_max = max(current_max, next_element)

    return smallest_range


if __name__ == "__main__":
    doctest.testmod()
    example1 = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    output1 = smallest_range(example1)
    print("Smallest Range:", output1)  # Smallest Range: [20, 24]
