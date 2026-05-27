def selection_sort(collection: list[int]) -> list[int]:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    :param collection: A list of integers to be sorted.
    :return: The sorted list.


    Time Complexity: O(n^2) - Due to the nested loops, where n is the length
        of the collection. The outer loop runs n-1 times, and the inner loop
        runs n-i-1 times for each iteration.
    Space Complexity: O(1) - Only a constant amount of extra space is used
        for variables (length, i, min_index, k).
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
        min_index = i
        for k in range(i + 1, length):
            if collection[k] < collection[min_index]:
                min_index = k
        if min_index != i:
            collection[i], collection[min_index] = collection[min_index], collection[i]
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    sorted_list = selection_sort(unsorted)
    print("Sorted List:", sorted_list)
