"""
Slowsort

Slowsort is a humorous, deliberately inefficient sorting algorithm based on the
"multiply and surrender" paradigm — the opposite of divide and conquer. It was
invented by Andrei Broder and Jorge Stolfi and published in their 1986 paper
"Pessimal Algorithms and Simplexity Analysis".

The algorithm works recursively:
1. Find the maximum of the first half and second half of the array separately.
2. Compare those two maximums and place the larger one at the end.
3. Recursively sort everything except the last element.

Slowsort is provably non-optimal and runs in superpolynomial time even on
average, making it slower than bogosort for small inputs but guaranteed to
terminate.

Time Complexity:  O(n^(log n / 2)) — superpolynomial, worse than any polynomial
Space Complexity: O(log n) due to recursion stack

Reference:
    https://en.wikipedia.org/wiki/Slowsort
"""

from __future__ import annotations


def slowsort(arr: list[int], low: int, high: int) -> None:
    """
    Recursively sort arr[low..high] in place using the slowsort algorithm.

    Args:
        arr:  The list of integers to sort (modified in place).
        low:  The starting index of the subarray to sort.
        high: The ending index of the subarray to sort (inclusive).

    >>> a = [5, 3, 8, 1, 9, 2]
    >>> slowsort(a, 0, len(a) - 1)
    >>> a
    [1, 2, 3, 5, 8, 9]

    >>> b = [1]
    >>> slowsort(b, 0, 0)
    >>> b
    [1]

    >>> c = [4, 4, 4]
    >>> slowsort(c, 0, len(c) - 1)
    >>> c
    [4, 4, 4]

    >>> d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> slowsort(d, 0, len(d) - 1)
    >>> d
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    if low >= high:
        return
    mid = (low + high) // 2
    slowsort(arr, low, mid)
    slowsort(arr, mid + 1, high)
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    slowsort(arr, low, high - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by commas: ").strip()
    unsorted = [int(x) for x in user_input.split(",")]
    print(f"Unsorted: {unsorted}")
    slowsort(unsorted, 0, len(unsorted) - 1)
    print(f"Sorted:   {unsorted}")
