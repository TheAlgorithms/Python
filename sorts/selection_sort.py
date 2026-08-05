def selection_sort(collection: list[int]) -> list[int]:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Selection sort works by repeatedly finding the minimum element from the
    unsorted portion of the list and placing it at the beginning.

    :param collection: A list of integers to be sorted.
    :return: The sorted list.

    Time Complexity: O(n^2) - where n is the number of elements.
        The algorithm always makes n*(n-1)/2 comparisons regardless of input.
    Space Complexity: O(1) - sorts in place using only a constant amount of extra space.

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
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(selection_sort(unsorted))
