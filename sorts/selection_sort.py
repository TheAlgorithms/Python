def selection_sort(collection: list[int]) -> list[int]:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    :param collection: A list of integers to be sorted.
    :return: The sorted list.

    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    for i in range(length - 1):
        min_index = _find_minimum_index(collection, i, length)
        if min_index != i:
            collection[i], collection[min_index] = collection[min_index], collection[i]
    return collection


def _find_minimum_index(collection: list[int], start: int, length: int) -> int:
    """
    Find the index of the minimum element in the unsorted portion.
    """
    min_index = start
    for k in range(start + 1, length):
        if collection[k] < collection[min_index]:
            min_index = k
    return min_index


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    sorted_list = selection_sort(unsorted)
    print("Sorted List:", sorted_list)
