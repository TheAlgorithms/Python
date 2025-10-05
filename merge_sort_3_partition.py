"""
Three-way (ternary) merge sort.

Doctests:
python -m doctest -v three_way_merge_sort.py
or
python3 -m doctest -v three_way_merge_sort.py

Manual test:
python three_way_merge_sort.py
"""

from typing import List, Any


def merge_sort(collection: List[Any]) -> List[Any]:
    """
    Sorts a list using a three-way merge sort (split into 3 parts).

    :param collection: A mutable ordered collection with comparable items.
    :return: The same collection ordered in ascending order.

    Time Complexity: O(n log_3 n) ≈ O(n log n)
    Space Complexity: O(n)

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> merge_sort([9,1,8,2,7,3,6,4,5])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    def merge_three(left: List[Any], middle: List[Any], right: List[Any]) -> List[Any]:
        """
        Merge three sorted lists into a single sorted list.

        Uses indices  for efficiency.
        """
        i = j = k = 0
        nL, nM, nR = len(left), len(middle), len(right)
        result: List[Any] = []

        # While all three have elements, pick the smallest of the three
        while i < nL and j < nM and k < nR:
            if left[i] <= middle[j] and left[i] <= right[k]:
                result.append(left[i]); i += 1
            elif middle[j] <= left[i] and middle[j] <= right[k]:
                result.append(middle[j]); j += 1
            else:
                result.append(right[k]); k += 1

        # Now at least one list is exhausted. Merge remaining two (pairwise)
        # Merge left & middle
        while i < nL and j < nM:
            if left[i] <= middle[j]:
                result.append(left[i]); i += 1
            else:
                result.append(middle[j]); j += 1

        # Merge middle & right
        while j < nM and k < nR:
            if middle[j] <= right[k]:
                result.append(middle[j]); j += 1
            else:
                result.append(right[k]); k += 1

        # Merge left & right
        while i < nL and k < nR:
            if left[i] <= right[k]:
                result.append(left[i]); i += 1
            else:
                result.append(right[k]); k += 1

        # Append leftovers (at most one of the three loops below will add many)
        while i < nL:
            result.append(left[i]); i += 1
        while j < nM:
            result.append(middle[j]); j += 1
        while k < nR:
            result.append(right[k]); k += 1

        return result

    # Base case
    n = len(collection)
    if n <= 1:
        return collection[:]

    # Split into three roughly equal parts
    third = n // 3
    mid1 = third - 1  # last index of first part (not used directly)
    # compute split indices for slicing
    cut1 = third
    cut2 = 2 * third + (1 if n % 3 == 2 else 0)  # distribute remainder to the second cut

    left = collection[:cut1]
    middle = collection[cut1:cut2]
    right = collection[cut2:]

    # Recursively sort the three parts
    sorted_left = merge_sort(left)
    sorted_middle = merge_sort(middle)
    sorted_right = merge_sort(right)

    # Merge three sorted parts and return
    return merge_three(sorted_left, sorted_middle, sorted_right)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        if not user_input:
            print("[]")
        else:
            unsorted = [int(item) for item in user_input.split(",")]
            sorted_list = merge_sort(unsorted)
            print(*sorted_list, sep=",")
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
