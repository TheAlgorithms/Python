"""
Reversort is a sorting algorithm described in Google Code Jam 2021 Qualification Round.

Algorithm:
1. For i from 1 to N-1:
   a. Find the position j of the minimum element in the subarray from position i to N
   b. Reverse the subarray from position i to j

Time Complexity: O(n²) - For each position, we find the minimum and reverse
Space Complexity: O(n) - Due to list slicing in Python
                  (can be O(1) with in-place reversal)

For doctests run following command:
python3 -m doctest -v reversort.py

For manual testing run:
python reversort.py
"""

from typing import Any


def reversort(collection: list[Any]) -> list[Any]:
    """
    Sort a list using the Reversort algorithm.

    Reversort works by repeatedly finding the minimum element in the unsorted
    portion and reversing the subarray from the current position to where the
    minimum element is located.

    :param collection: A mutable ordered collection with comparable items
    :return: The sorted collection in ascending order

    Examples:
    >>> reversort([4, 2, 1, 3])
    [1, 2, 3, 4]
    >>> reversort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> reversort([])
    []
    >>> reversort([-2, -5, -45])
    [-45, -5, -2]
    >>> reversort([1])
    [1]
    >>> reversort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> reversort([2, 1, 4, 3])
    [1, 2, 3, 4]
    >>> reversort([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]
    >>> reversort([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> reversort([3, 3, 3, 3])
    [3, 3, 3, 3]
    >>> reversort([56])
    [56]
    >>> reversort([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    >>> reversort([]) == sorted([])
    True
    >>> reversort([-2, -45, -5]) == sorted([-2, -45, -5])
    True
    >>> reversort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True
    >>> reversort(['d', 'a', 'b', 'e']) == sorted(['d', 'a', 'b', 'e'])
    True
    >>> reversort(['z', 'a', 'y', 'b', 'x', 'c'])
    ['a', 'b', 'c', 'x', 'y', 'z']
    >>> reversort([1.1, 3.3, 5.5, 7.7, 2.2, 4.4, 6.6])
    [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
    >>> reversort([1, 3.3, 5, 7.7, 2, 4.4, 6])
    [1, 2, 3.3, 4.4, 5, 6, 7.7]
    >>> import random
    >>> collection_arg = random.sample(range(-50, 50), 100)
    >>> reversort(collection_arg) == sorted(collection_arg)
    True
    >>> import string
    >>> collection_arg = random.choices(string.ascii_letters + string.digits, k=100)
    >>> reversort(collection_arg) == sorted(collection_arg)
    True
    """
    arr = collection[:]  # Create a copy to avoid modifying the original
    n = len(arr)

    for i in range(n - 1):
        # Find the position of the minimum element in arr[i:]
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Reverse the subarray from position i to min_index
        if min_index != i:
            arr[i : min_index + 1] = arr[i : min_index + 1][::-1]

    return arr


def reversort_cost(collection: list[Any]) -> int:
    """
    Calculate the cost of sorting using Reversort.

    The cost is defined as the sum of the lengths of all reversed segments.
    This is based on the Google Code Jam 2021 problem.

    :param collection: A mutable ordered collection with comparable items
    :return: The total cost of sorting

    Examples:
    >>> reversort_cost([4, 2, 1, 3])
    6
    >>> reversort_cost([1, 2])
    1
    >>> reversort_cost([7, 6, 5, 4, 3, 2, 1])
    12
    >>> reversort_cost([1, 2, 3, 4])
    3
    >>> reversort_cost([1])
    0
    >>> reversort_cost([])
    0
    """
    arr = collection[:]  # Create a copy to avoid modifying the original
    n = len(arr)
    total_cost = 0

    for i in range(n - 1):
        # Find the position of the minimum element in arr[i:]
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Reverse the subarray from position i to min_index
        arr[i : min_index + 1] = arr[i : min_index + 1][::-1]

        # Cost is the length of the reversed segment
        total_cost += min_index - i + 1

    return total_cost


if __name__ == "__main__":
    import doctest
    from random import sample
    from timeit import timeit

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"Sorted list: {reversort(unsorted)}")
    print(f"Sort cost: {reversort_cost(unsorted)}")

    # Benchmark
    num_runs = 1000
    test_arr = sample(range(-50, 50), 100)
    timer = timeit("reversort(test_arr[:])", globals=globals(), number=num_runs)
    print(f"\nProcessing time: {timer:.5f}s for {num_runs:,} runs on 100 elements")
