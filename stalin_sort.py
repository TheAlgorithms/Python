"""
This is a pure Python implementation of the stalin sort algorithm,
inspired by the dictator of the former soviet union Josef Stalin.

This sorting algorithm sorts a collection of elements by deleting
every element that is not in order resulting in a sorted collection.

For manual testing run:
python stalin_sort.py
"""

def stalin_sort(collection):
    """A pure Python implementation of stalin sort algorithm

    :param collection: a mutable collection of comparable items
    :return: the same collection ordered by ascending

    Examples:
    >>> stalin_sort([1, 6, 3, 20, 30])
    [1, 6, 20, 30]
    >>> stalin_sort([])
    []
    >>> stalin_sort([-2, 5, -3, 30, 15, 7])
    [-2, 5, 30]
    """
    sorted_collection = [collection[0]]
    for i in collection[1:]:
        if i > sorted_collection[-1]:
            sorted_collection.append(i)
    return sorted_collection

if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(stalin_sort(unsorted))