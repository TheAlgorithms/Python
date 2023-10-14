"""
    Sparse table is a data structure that allows answering range queries on
    a static array, i.e. the elements do not change throughout all the queries.

    The implementation below will solve the problem of Range Minimum Query:
    Finding the minimum value of a subset [L..R] of a static array.

    Overall time complexity: O(nlogn)
    Overall space complexity: O(nlogn)

    Wikipedia link: https://en.wikipedia.org/wiki/Range_minimum_query
"""


def build_sparse_table(arr: list[int], arr_length: int) -> list[list[int]]:
    """
    Precompute range minimum queries with power of two length
    and store the precomputed values in a table.

    >>> build_sparse_table([8, 1, 0, 3, 4, 9, 3], 7)
    [[8, 1, 0, 3, 4, 9, 3], [1, 0, 0, 3, 4, 3, 0], [0, 0, 0, 3, 0, 0, 0]]
    >>> build_sparse_table([3, 1, 9], 3)
    [[3, 1, 9], [1, 1, 0]]
    >>> build_sparse_table([], 0)
    Traceback (most recent call last):
    ...
    ValueError: math domain error
    """
    import math

    if arr == []:
        raise ValueError("math domain error")

    # Initialise lookup table
    k = int(math.log2(arr_length)) + 1
    lookup = [[0 for i in range(arr_length)] for j in range(k)]

    for i in range(arr_length):
        lookup[0][i] = arr[i]

    j = 1

    while (1 << j) <= arr_length:
        # Compute the minimum value for all intervals with size (2 ** j)
        i = 0
        while (i + (1 << j) - 1) < arr_length:
            lookup[j][i] = min(lookup[j - 1][i + (1 << (j - 1))], lookup[j - 1][i])
            i += 1

        j += 1

    return lookup


def query(lookup: list[list[int]], left_bound: int, right_bound: int) -> int:
    """
    >>> query(build_sparse_table([8, 1, 0, 3, 4, 9, 3], 7), 0, 4)
    0
    >>> query(build_sparse_table([8, 1, 0, 3, 4, 9, 3], 7), 4, 6)
    3
    >>> query(build_sparse_table([8, 1, 0, 3, 4, 9, 3], 7), 0, 11)
    Traceback (most recent call last):
    ...
    IndexError: list index out of range

    >>> query(build_sparse_table([3, 1, 9], 3), 2, 2)
    9
    >>> query(build_sparse_table([3, 1, 9], 3), 0, 1)
    1

    >>> query(build_sparse_table([], 0), 0, 0)
    Traceback (most recent call last):
    ...
    ValueError: math domain error
    """
    import math

    if lookup == []:
        raise ValueError("math domain error")
    if left_bound < 0 or right_bound >= len(lookup[0]):
        raise IndexError("list index out of range")

    """
    Find the highest power of 2
    that is at least the number of elements in a given range.
    """
    j = int(math.log2(right_bound - left_bound + 1))
    return min(lookup[j][right_bound - (1 << j) + 1], lookup[j][left_bound])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
