"""
This is pure Python implementation of linear search algorithm

For doctests run following command:
python3 -m doctest -v linear_search.py

For manual testing run:
python3 linear_search.py
"""


def linear_search(sequence: list, target: int) -> int:
    """A pure Python implementation of a linear search algorithm

    :param sequence: a collection with comparable items (as sorted items not required
        in Linear Search)
    :param target: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> linear_search([0, 5, 7, 10, 15], 0)
    0
    >>> linear_search([0, 5, 7, 10, 15], 15)
    4
    >>> linear_search([0, 5, 7, 10, 15], 5)
    1
    >>> linear_search([0, 5, 7, 10, 15], 6)
    -1
    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return -1


def rec_linear_search(sequence: list, index: int, target: int) -> int:
    """
    A pure Python implementation of a recursive linear search algorithm

    :param sequence: a collection with comparable items (as sorted items not required
        in Linear Search)
    :param index: intially equal to the size of the array - 1 and represents the element that we are currently checking
    :param target: The element to be found
    :return: Index of the key or -1 if key not found

    Examples:
    >>> rec_linear_search([0, 30, 500, 100, 700], 5, 0)
    0
    >>> rec_linear_search([0, 30, 500, 100, 700], 5, 700)
    4
    >>> rec_linear_search([0, 30, 500, 100, 700], 5, 30)
    1
    >>> rec_linear_search([0, 30, 500, 100, 700], 5, -6)
    -1
    """
    if index < 0:
        raise Exception("Invalid size bound!")
    if index == 0 and sequence[index] != target:
        return -1
    if index >= 0 and sequence[index] == target:
        return index
    rec_linear_search(sequence, index - 1, target)
    return -1


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item.strip()) for item in user_input.split(",")]
    size = len(sequence)
    target = int(input("Enter a single number to be found in the list:\n").strip())
    result = linear_search(sequence, target)
    # result = rec_linear_search(sequence, size-1, target)

    if result != -1:
        print(f"linear_search({sequence}, {target}) = {result}")
    else:
        print(f"{target} was not found in {sequence}")
