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


def rec_linear_search(sequence: list, low: int, high: int, target: int) -> int:
    """
    A pure Python implementation of a recursive linear search algorithm

    :param sequence: a collection with comparable items (as sorted items not required
        in Linear Search)
    :param low: Lower bound of the array
    :param high: Higher bound of the array
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
    """
    """
    EXPLANATION FOR RECURSIVE APPROACH:
    We iterate through the array from the end by decrementing the size variable and recursively calling the function searchElement(). 
    If the size variable becomes less than zero it means the element is not present in the array and we return "-1." 
    If a match is found, we return the size variable which is the index of the found element.
    
    NOTE:For duplicate element index of last matched element will be returned due to recursion.
    Time complexity :O(N)
    Space complexity:O(1)
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
