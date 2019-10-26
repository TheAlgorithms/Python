"""
This is a pure python implementation of the insertion sort algorithm

For doctests run following command:
python -m doctest -v insertion_sort.py
or
python3 -m doctest -v insertion_sort.py

For manual testing run:
python insertion_sort.py
"""


def insertion_sort(collection):
    """Pure implementation of the insertion sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> insertion_sort([])
    []

    >>> insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    for i in range(1, len(collection)):
        insert_value = collection[i]
        j = i - 1
        while j >= 0 and insert_value < collection[j]:
            collection[j + 1] = collection[j]
            j -= 1
        collection[j + 1] = insert_value
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(insertion_sort(unsorted))
