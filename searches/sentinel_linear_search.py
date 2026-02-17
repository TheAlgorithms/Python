"""
This is pure Python implementation of sentinel linear search algorithm

For doctests run following command:
python -m doctest -v sentinel_linear_search.py
or
python3 -m doctest -v sentinel_linear_search.py

For manual testing run:
python sentinel_linear_search.py
"""


def sentinel_linear_search(sequence, target):
    """Pure implementation of sentinel linear search algorithm in Python

    :param sequence: a mutable list with comparable items. Note: this function
        temporarily mutates the input list by appending and then removing the
        target value, but the list is restored to its original state.
    :param target: item value to search
    :return: index of found item or None if item is not found

    The sentinel linear search algorithm works by appending the target value to the
    end of the list before searching. This eliminates the need for boundary checking
    during the loop, as the search is guaranteed to find the target (at minimum, at
    the end where the sentinel is placed). The input list is restored after the search.

    Examples:
    >>> sentinel_linear_search([0, 5, 7, 10, 15], 0)
    0

    >>> sentinel_linear_search([0, 5, 7, 10, 15], 15)
    4

    >>> sentinel_linear_search([0, 5, 7, 10, 15], 5)
    1

    >>> sentinel_linear_search([0, 5, 7, 10, 15], 6)

    >>> sentinel_linear_search([1], 1)
    0

    >>> sentinel_linear_search([1], 99)

    >>> sentinel_linear_search([], 5)

    >>> sentinel_linear_search([3, 1, 4, 1, 5, 9, 2, 6], 9)
    5

    >>> sentinel_linear_search([3, 1, 4, 1, 5, 9, 2, 6], 1)
    1

    >>> sentinel_linear_search(['a', 'b', 'c', 'd'], 'c')
    2

    >>> sentinel_linear_search(['a', 'b', 'c', 'd'], 'z')

    >>> sentinel_linear_search([1.5, 2.7, 3.14, 4.0], 3.14)
    2

    >>> sentinel_linear_search([1.5, 2.7, 3.14, 4.0], 2.5)

    >>> sentinel_linear_search([-10, -5, 0, 5, 10], -5)
    1

    >>> sentinel_linear_search([-10, -5, 0, 5, 10], 0)
    2

    """
    sequence.append(target)

    index = 0
    while sequence[index] != target:
        index += 1

    sequence.pop()

    if index == len(sequence):
        return None

    return index


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item) for item in user_input.split(",")]

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = sentinel_linear_search(sequence, target)
    if result is not None:
        print(f"{target} found at positions: {result}")
    else:
        print("Not found")
