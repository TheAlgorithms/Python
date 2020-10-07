"""
Pure Python implementation of a binary search algorithm.

For doctests run following command:
python3 -m doctest -v simple_binary_search.py

For manual testing run:
python3 simple_binary_search.py
"""
from __future__ import annotations


def binary_search(a_list: list[int], item: int) -> bool:
    """
    >>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> print(binary_search(test_list, 3))
    False
    >>> print(binary_search(test_list, 13))
    True
    >>> print(binary_search([4, 4, 5, 6, 7], 4))
    True
    >>> print(binary_search([4, 4, 5, 6, 7], -10))
    False
    >>> print(binary_search([-18, 2], -18))
    True
    >>> print(binary_search([5], 5))
    True
    >>> print(binary_search(['a', 'c', 'd'], 'c'))
    True
    >>> print(binary_search(['a', 'c', 'd'], 'f'))
    False
    >>> print(binary_search([], 1))
    False
    >>> print(binary_search([-.1, .1 , .8], .1))
    True
    >>> binary_search(range(-5000, 5000, 10), 80)
    True
    >>> binary_search(range(-5000, 5000, 10), 1255)
    False
    >>> binary_search(range(0, 10000, 5), 2)
    False
    """
    if len(a_list) == 0:
        return False
    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    if item < a_list[midpoint]:
        return binary_search(a_list[:midpoint], item)
    else:
        return binary_search(a_list[midpoint + 1 :], item)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item.strip()) for item in user_input.split(",")]
    target = int(input("Enter the number to be found in the list:\n").strip())
    not_str = "" if binary_search(sequence, target) else "not "
    print(f"{target} was {not_str}found in {sequence}")
