"""
This is pure Python implementation of sentinel linear search algorithm.

The sentinel linear search improves on linear search by adding a sentinel
(target value) at the end of the list to avoid bounds checking on each iteration.

For doctests run following command:
python -m doctest -v sentinel_linear_search.py
or
python3 -m doctest -v sentinel_linear_search.py

For manual testing run:
python sentinel_linear_search.py
"""
from collections.abc import Sequence
from typing import Any


def sentinel_linear_search(sequence: list, target: Any) -> int | None:
    """Pure implementation of sentinel linear search algorithm in Python.

    Args:
        sequence: A list of comparable items. Note: this list will be modified
                  temporarily by appending the target value (restored before return).
        target: The item value to search for.

    Returns:
        The index of the found item, or None if the item is not found.

    Examples:
    >>> sentinel_linear_search([0, 5, 7, 10, 15], 0)
    0
    >>> sentinel_linear_search([0, 5, 7, 10, 15], 15)
    4
    >>> sentinel_linear_search([0, 5, 7, 10, 15], 5)
    1
    >>> sentinel_linear_search([0, 5, 7, 10, 15], 6) is None
    True
    """
    sequence.append(target)

    index = 0
    while sequence[index] != target:
        index += 1

    sequence.pop()

    if index >= len(sequence):
        return None

    return index


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item) for item in user_input.split(",")]

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = sentinel_linear_search(sequence, target)
    if result is not None:
        print(f"{target} found at position: {result}")
    else:
        print("Not found")
