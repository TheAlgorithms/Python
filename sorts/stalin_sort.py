"""
This is a Python implementation of stalin sort algorithm.
Stalin sort removes the lement that is not in ascending order

For doctests run following command:
python3 -m doctest -v stalin_sort.py

For manual testing run:
python circle_sort.py
"""


def stalin_sort(collection: list) -> list:
    """Pure implementation of stalin sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> stalin_sort([1, 2, 5, 3, 6, 4, 10])
    [1, 2, 5, 6, 10]
    >>> stalin_sort([])
    []
    >>> stalin_sort([6, 5, 4, 3, 2, 1])
    [6]
    """
    i = 1
    while i < len(collection):
        if collection[i] < collection[i - 1]:
            collection.pop(i)
        else:
            i += 1
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(stalin_sort(unsorted))
