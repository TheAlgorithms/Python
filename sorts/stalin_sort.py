"""
This is a pure Python implementation of the stalin sort algorithm.
Stalin sort iterates over the list, comparing each element with the
previous one, and removes any that are out of order.
More information at: https://github.com/gustavo-depaula/stalin-sort

"""


def stalin_sort(collection: list) -> list:
    """Pure python implementation of the stalin sort algorithm in Python
    :param collection: a list of comparable items
    :return: all of the items that were in order
    Examples:
    >>> stalin_sort([0, 5, 3, 2, 2])
    [0, 5]
    >>> stalin_sort([])
    []
    >>> stalin_sort([-2, -5, -45])
    [-2]
    """
    if collection == []:
        return []
    largest = collection[0]
    removed = 0
    for i in range(len(collection)):
        if collection[i - removed] < largest:
            collection.pop(i - removed)
            removed += 1
        else:
            largest = collection[i - removed]
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(stalin_sort(unsorted))
