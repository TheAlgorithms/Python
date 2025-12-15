"""
PowerSort - An adaptive merge sort algorithm.

PowerSort is an adaptive, stable sorting algorithm that efficiently handles
partially ordered data by optimally merging existing runs (consecutive sequences
of sorted elements) in the input. It was developed by J. Ian Munro and Sebastian
Wild and has been integrated into Python's standard library since version 3.11.

The algorithm works by:
1. Detecting naturally occurring runs (ascending or descending sequences)
2. Using a power-based merge strategy to determine optimal merge order
3. Maintaining a stack of runs and merging based on calculated node powers

Time Complexity: O(n log n) worst case, O(n) for nearly sorted data
Space Complexity: O(n) for merge buffer

References:
- https://en.wikipedia.org/wiki/Powersort
- https://arxiv.org/abs/1805.04154 (Original paper by Munro and Wild)

For doctests run:
python -m doctest -v power_sort.py

For manual testing run:
python power_sort.py
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


def _find_run(
    arr: list, start: int, end: int, key: Callable[[Any], Any] | None = None
) -> int:
    """
    Detect a run (ascending or descending sequence) starting at 'start'.


    If the run is descending, reverse it in-place to make it ascending.
    Returns the end index (exclusive) of the detected run.


    Args:
        arr: The list to search in
        start: Starting index of the run
        end: End index (exclusive) of the search range
        key: Optional key function for comparisons


    Returns:
        End index (exclusive) of the detected run


    >>> arr = [3, 2, 1, 4, 5, 6]
    >>> _find_run(arr, 0, 6)
    3
    >>> arr
    [1, 2, 3, 4, 5, 6]
    >>> arr = [1, 2, 3, 2, 1]
    >>> _find_run(arr, 0, 5)
    3
    >>> arr
    [1, 2, 3, 2, 1]
    """
    if start >= end - 1:
        return start + 1

    key_func = key if key else lambda element: element
    run_end = start + 1

    # Check if run is ascending or descending
    if key_func(arr[run_end]) < key_func(arr[start]):
        # Descending run
        while run_end < end and key_func(arr[run_end]) < key_func(arr[run_end - 1]):
            run_end += 1
        # Reverse the descending run to make it ascending
        arr[start:run_end] = reversed(arr[start:run_end])
    else:
        # Ascending run
        while run_end < end and key_func(arr[run_end]) >= key_func(arr[run_end - 1]):
            run_end += 1

    return run_end


def _node_power(total_length: int, b1: int, n1: int, b2: int, n2: int) -> int:
    """
    Calculate the node power for two adjacent runs.


    This determines the merge priority in the stack. The power is the smallest
    integer p such that floor(a * 2^p) != floor(b * 2^p), where:
    - a = (b1 + n1/2) / n
    - b = (b2 + n2/2) / n


    Args:
        total_length: Total length of the array
        b1: Start index of first run
        n1: Length of first run
        b2: Start index of second run
        n2: Length of second run


    Returns:
        The calculated node power


    >>> _node_power(100, 0, 25, 25, 25)
    2
    >>> _node_power(100, 0, 50, 50, 50)
    1
    """
    # Calculate midpoints: a = (b1 + n1/2) / total_length,
    # b = (b2 + n2/2) / total_length
    # To avoid floating point, we work with a = (2*b1 + n1) / (2*total_length) and
    # b = (2*b2 + n2) / (2*total_length)
    # We want smallest p where floor(a * 2^p) != floor(b * 2^p)
    # This is floor((2*b1 + n1) * 2^p / (2*total_length)) !=
    # floor((2*b2 + n2) * 2^p / (2*total_length))

    a = 2 * b1 + n1
    b = 2 * b2 + n2
    two_n = 2 * total_length

    # Find smallest power p where floor(a * 2^p / two_n) !=
    # floor(b * 2^p / two_n)
    power = 0
    while (a * (1 << power)) // two_n == (b * (1 << power)) // two_n:
        power += 1

    return power


def _merge(
    arr: list,
    start1: int,
    end1: int,
    end2: int,
    key: Callable[[Any], Any] | None = None,
) -> None:
    """
    Merge two adjacent sorted runs in-place using auxiliary space.


    Merges arr[start1:end1] with arr[end1:end2].


    Args:
        arr: The list containing the runs
        start1: Start index of first run
        end1: End index of first run (start of second run)
        end2: End index of second run
        key: Optional key function for comparisons


    >>> arr = [1, 3, 5, 2, 4, 6]
    >>> _merge(arr, 0, 3, 6)
    >>> arr
    [1, 2, 3, 4, 5, 6]
    >>> arr = [5, 6, 7, 1, 2, 3]
    >>> _merge(arr, 0, 3, 6)
    >>> arr
    [1, 2, 3, 5, 6, 7]
    """
    key_func = key if key else lambda element: element

    # Copy the runs to temporary storage
    left = arr[start1:end1]
    right = arr[end1:end2]

    i = j = 0
    k = start1

    # Merge the two runs
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def power_sort(
    collection: list,
    *,
    key: Callable[[Any], Any] | None = None,
    reverse: bool = False,
) -> list:
    """
    Sort a list using the PowerSort algorithm.


    PowerSort is an adaptive merge sort that detects existing runs in the data
    and uses a power-based merging strategy for optimal performance.


    Args:
        collection: A mutable ordered collection with comparable items
        key: Optional function to extract comparison key from each element
        reverse: If True, sort in descending order


    Returns:
        The same collection ordered according to the parameters


    Time Complexity: O(n log n) worst case, O(n) for nearly sorted data
    Space Complexity: O(n)


    Examples:
    >>> power_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> power_sort([])
    []
    >>> power_sort([1])
    [1]
    >>> power_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> power_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> power_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> power_sort([3, 1, 4, 1, 5, 9, 2, 6, 5])
    [1, 1, 2, 3, 4, 5, 5, 6, 9]
    >>> power_sort(['banana', 'apple', 'cherry'])
    ['apple', 'banana', 'cherry']
    >>> power_sort([3.14, 2.71, 1.41, 1.73])
    [1.41, 1.73, 2.71, 3.14]
    >>> power_sort([5, 2, 8, 1, 9], reverse=True)
    [9, 8, 5, 2, 1]
    >>> power_sort(['apple', 'pie', 'a', 'longer'], key=len)
    ['a', 'pie', 'apple', 'longer']
    >>> power_sort([(1, 'b'), (2, 'a'), (1, 'a')], key=lambda x: x[0])
    [(1, 'b'), (1, 'a'), (2, 'a')]
    >>> power_sort([1, 2, 3, 2, 1, 2, 3, 4])
    [1, 1, 2, 2, 2, 3, 3, 4]
    >>> result = power_sort(list(range(100)))
    >>> result == list(range(100))
    True
    >>> result = power_sort(list(reversed(range(50))))
    >>> result == list(range(50))
    True
    """
    if len(collection) <= 1:
        return collection

    # Make a copy to avoid modifying the original if it's immutable
    arr = list(collection)
    total_length = len(arr)

    # Adjust key function for reverse sorting
    needs_final_reverse = False
    if reverse:
        if key:
            original_key = key

            def reverse_key(element: Any) -> Any:
                """
                Reverse key function for numeric values.

                Args:
                    element: The element to process

                Returns:
                    Negated value for numeric types, original value otherwise

                >>> reverse_key(5)
                -5
                >>> reverse_key('hello')
                'hello'
                """
                val = original_key(element)
                if isinstance(val, int | float):
                    return -val
                return val

            key = reverse_key
            needs_final_reverse = True
        else:

            def reverse_cmp(element: Any) -> Any:
                """
                Reverse comparison function for numeric values.

                Args:
                    element: The element to process

                Returns:
                    Negated value for numeric types, original value otherwise

                >>> reverse_cmp(10)
                -10
                >>> reverse_cmp('test')
                'test'
                """
                if isinstance(element, int | float):
                    return -element
                return element

            key = reverse_cmp
            needs_final_reverse = True

    # Stack to hold runs: each entry is (start_index, length, power)
    stack: list[tuple[int, int, int]] = []

    start = 0
    while start < total_length:
        # Find the next run
        run_end = _find_run(arr, start, total_length, key)
        run_length = run_end - start

        # Calculate power for this run
        if len(stack) == 0:
            power = 0
        else:
            prev_start, prev_length, _ = stack[-1]
            power = _node_power(
                total_length, prev_start, prev_length, start, run_length
            )

        # Merge runs from stack based on power comparison
        while len(stack) > 0 and stack[-1][2] >= power:
            # Merge the top run with the current run
            prev_start, prev_length, _ = stack.pop()
            _merge(arr, prev_start, prev_start + prev_length, run_end, key)

            # Update current run to include the merged run
            start = prev_start
            run_length = run_end - start

            # Recalculate power
            if len(stack) == 0:
                power = 0
            else:
                prev_prev_start, prev_prev_length, _ = stack[-1]
                power = _node_power(
                    total_length, prev_prev_start, prev_prev_length, start, run_length
                )

        # Push current run onto stack
        stack.append((start, run_length, power))
        start = run_end

    # Merge all remaining runs on the stack
    while len(stack) > 1:
        start2, length2, _ = stack.pop()
        start1, length1, _ = stack.pop()
        _merge(arr, start1, start1 + length1, start2 + length2, key)

        # Recalculate power for merged run
        if len(stack) == 0:
            power = 0
        else:
            prev_start, prev_length, _ = stack[-1]
            merged_length = start2 + length2 - start1
            power = _node_power(
                total_length, prev_start, prev_length, start1, merged_length
            )

        stack.append((start1, start2 + length2 - start1, power))

    # Handle reverse sorting for non-numeric types
    if (
        reverse
        and needs_final_reverse
        and key
        and len(arr) > 0
        and not isinstance(arr[0], int | float)
    ):
        # For non-numeric types, we need to reverse the final result
        # Check if we used numeric negation or not
        arr.reverse()

    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("\nPowerSort Interactive Testing")
    print("=" * 40)

    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        if user_input == "":
            unsorted = []
        else:
            unsorted = [int(item.strip()) for item in user_input.split(",")]

        print(f"\nOriginal: {unsorted}")
        sorted_list = power_sort(unsorted)
        print(f"Sorted:   {sorted_list}")

        # Test reverse
        sorted_reverse = power_sort(unsorted, reverse=True)
        print(f"Reverse:  {sorted_reverse}")

    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
