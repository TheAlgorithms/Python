"""
This is a pure Python implementation of the pancake sort algorithm
For doctests run following command:
python3 -m doctest -v pancake_sort.py
or
python -m doctest -v pancake_sort.py
For manual testing run:
python pancake_sort.py
"""

from __future__ import annotations
from collections.abc import MutableSequence


def pancake_sort(arr: MutableSequence[int]) -> MutableSequence[int]:
    """Sort Array with Pancake Sort.
    :param arr: Collection containing comparable items
    :return: Collection ordered in ascending order of items
    Examples:
    >>> pancake_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> pancake_sort([])
    []
    >>> pancake_sort([-2, -5, -45])
    [-45, -5, -2]
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    cur = len(arr)
    while cur > 1:
        # Find the maximum number in arr
        mi = arr.index(max(arr[0:cur]))
        # Reverse from 0 to mi
        arr = arr[mi::-1] + arr[mi + 1 : len(arr)]
        # Reverse whole list
        arr = arr[cur - 1 :: -1] + arr[cur : len(arr)]
        cur -= 1
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
