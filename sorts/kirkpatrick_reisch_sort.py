import heapq
import random

"""
Kirkpatrick-Reisch sorting algorithm.
Divides input into sqrt(n) blocks, sorts each, then merges using a min-heap.

Time Complexity:
- Average case: O(n * sqrt(n))
- Worst case: O(n * sqrt(n))
- Best case: O(n * sqrt(n))

Space Complexity: O(n)

Explanation Links:
https://en.wikipedia.org/wiki/Kirkpatrick%E2%80%93Reisch_sort
https://sortingsearching.com/2020/06/06/kirkpatrick-reisch.html
"""


def kirkpatrick_reisch_sort(arr):
    """
    Implements the Kirkpatrick-Reisch sorting algorithm.

    Args:
    arr (list): The input list to be sorted.

    Returns:
    list: A new list containing the sorted elements.

    Examples:
    >>> kirkpatrick_reisch_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    >>> kirkpatrick_reisch_sort([])
    []

    >>> kirkpatrick_reisch_sort([1])
    [1]

    >>> kirkpatrick_reisch_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> kirkpatrick_reisch_sort([-1, -3, 5, 0, 2])
    [-3, -1, 0, 2, 5]
    """
    n = len(arr)
    if n <= 1:
        return arr

    # Step 1: Divide the input into sqrt(n) blocks
    block_size = int(n**0.5)
    blocks = [arr[i : i + block_size] for i in range(0, n, block_size)]

    # Step 2: Sort each block
    for block in blocks:
        block.sort()

    # Step 3: Create a min-heap of the first elements of each block
    heap = [(block[0], i, 0) for i, block in enumerate(blocks) if block]
    heapq.heapify(heap)

    # Step 4: Extract elements from the heap and refill from blocks
    sorted_arr = []
    while heap:
        val, block_index, element_index = heapq.heappop(heap)
        sorted_arr.append(val)

        if element_index + 1 < len(blocks[block_index]):
            next_element = blocks[block_index][element_index + 1]
            heapq.heappush(heap, (next_element, block_index, element_index + 1))

    return sorted_arr


if __name__ == "__main__":
    # Generate a random list of integers
    arr = [random.randint(1, 1000) for _ in range(100)]

    print("Original Array:", arr)
    sorted_arr = kirkpatrick_reisch_sort(arr)
    print("Sorted Array:", sorted_arr)

    # Verify the result
    assert sorted_arr == sorted(arr)
