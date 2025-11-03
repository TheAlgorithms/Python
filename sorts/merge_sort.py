"""
This is a pure Python implementation of the merge sort algorithm
with added input validation for safer usage.

For doctests run following command:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py
For manual testing run:
python merge_sort.py
"""

# -----------------------
# Input validation helper
# -----------------------
def _validate_sort_input(arr):
    """
    Ensures the input is a list (or tuple) of comparable elements.

    Raises:
        TypeError: if arr is not a list or tuple.
        ValueError: if list contains uncomparable elements.
    """
    if not isinstance(arr, (list, tuple)):
        raise TypeError("merge_sort() input must be a list or tuple.")
    if len(arr) > 1 and not all(isinstance(x, (int, float, str)) for x in arr):
        raise ValueError("merge_sort() elements must be comparable (int, float, or str).")


def merge_sort(collection: list) -> list:
    """
    Sorts a list using the merge sort algorithm.

    :param collection: A mutable ordered collection with comparable items.
    :return: The same collection ordered in ascending order.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    _validate_sort_input(collection)

    def merge(left: list, right: list) -> list:
        """
        Merge two sorted lists into a single sorted list.

        :param left: Left collection
        :param right: Right collection
        :return: Merged result
        """
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(collection) <= 1:
        return list(collection)

    mid_index = len(collection) // 2
    return merge(
        merge_sort(collection[:mid_index]),
        merge_sort(collection[mid_index:])
    )


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item) for item in user_input.split(",") if item]
        sorted_list = merge_sort(unsorted)
        print("Sorted list:", *sorted_list, sep=" ")
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
    except TypeError as e:
        print(e)
