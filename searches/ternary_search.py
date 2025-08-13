"""
Ternary Search Algorithm - Iterative and Recursive Implementations

Divides the search range into 3 parts instead of 2, and recursively or iteratively
eliminates 2/3 of the array in each step.

Time Complexity  : O(log3 N)
Space Complexity : O(1) for iterative, O(log3 N) for recursive
"""

from __future__ import annotations


def linear_search(start: int, end: int, array: list[int | float | str], target) -> int:
    """
    Fallback linear search when search window is small.

    >>> linear_search(0, 4, [1, 2, 3, 4], 3)
    2
    >>> linear_search(0, 2, ["a", "b", "c"], "b")
    1
    >>> linear_search(0, 3, [0.1, 0.2, 0.3], 0.4)
    -1
    """
    for i in range(start, end):
        if array[i] == target:
            return i
    return -1


def ternary_search_iterative(array: list[int | float | str], target) -> int:
    """
    Iterative ternary search algorithm for sorted arrays.

    >>> ternary_search_iterative([1, 3, 5, 7, 9], 7)
    3
    >>> ternary_search_iterative([1, 3, 5, 7, 9], 2)
    -1
    >>> ternary_search_iterative([], 4)
    -1
    """
    left = 0
    right = len(array) - 1
    threshold = 10

    while left <= right:
        if right - left < threshold:
            return linear_search(left, right + 1, array, target)

        one_third = left + (right - left) // 3
        two_third = right - (right - left) // 3

        if array[one_third] == target:
            return one_third
        elif array[two_third] == target:
            return two_third
        elif target < array[one_third]:
            right = one_third - 1
        elif target > array[two_third]:
            left = two_third + 1
        else:
            left = one_third + 1
            right = two_third - 1

    return -1


def ternary_search_recursive(
    array: list[int | float | str],
    target,
    left: int = 0,
    right: int | None = None,
    threshold: int = 10,
) -> int:
    """
    Recursive ternary search algorithm.

    >>> ternary_search_recursive([1, 3, 5, 7, 9], 7)
    3
    >>> ternary_search_recursive(["a", "b", "c", "d"], "c")
    2
    >>> ternary_search_recursive([], 1)
    -1
    """
    if right is None:
        right = len(array) - 1

    if left > right:
        return -1

    if right - left < threshold:
        return linear_search(left, right + 1, array, target)

    one_third = left + (right - left) // 3
    two_third = right - (right - left) // 3

    if array[one_third] == target:
        return one_third
    elif array[two_third] == target:
        return two_third
    elif target < array[one_third]:
        return ternary_search_recursive(array, target, left, one_third - 1, threshold)
    elif target > array[two_third]:
        return ternary_search_recursive(array, target, two_third + 1, right, threshold)
    else:
        return ternary_search_recursive(
            array, target, one_third + 1, two_third - 1, threshold
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        raw_input = input("\nEnter sorted numbers separated by commas: ").strip()
        collection = [int(x) for x in raw_input.split(",")]
        assert collection == sorted(collection), (
            "Input must be sorted in ascending order."
        )
        target = int(input("Enter the number to search: "))

        result_iter = ternary_search_iterative(collection, target)
        result_rec = ternary_search_recursive(collection, target)

        if result_iter != -1:
            print(f"Iterative Search: Found {target} at index {result_iter}")
            print(f"Recursive Search: Found {target} at index {result_rec}")
        else:
            print(f"{target} not found in the list.")
    except Exception as e:
        print(f"Error: {e}")
