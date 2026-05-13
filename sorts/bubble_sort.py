def bubble_sort(collection: list[int]) -> list[int]:
    """
    Sorts a list in ascending order using the bubble sort algorithm.

    :param collection: A list of integers to be sorted.
    :return: The sorted list.

    Examples:
    >>> bubble_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    for i in range(length):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True
        if not swapped:
            break
    return collection


def get_user_input() -> list[int]:
    """Helper function to get list from user input."""
    user_input = input("Enter numbers separated by a comma:\n").strip()
    return [int(item) for item in user_input.split(",")]


if __name__ == "__main__":
    unsorted = get_user_input()
    sorted_list = bubble_sort(unsorted)
    print("Sorted List:", sorted_list)
