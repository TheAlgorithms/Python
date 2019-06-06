"""
Jump search algorithm

    >>> arr = [
    ...     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
    ... ]

    >>> arr[jump_search(arr, 55)]
    55

    >>> arr[jump_search(arr, 0)]
    0

    >>> arr[jump_search(arr, 610)]
    610

Check if all arr at once:

    >>> all(arr[jump_search(arr, x)] == x for x in arr)
    True

"""

from math import floor, sqrt


def jump_search(arr, x):
    prev = 0
    n = len(arr)
    step = int(floor(sqrt(n)))
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(floor(sqrt(n)))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev

    return -1
