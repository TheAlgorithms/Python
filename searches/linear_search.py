"""
This is a pure Python implementation of the linear search algorithm.

For doctests run following command:
python3 -m doctest -v linear_search.py

For manual testing run:
python3 linear_search.py
"""
def linear_search(sequence: list, target: int) -> int:
    """... existing docstring ..."""

    if not sequence:
        return -1


def linear_search(sequence: list, target: int) -> int:
    """A pure Python implementation of a linear search algorithm

    :param sequence: a collection with comparable items (No sorting required)
    :param target: Value to search for
    :return: index of target if found, else -1

    Examples:
    >>> linear_search([0, 5, 7, 10, 15], 0)
    0
    >>> linear_search([0, 5, 7, 10, 15], 6)
    -1
    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return -1


def rec_linear_search(sequence: list, low: int, high: int, target: int) -> int:
    """
    Recursive linear search algorithm

    :param sequence: Collection of comparable items (no sorting required)
    :param low: Lower index bound
    :param high: Higher index bound
    :param target: Value to search for
    :return: Index of the target if found, else -1

    Examples:
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 0)
    0
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 700)
    4
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 30)
    1
    >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, -6)
    -1
    """
    if not (0 <= high < len(sequence) and 0 <= low < len(sequence)):
        raise ValueError("Invalid upper or lower bound!")
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
