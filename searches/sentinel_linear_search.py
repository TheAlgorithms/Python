"""
Sentinel Linear Search Algorithm
A variation of linear search that reduces comparisons per iteration.
Reference: https://en.wikipedia.org/wiki/Linear_search#With_a_sentinel
"""


def sentinel_linear_search(arr: list[int], target: int) -> int:
    """
    Search for target using sentinel method, return index or -1 if not found.

    >>> sentinel_linear_search([1, 2, 3, 4, 5], 3)
    2
    >>> sentinel_linear_search([1, 2, 3, 4, 5], 6)
    -1
    >>> sentinel_linear_search([], 1)
    -1
    """
    n = len(arr)
    if n == 0:
        return -1

    last = arr[n - 1]
    arr[n - 1] = target
    i = 0

    while arr[i] != target:
        i += 1

    # Restore the original last element to prevent mutation of the input array
    arr[n - 1] = last

    if i < n - 1 or arr[n - 1] == target:
        return i
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(sentinel_linear_search([1, 2, 3, 4, 5], 3))
