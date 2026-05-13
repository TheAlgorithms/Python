def quick_sort(collection: list[int]) -> list[int]:
    """
    Sorts a list in ascending order using the quick sort algorithm.

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    if len(collection) <= 1:
        return collection

    pivot = collection[len(collection) // 2]
    left = [x for x in collection if x < pivot]
    middle = [x for x in collection if x == pivot]
    right = [x for x in collection if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def get_user_input() -> list[int]:
    """Helper function to get list from user input."""
    user_input = input("Enter numbers separated by a comma:\n").strip()
    return [int(item) for item in user_input.split(",")]


if __name__ == "__main__":
    unsorted = get_user_input()
    sorted_list = quick_sort(unsorted)
    print("Sorted List:", sorted_list)
