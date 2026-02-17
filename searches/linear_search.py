"""
This is pure Python implementation of linear search algorithm

For doctests run following command:
python3 -m doctest -v linear_search.py

For manual testing run:
python3 linear_search.py
"""


def linear_search(sequence: list, target: int) -> int:
    """A pure Python implementation of a linear search algorithm

    Linear search iterates through a collection sequentially until it finds the
    target element or reaches the end of the collection. It works on both sorted
    and unsorted collections.

    :param sequence: a collection with comparable items (as sorted items not required
        in Linear Search)
    :param target: item value to search
    :return: index of found item or -1 if item is not found

    Examples:
    >>> linear_search([0, 5, 7, 10, 15], 0)
    0
    >>> linear_search([0, 5, 7, 10, 15], 15)
    4
    >>> linear_search([0, 5, 7, 10, 15], 5)
    1
    >>> linear_search([0, 5, 7, 10, 15], 6)
    -1

    >>> linear_search([], 5)
    -1

    >>> linear_search([42], 42)
    0

    >>> linear_search([42], 99)
    -1

    >>> linear_search([3, 1, 4, 1, 5, 9, 2, 6], 1)
    1

    >>> linear_search([3, 1, 4, 1, 5, 9, 2, 6], 9)
    5

    >>> linear_search([10, 20, 30, 40, 50], 30)
    2

    >>> linear_search([5, 5, 5, 5], 5)
    0

    >>> linear_search([-5, -2, 0, 3, 7], -5)
    0

    >>> linear_search([-5, -2, 0, 3, 7], 0)
    2

    >>> linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    9

    >>> linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    0

    >>> linear_search([100, 200, 300, 400], 250)
    -1
    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return -1


def rec_linear_search(sequence: list, low: int, high: int, target: int) -> int:
    """
    A pure Python implementation of a recursive linear search algorithm

    This is the recursive variant of linear search. It searches from both bounds
    (low and high) converging toward the middle, checking both ends simultaneously.

    :param sequence: a collection with comparable items (as sorted items not required
        in Linear Search)
    :param low: Lower bound of the array (starting index)
    :param high: Higher bound of the array (ending index)
    :param target: The element to be found
    :return: Index of the key or -1 if key not found

    Examples:
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 0)
    0
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 700)
    4
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 30)
    1
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, -6)
    -1

    >>> rec_linear_search([42], 0, 0, 42)
    0

    >>> rec_linear_search([42], 0, 0, 99)
    -1

    >>> rec_linear_search([1, 2, 3, 4, 5], 0, 4, 1)
    0

    >>> rec_linear_search([1, 2, 3, 4, 5], 0, 4, 5)
    4

    >>> rec_linear_search([1, 2, 3, 4, 5], 0, 4, 3)
    2

    >>> rec_linear_search([10, 20, 30, 40, 50, 60], 0, 5, 40)
    3

    >>> rec_linear_search([-5, -2, 0, 3, 7], 0, 4, -5)
    0

    >>> rec_linear_search([-5, -2, 0, 3, 7], 0, 4, 7)
    4

    >>> rec_linear_search([5, 5, 5, 5, 5], 0, 4, 5)
    0

    >>> rec_linear_search([1, 2, 3, 4, 5], 0, 4, 0)
    -1
    """
    if not (0 <= high < len(sequence) and 0 <= low < len(sequence)):
        raise Exception("Invalid upper or lower bound!")
    if high < low:
        return -1
    if sequence[low] == target:
        return low
    if sequence[high] == target:
        return high
    return rec_linear_search(sequence, low + 1, high - 1, target)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item.strip()) for item in user_input.split(",")]

    target = int(input("Enter a single number to be found in the list:\n").strip())
    result = linear_search(sequence, target)
    if result != -1:
        print(f"linear_search({sequence}, {target}) = {result}")
    else:
        print(f"{target} was not found in {sequence}")
