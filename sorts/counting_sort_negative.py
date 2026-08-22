from __future__ import annotations

"""
Counting Sort — Extended to support negative numbers.

Standard Counting Sort only works with non-negative integers.
This implementation handles negative numbers by shifting the range.

Time Complexity:  O(n + k) where k = max_value - min_value
Space Complexity: O(n + k)

Stability: Stable — equal elements maintain their relative order.

Limitation: Only works with integers (not floats or strings).

>>> counting_sort([4, 2, 2, 8, 3, 3, 1])
[1, 2, 2, 3, 3, 4, 8]

>>> counting_sort([-5, -2, -8, 0, 3, -1, 7])
[-8, -5, -2, -1, 0, 3, 7]

>>> counting_sort([])
[]

>>> counting_sort([1])
[1]

>>> counting_sort([5, 5, 5, 5])
[5, 5, 5, 5]

>>> counting_sort([0, 0, 0])
[0, 0, 0]

>>> counting_sort([-3, -3, -1, -1, -2])
[-3, -3, -2, -1, -1]

>>> counting_sort([100, -100, 0, 50, -50])
[-100, -50, 0, 50, 100]
"""


def counting_sort(array: list[int]) -> list[int]:
    """
    Sort a list of integers using counting sort with support for negative numbers.

    This works by:
    1. Finding the min and max values to determine the range
    2. Creating a count array of size (max - min + 1)
    3. Counting occurrences of each value (shifted by min)
    4. Building the cumulative count for stable placement
    5. Placing elements in their correct sorted position

    Args:
        array: A list of integers to sort (can include negatives).

    Returns:
        A new sorted list.

    Raises:
        TypeError: If any element is not an integer.

    >>> counting_sort([3, 1, 4, 1, 5, 9, 2, 6])
    [1, 1, 2, 3, 4, 5, 6, 9]

    >>> counting_sort([-10, 5, -3, 8, -1, 0])
    [-10, -3, -1, 0, 5, 8]
    """
    if len(array) <= 1:
        return list(array)

    # Validate input
    for element in array:
        if not isinstance(element, int):
            raise TypeError(
                f"Counting sort only works with integers, got {type(element).__name__}"
            )

    # Find the range
    min_val = min(array)
    max_val = max(array)
    range_size = max_val - min_val + 1

    # Initialize count array
    count = [0] * range_size

    # Count occurrences (shift by min_val to handle negatives)
    for value in array:
        count[value - min_val] += 1

    # Build cumulative count (for stable sort)
    for i in range(1, range_size):
        count[i] += count[i - 1]

    # Build the output array (traverse input in reverse for stability)
    output = [0] * len(array)
    for value in reversed(array):
        index = count[value - min_val] - 1
        output[index] = value
        count[value - min_val] -= 1

    return output


def counting_sort_simple(array: list[int]) -> list[int]:
    """
    Simplified counting sort — builds sorted array directly from counts.

    This version is simpler but NOT stable (equal elements may not preserve
    their original relative order, though for integers this doesn't matter).

    Args:
        array: A list of integers to sort.

    Returns:
        A new sorted list.

    >>> counting_sort_simple([4, 2, 2, 8, 3, 3, 1])
    [1, 2, 2, 3, 3, 4, 8]

    >>> counting_sort_simple([-3, -1, -5, 0, 2])
    [-5, -3, -1, 0, 2]
    """
    if len(array) <= 1:
        return list(array)

    min_val = min(array)
    max_val = max(array)
    range_size = max_val - min_val + 1

    count = [0] * range_size

    for value in array:
        count[value - min_val] += 1

    # Reconstruct sorted array from counts
    result = []
    for i in range(range_size):
        result.extend([i + min_val] * count[i])

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Demo
    print("=== Counting Sort (with negative number support) ===\n")

    test_cases = [
        [4, 2, 2, 8, 3, 3, 1],
        [-5, -2, -8, 0, 3, -1, 7],
        [100, -100, 0, 50, -50],
        [5, 5, 5, 5],
        [],
    ]

    for arr in test_cases:
        sorted_arr = counting_sort(arr)
        print(f"  Input:  {arr}")
        print(f"  Output: {sorted_arr}\n")
