"""
This is a pure Python implementation of the Stalin Sort algorithm.
Stalin Sort removes any elements that are out of ascending order, 
leaving only a sorted subsequence of the original list.

For doctests run following command:
python -m doctest -v stalin_sort.py
or
python3 -m doctest -v stalin_sort.py
For manual testing run:
python stalin_sort.py
"""

def stalin_sort(collection: list) -> list:
    """
    Sorts a list by removing elements that are out of order, leaving a sorted subsequence.

    :param collection: A list of comparable items.
    :return: A list containing only elements that maintain ascending order.

    Examples:
    >>> stalin_sort([4, 5, 3, 6, 7, 2, 8])
    [4, 5, 6, 7, 8]
    >>> stalin_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> stalin_sort([5, 4, 3, 2, 1])
    [5]
    >>> stalin_sort([])
    []
    """
    if not collection:
        return []

    sorted_list = [collection[0]]
    for element in collection[1:]:
        if element >= sorted_list[-1]:
            sorted_list.append(element)
    return sorted_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item) for item in user_input.split(",")]
        sorted_list = stalin_sort(unsorted)
        print("Stalin-sorted list:", *sorted_list, sep=", ")
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
