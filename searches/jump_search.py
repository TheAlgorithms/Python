"""
Pure Python implementation of the jump search algorithm.
This algorithm iterates through a sorted collection with a step of n^(1/2),
until the element compared is bigger than the one searched.
It will then perform a linear search until it matches the wanted number.
If not found, it returns -1.

https://en.wikipedia.org/wiki/Jump_search
"""

import math
from collections.abc import Sequence
from typing import Any, Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool:
        ...


T = TypeVar("T", bound=Comparable)


def jump_search(arr: Sequence[T], item: T) -> int:
    """
    Python implementation of the jump search algorithm.
    Return the index if the `item` is found, otherwise return -1.

    Examples:
    >>> jump_search([0, 1, 2, 3, 4, 5], 3)
    3
    >>> jump_search([-5, -2, -1], -1)
    2
    >>> jump_search([0, 5, 10, 20], 8)
    -1
    >>> jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55)
    10
    >>> jump_search(["aa", "bb", "cc", "dd", "ee", "ff"], "ee")
    4
    """

    arr_size = len(arr)
    block_size = int(math.sqrt(arr_size))

    prev = 0
    step = block_size
    while arr[min(step, arr_size) - 1] < item:
        prev = step
        step += block_size
        if prev >= arr_size:
            return -1

    while arr[prev] < item:
        prev += 1
        if prev == min(step, arr_size):
            return -1
    if arr[prev] == item:
        return prev
    return -1


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    array = [int(item) for item in user_input.split(",")]
    x = int(input("Enter the number to be searched:\n"))

    res = jump_search(array, x)
    if res == -1:
        print("Number not found!")
    else:
        print(f"Number {x} is at index {res}")
