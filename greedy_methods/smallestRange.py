"""
https://medium.com/@saiashish3760/leetcode-q632-smallest-range-covering-elements-from-k-lists-q507-496c21157914
"""
import doctest
import heapq
import sys

def smallest_range(nums: list[list[int]]) -> list[int]:
    """
    Find the smallest range from each list in nums.
    
    Uses min heap for efficiency. The range includes at least one number from each list.

    Args:
        nums (list of list of int): List of k sorted integer lists.

    Returns:
        list: Smallest range as a two-element list.

    Examples:
    >>> smallest_range([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
    [20, 24]
    >>> smallest_range([[1,2,3], [1,2,3], [1,2,3]])
    [1, 1]
    """

    min_heap: list[tuple[int, int, int]] = []
    current_max = -sys.maxsize - 1

    for i, list_ in enumerate(nums):
        heapq.heappush(min_heap, (list_[0], i, 0))
        current_max = max(current_max, list_[0])

    # Initialize smallest_range with large integer values
    smallest_range = [-sys.maxsize - 1, sys.maxsize]

    while min_heap:
        current_min, list_index, element_index = heapq.heappop(min_heap)

        if current_max - current_min < smallest_range[1] - smallest_range[0]:
            smallest_range = [current_min, current_max]

        if element_index == len(nums[list_index]) - 1:
            break

        next_element = nums[list_index][element_index + 1]
        heapq.heappush(min_heap, (next_element, list_index, element_index + 1))
        current_max = max(current_max, next_element)

    return smallest_range

if __name__ == "__main__":
    doctest.testmod()
    example1 = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    output1 = smallest_range(example1)
    print("Smallest Range:", output1)  # Output: [20, 24]
