#!/usr/bin/env python3
"""
Flash Sort Algorithm Implementation

Flash sort is a distribution sorting algorithm showing linear computational
complexity O(n) for uniformly distributed datasets and relatively little
additional memory requirement. The basic idea is to use the distribution
of the values to be sorted to determine their approximate final positions
directly, without comparing and moving each element through many intermediate
positions as done by other algorithms.

The algorithm was developed by Karl-Dietrich Neubert in 1998 and builds upon
the idea of bucket sort. It works by classifying elements into classes and
then sorting each class.

Time Complexity:
- Best Case: O(n) when data is uniformly distributed
- Average Case: O(n + k) where k is the number of classes
- Worst Case: O(n²) when data is not uniformly distributed

Space Complexity: O(k) where k is the number of classes

Source: https://en.wikipedia.org/wiki/Flashsort
"""

from __future__ import annotations


def flash_sort(arr: list[int | float]) -> list[int | float]:
    """
    Sorts a list using the Flash Sort algorithm.

    Flash sort is particularly efficient for uniformly distributed data.
    It uses the distribution of values to determine approximate positions.

    Args:
        arr: List of integers or floats to be sorted

    Returns:
        Sorted list in ascending order

    Examples:
    >>> flash_sort([4, 2, 7, 1, 9, 3])
    [1, 2, 3, 4, 7, 9]
    >>> flash_sort([])
    []
    >>> flash_sort([5])
    [5]
    >>> flash_sort([3, 3, 3, 3])
    [3, 3, 3, 3]
    >>> flash_sort([-1, -5, 0, 3, 2])
    [-5, -1, 0, 2, 3]
    >>> flash_sort([1.5, 2.3, 0.1, 3.7, 1.2])
    [0.1, 1.2, 1.5, 2.3, 3.7]
    >>> flash_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> import random
    >>> data = random.sample(range(100), 20)
    >>> flash_sort(data) == sorted(data)
    True
    >>> flash_sort([42])
    [42]
    >>> flash_sort([2.5, 1.1, 3.3, 2.5, 1.1])
    [1.1, 1.1, 2.5, 2.5, 3.3]
    """
    if len(arr) <= 1:
        return arr.copy()

    # Create a copy to avoid modifying the original array
    result = arr.copy()
    n = len(result)

    # Find min and max values
    min_val = min(result)
    max_val = max(result)

    # If all elements are the same, return the array
    if min_val == max_val:
        return result

    # Number of classes (buckets) - typically n/10 to n/5 works well
    m = max(1, int(0.45 * n))

    # Initialize class sizes array
    class_sizes = [0] * m

    # Calculate class sizes
    c1 = (m - 1) / (max_val - min_val)

    for value in result:
        class_index = int(c1 * (value - min_val))
        if class_index >= m:
            class_index = m - 1
        class_sizes[class_index] += 1

    # Calculate cumulative class sizes (positions)
    for i in range(1, m):
        class_sizes[i] += class_sizes[i - 1]

    # Permutation phase
    hold = result[0]
    j = 0
    k = m - 1

    while j < n - 1:
        while j >= class_sizes[k]:
            k -= 1

        flash = int(c1 * (hold - min_val))
        if flash >= m:
            flash = m - 1

        while j < class_sizes[flash]:
            k = flash
            class_sizes[k] -= 1
            result[j], result[class_sizes[k]] = result[class_sizes[k]], result[j]
            hold = result[j]
            j += 1
            flash = int(c1 * (hold - min_val))
            if flash >= m:
                flash = m - 1

        j += 1
        if j < n:
            hold = result[j]

    # Insertion sort for final sorting within classes
    for i in range(1, n):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key

    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # Additional test cases
    test_cases: list[list[int | float]] = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 3, 3, 3],
        [-1, -3, 2, 0, -5],
        [1.1, 2.2, 0.5, 3.3, 1.5],
    ]

    for test_case in test_cases:
        sorted_result = flash_sort(test_case)
        expected = sorted(test_case)
        assert sorted_result == expected, f"Failed for {test_case}"
        print(f"✓ {test_case} -> {sorted_result}")

    print("All tests passed!")
