from typing import List


def library_sort(collection: List[int], reverse: bool = False) -> List[int]:
    """
    A pure Python implementation of library sort (also called gapped insertion sort).

    It w orks like insertion sort, but leaves empty gaps in the array so a new item can
    be placed without shifting everything after it. When the gaps fill up, the array is
    rebalanced. Expected time is O(n log n).

    Reference: https://en.wikipedia.org/wiki/Library_sort

    For doctests run the following command:
    python3 -m doctest -v library_sort.py

    For manual testing run:
    python3 library_sort.py
    Time Complexity: O(N log N) average, O(N^2) worst-case
    Space Complexity: O(N)

    Examples:
    >>> library_sort([5, 2, 9, 1, 5, 6])
    [1, 2, 5, 5, 6, 9]
    >>> library_sort([3, 1, 4, 1, 5, 9, 2])
    [1, 1, 2, 3, 4, 5, 9]
    >>> library_sort([])
    []
    >>> library_sort([1])
    [1]
    >>> library_sort([5, 2, 9, 1], reverse=True)
    [9, 5, 2, 1]
    """
    if not collection:
        return []

    n = len(collection)
    gapped = [None] * (2 * n)
    gapped[0] = collection[0]

    for i in range(1, n):
        val = collection[i]
        valid_indices = [idx for idx, x in enumerate(gapped) if x is not None]
        valid_vals = [gapped[idx] for idx in valid_indices]

        low, high = 0, len(valid_vals) - 1
        pos = len(valid_vals)
        while low <= high:
            mid = (low + high) // 2
            if valid_vals[mid] >= val:
                pos = mid
                high = mid - 1
            else:
                low = mid + 1

        if pos == len(valid_vals):
            target_idx = valid_indices[-1] + 1 if valid_indices else 0
        else:
            target_idx = valid_indices[pos]

        if target_idx < len(gapped) and gapped[target_idx] is None:
            gapped[target_idx] = val
        else:
            current_elements = [x for x in gapped if x is not None]
            current_elements.append(val)
            current_elements.sort()

            gapped = [None] * (2 * len(current_elements))
            step = len(gapped) // len(current_elements)
            for idx, elem in enumerate(current_elements):
                gapped[idx * step] = elem

    sorted_arr = [x for x in gapped if x is not None]
    if reverse:
        sorted_arr.reverse()
    return sorted_arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("\nLibrarySort Interactive Testing")
    print("=" * 40)

    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        if user_input == "":
            unsorted = []
        else:
            unsorted = [int(item.strip()) for item in user_input.split(",")]

        print(f"\nOriginal: {unsorted}")
        sorted_list = library_sort(unsorted)
        print(f"Sorted:   {sorted_list}")

        # Test reverse
        sorted_reverse = library_sort(unsorted, reverse=True)
        print(f"Reverse:  {sorted_reverse}")

    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
