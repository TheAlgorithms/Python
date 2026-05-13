def insertion_sort(collection: list[int]) -> list[int]:
    """
    Sorts a list in ascending order using the insertion sort algorithm.

    :param collection: A list of integers to be sorted.
    :return: The sorted list.

    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> insertion_sort([])
    []

    >>> insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    START_INDEX = 1          # Magic number replaced with constant
    length = len(collection)

    for insert_index in range(START_INDEX, length):
        current_value = collection[insert_index]
        position = insert_index

        while position > 0 and collection[position - 1] > current_value:
            collection[position] = collection[position - 1]
            position -= 1

        collection[position] = current_value

    return collection


def get_user_input() -> list[int]:
    """Helper function to get list from user input."""
    user_input = input("Enter numbers separated by a comma:\n").strip()
    return [int(item) for item in user_input.split(",")]


if __name__ == "__main__":
    unsorted = get_user_input()
    sorted_list = insertion_sort(unsorted)
    print("Sorted List:", sorted_list)
