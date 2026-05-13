def merge_sort(collection: list[int]) -> list[int]:
    """
    Sorts a list in ascending order using the merge sort algorithm.

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    if len(collection) <= 1:
        return collection

    mid = len(collection) // 2
    left = merge_sort(collection[:mid])
    right = merge_sort(collection[mid:])

    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def get_user_input() -> list[int]:
    """Helper function to get list from user input."""
    user_input = input("Enter numbers separated by a comma:\n").strip()
    return [int(item) for item in user_input.split(",")]


if __name__ == "__main__":
    unsorted = get_user_input()
    sorted_list = merge_sort(unsorted)
    print("Sorted List:", sorted_list)
