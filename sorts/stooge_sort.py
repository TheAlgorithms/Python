"""
Stooge Sort - a recursive sorting algorithm.

It is notably slow (worse than bubble sort) but is included here
for educational purposes to illustrate recursive divide-and-conquer thinking.

Time Complexity: O(n^(log3/log1.5)) ≈ O(n^2.71)
Space Complexity: O(log n) due to recursion stack

Reference: https://en.wikipedia.org/wiki/Stooge_sort
"""


def stooge_sort(arr: list[int], i: int = 0, j: int = -1) -> list[int]:
    """
    Sorts a list in-place using the stooge sort algorithm and returns it.

    >>> stooge_sort([3, 1, 2])
    [1, 2, 3]
    >>> stooge_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> stooge_sort([1])
    [1]
    >>> stooge_sort([])
    []
    >>> stooge_sort([2, 2, 1])
    [1, 2, 2]
    >>> stooge_sort([10, -1, 5, 0])
    [-1, 0, 5, 10]
    """
    if len(arr) <= 1:
        return arr

    if j == -1:
        j = len(arr) - 1

    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]

    if (j - i + 1) > 2:
        t = (j - i + 1) // 3
        stooge_sort(arr, i, j - t)
        stooge_sort(arr, i + t, j)
        stooge_sort(arr, i, j - t)

    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by commas: ")
    nums = [int(x.strip()) for x in user_input.split(",")]
    print(f"Sorted: {stooge_sort(nums)}")
