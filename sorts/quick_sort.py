"""
This is a pure Python implementation of the quick sort algorithm

For doctests run following command:
python -m doctest -v quick_sort.py
or
python3 -m doctest -v quick_sort.py

For manual testing run:
python quick_sort.py
"""


def quick_sort(collection: list) -> list:
    """
    Pure implementation of quick sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

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
    # Use the last element as the first pivot
    pivot: int = collection.pop()
    # Put elements greater than pivot in greater list
    # Put elements lesser than pivot in lesser list
    greater: list = []
    lesser: list = []
    for element in collection:
        if element > pivot:
            greater.append(element)
        else:
            lesser.append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted))
