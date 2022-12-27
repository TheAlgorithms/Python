"""
Python implementation of the MSD radix sort algorithm.
It used the binary representation of the integers to sort
them.
https://en.wikipedia.org/wiki/Radix_sort
"""
from __future__ import annotations


def msd_radix_sort(list_of_ints: list[int]) -> list[int]:
    """
    Implementation of the MSD radix sort algorithm. Only works
    with positive integers
    :param list_of_ints: A list of integers
    :return: Returns the sorted list
    >>> msd_radix_sort([40, 12, 1, 100, 4])
    [1, 4, 12, 40, 100]
    >>> msd_radix_sort([])
    []
    >>> msd_radix_sort([123, 345, 123, 80])
    [80, 123, 123, 345]
    >>> msd_radix_sort([1209, 834598, 1, 540402, 45])
    [1, 45, 1209, 540402, 834598]
    >>> msd_radix_sort([-1, 34, 45])
    Traceback (most recent call last):
        ...
    ValueError: All numbers must be positive
    """
    if not list_of_ints:
        return []

    if min(list_of_ints) < 0:
        raise ValueError("All numbers must be positive")

    most_bits = max(len(bin(x)[2:]) for x in list_of_ints)
    return _msd_radix_sort(list_of_ints, most_bits)


def _msd_radix_sort(list_of_ints: list[int], bit_position: int) -> list[int]:
    """
    Sort the given list based on the bit at bit_position. Numbers with a
    0 at that position will be at the start of the list, numbers with a
    1 at the end.
    :param list_of_ints: A list of integers
    :param bit_position: the position of the bit that gets compared
    :return: Returns a partially sorted list
    >>> _msd_radix_sort([45, 2, 32], 1)
    [2, 32, 45]
    >>> _msd_radix_sort([10, 4, 12], 2)
    [4, 12, 10]
    """
    if bit_position == 0 or len(list_of_ints) in [0, 1]:
        return list_of_ints

    zeros = []
    ones = []
    # Split numbers based on bit at bit_position from the right
    for number in list_of_ints:
        if (number >> (bit_position - 1)) & 1:
            # number has a one at bit bit_position
            ones.append(number)
        else:
            # number has a zero at bit bit_position
            zeros.append(number)

    # recursively split both lists further
    zeros = _msd_radix_sort(zeros, bit_position - 1)
    ones = _msd_radix_sort(ones, bit_position - 1)

    # recombine lists
    res = zeros
    res.extend(ones)

    return res


def msd_radix_sort_inplace(list_of_ints: list[int]):
    """
    Inplace implementation of the MSD radix sort algorithm.
    Sorts based on the binary representation of the integers.
    >>> lst = [1, 345, 23, 89, 0, 3]
    >>> msd_radix_sort_inplace(lst)
    >>> lst == sorted(lst)
    True
    >>> lst = [1, 43, 0, 0, 0, 24, 3, 3]
    >>> msd_radix_sort_inplace(lst)
    >>> lst == sorted(lst)
    True
    >>> lst = []
    >>> msd_radix_sort_inplace(lst)
    >>> lst == []
    True
    >>> lst = [-1, 34, 23, 4, -42]
    >>> msd_radix_sort_inplace(lst)
    Traceback (most recent call last):
        ...
    ValueError: All numbers must be positive
    """

    length = len(list_of_ints)
    if not list_of_ints or length == 1:
        return

    if min(list_of_ints) < 0:
        raise ValueError("All numbers must be positive")

    most_bits = max(len(bin(x)[2:]) for x in list_of_ints)
    _msd_radix_sort_inplace(list_of_ints, most_bits, 0, length)


def _msd_radix_sort_inplace(
    list_of_ints: list[int], bit_position: int, begin_index: int, end_index: int
):
    """
    Sort the given list based on the bit at bit_position. Numbers with a
    0 at that position will be at the start of the list, numbers with a
    1 at the end.
    >>> lst = [45, 2, 32, 24, 534, 2932]
    >>> _msd_radix_sort_inplace(lst, 1, 0, 3)
    >>> lst == [32, 2, 45, 24, 534, 2932]
    True
    >>> lst = [0, 2, 1, 3, 12, 10, 4, 90, 54, 2323, 756]
    >>> _msd_radix_sort_inplace(lst, 2, 4, 7)
    >>> lst == [0, 2, 1, 3, 12, 4, 10, 90, 54, 2323, 756]
    True
    """
    if bit_position == 0 or end_index - begin_index <= 1:
        return

    bit_position -= 1

    i = begin_index
    j = end_index - 1
    while i <= j:
        changed = False
        if not (list_of_ints[i] >> bit_position) & 1:
            # found zero at the beginning
            i += 1
            changed = True
        if (list_of_ints[j] >> bit_position) & 1:
            # found one at the end
            j -= 1
            changed = True

        if changed:
            continue

        list_of_ints[i], list_of_ints[j] = list_of_ints[j], list_of_ints[i]
        j -= 1
        if not j == i:
            i += 1

    _msd_radix_sort_inplace(list_of_ints, bit_position, begin_index, i)
    _msd_radix_sort_inplace(list_of_ints, bit_position, i, end_index)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
