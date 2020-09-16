"""
Pure Python implementation of the binary search algorithm.

For doctests run following command:
python -m doctest -v simple_binary_search.py
or
python3 -m doctest -v simple_binary_search.py

For manual testing run:
python simple_binary_search.py
"""
from typing import List


def binary_search(a_list: List[int], item: int) -> bool:
    """
    Pure python implementation of a binary search of a number is in a list.

    >>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> print(binary_search(test_list, 3))
    False
    >>> print(binary_search(test_list, 13))
    True
    """
    if len(a_list) == 0:
        return False
    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    if item < a_list[midpoint]:
        return binary_search(a_list[:midpoint], item)
    else:
        return binary_search(a_list[midpoint + 1:], item)


if __name__ == "__main__":
    user_input: str = input("Enter numbers separated by comma:\n").strip()
    sequence: List[int] = [int(item.strip()) for item in user_input.split(",")]
    target_str = input("Enter the number to be found in the list:\n").strip()
    target: int = int(target_str)
    result = binary_search(sequence, target)
    if result:
        print(f"{target} was found in {sequence}")
    else:
        print(f"{target} was not found in {sequence}")
