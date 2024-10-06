def reversort(collection: list[int]) -> list[int]:
    """
    Sorts a list in ascending order using the Reversort algorithm.

    :param collection: A list of integers to be sorted.
    :return: The sorted list.

    Examples:
    >>> reversort([4, 2, 1, 3])
    [1, 2, 3, 4]

    >>> reversort([5, 6, 3, 2, 8])
    [2, 3, 5, 6, 8]

    >>> reversort([7])
    [7]
    """

    length = len(collection)
    for i in range(length - 1):
        # Find the index of the minimum element in the subarray collection[i:]
        j = min(range(i, length), key=collection.__getitem__)
        # Reverse the subarray collection[i:j+1]
        collection[i:j + 1] = collection[i:j + 1][::-1]
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    sorted_list = reversort(unsorted)
    print("Sorted List:", sorted_list)
