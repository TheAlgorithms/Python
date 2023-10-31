"""
This is a pure Python implementation of the radix sort algorithm

Source: https://en.wikipedia.org/wiki/Radix_sort
Source of flatten_extend(): How to Flatten a List of Lists in Python 
https://realpython.com/python-flatten-list/#considering-performance-while-flattening-your-lists
"""
from __future__ import annotations

RADIX = 10

def flatten_extend(list_of_lists: list[list]) -> list[int]:
    flat_list = []
    for l in list_of_lists:
        flat_list.extend(row)
    return flat_list

def radix_sort(list_of_ints: list[int]) -> list[int]:
    """
    Examples:
    >>> radix_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> radix_sort(list(range(15))) == sorted(range(15))
    True
    >>> radix_sort(list(range(14,-1,-1))) == sorted(range(15))
    True
    >>> radix_sort([1,100,10,1000]) == sorted([1,100,10,1000])
    True
    """
    placement = 1
    max_digit = max(list_of_ints)
    while placement <= max_digit:
        # declare and initialize empty buckets
        buckets: list[list] = [[] for _ in range(RADIX)]
        # split list_of_ints between the buckets
        for i in list_of_ints:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        # Flatten each buckets' contents back into list_of_ints
        list_of_ints = flatten_extend(buckets)
        # move to next 
        placement *= RADIX
    return list_of_ints


if __name__ == "__main__":
    import doctest

    doctest.testmod()
