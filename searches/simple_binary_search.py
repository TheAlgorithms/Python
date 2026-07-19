"""
Pure Python implementation of a binary search algorithm.

For doctests run following command:
python3 -m doctest -v simple_binary_search.py

For manual testing run:
python3 simple_binary_search.py
"""

from __future__ import annotations


def binary_search(a_list: list[int], item: int) -> int:
    """
    Returns the leftmost index of `item` in `a_list` if found,
    otherwise returns -1.

    >>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> binary_search(test_list, 3)
    -1
    >>> binary_search(test_list, 13)
    4
    >>> binary_search([4, 4, 5, 6, 7], 4)
    0
    >>> binary_search([4, 4, 5, 6, 7], -10)
    -1
    >>> binary_search([-18, 2], -18)
    0
    >>> binary_search([5], 5)
    0
    >>> binary_search(['a', 'c', 'd'], 'c')
    1
    >>> binary_search(['a', 'c', 'd'], 'f')
    -1
    >>> binary_search([], 1)
    -1
    >>> binary_search([-.1, .1 , .8], .1)
    1
    >>> binary_search(range(-5000, 5000, 10), 80)
    508
    >>> binary_search(range(-5000, 5000, 10), 1255)
    -1
    >>> binary_search(range(0, 10000, 5), 2)
    -1
    """
    low, high = 0, len(a_list) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if a_list[mid] == item:
            result = mid
            high = mid - 1  # keep searching left for duplicates
        elif item < a_list[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item.strip()) for item in user_input.split(",")]
    target = int(input("Enter the number to be found in the list:\n").strip())
    index = binary_search(sequence, target)
    if index != -1:
        print(f"{target} found at index {index} in {sequence}")
    else:
        print(f"{target} was not found in {sequence}")
