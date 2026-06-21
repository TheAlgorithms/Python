#!/usr/bin/env python3
"""
Pure Python implementation of the jump search algorithm.
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


def jump_search[T: Comparable](arr: Sequence[T], item: T) -> int:
    """
    Python implementation of the jump search algorithm.
    Return the index if the `item` is found, otherwise return -1.

    >>> jump_search([0, 1, 2, 3, 4, 5], 3)
    3
    >>> jump_search([-5, -2, -1], -1)
    2
    >>> jump_search([0, 5, 10, 20], 8)
    -1
    >>> jump_search(["aa", "bb", "cc", "dd", "ee", "ff"], "ee")
    4
    """
    arr_size = len(arr)
    if arr_size == 0:
        return -1

    block_size = int(math.sqrt(arr_size))
    prev = 0
    step = block_size

    # Finding the block where element is present
    while arr[min(step, arr_size) - 1] < item:
        prev = step
        step += block_size
        if prev >= arr_size:
            return -1

    # Linear search within the block
    while arr[prev] < item:
        prev += 1
        if prev == min(step, arr_size):
            return -1

    if arr[prev] == item:
        return prev
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    if user_input:
        array: list[Any] = [int(i) for i in user_input.split(",")]
        search_item = int(input("Enter the number to be searched:\n"))
        res = jump_search(array, search_item)
        if res == -1:
            print("Number not found!")
        else:
            print(f"Number {search_item} is at index {res}")
