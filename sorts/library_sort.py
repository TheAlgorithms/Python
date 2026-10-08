"""
A pure Python implementation of library sort (also called gapped insertion sort).

It works like insertion sort, but leaves empty gaps in the array so a new item can
be placed without shifting everything after it. When the gaps fill up, the array is
rebalanced. Expected time is O(n log n).

Reference: https://en.wikipedia.org/wiki/Library_sort

For doctests run the following command:
python3 -m doctest -v library_sort.py

For manual testing run:
python3 library_sort.py
"""

_EMPTY = object()


def _spread(slots: list) -> None:
    """
    Redistribute the stored items evenly across all slots, keeping their order.

    >>> slots = [3, 5, 7, _EMPTY, _EMPTY, _EMPTY]
    >>> _spread(slots)
    >>> [x if x is not _EMPTY else None for x in slots]
    [3, None, 5, None, 7, None]
    """
    items = [x for x in slots if x is not _EMPTY]
    for i in range(len(slots)):
        slots[i] = _EMPTY
    for i, item in enumerate(items):
        slots[i * len(slots) // len(items)] = item


def _insert(slots: list, item) -> None:
    """
    Insert item into the gapped array, keeping the stored items in sorted order.

    >>> slots = [1, _EMPTY, 5, _EMPTY]
    >>> _insert(slots, 3)
    >>> [x if x is not _EMPTY else None for x in slots]
    [1, 3, 5, None]
    """
    size = len(slots)
    low, high = 0, size - 1
    # Binary search over the slots, skipping empty ones.
    while low <= high:
        mid = (low + high) // 2
        probe = mid
        while probe <= high and slots[probe] is _EMPTY:
            probe += 1
        if probe > high:
            high = mid - 1
        elif slots[probe] <= item:
            low = probe + 1
        else:
            high = mid - 1

    # Every stored item before `low` is <= item, every one from `low` on is > item.
    if low < size and slots[low] is _EMPTY:
        slots[low] = item
        return

    right = low
    while right < size and slots[right] is not _EMPTY:
        right += 1
    left = low - 1
    while left >= 0 and slots[left] is not _EMPTY:
        left -= 1

    # Shift items towards the nearest gap to make room.
    if left < 0 or (right < size and right - low <= low - 1 - left):
        slots[low + 1 : right + 1] = slots[low:right]
        slots[low] = item
    else:
        slots[left : low - 1] = slots[left + 1 : low]
        slots[low - 1] = item


def library_sort(collection: list) -> list:
    """
    A pure Python implementation of library sort (also called gapped insertion sort).

    :param collection: a collection of comparable items
    :return: a new list with the items in ascending order

    Time complexity: O(n log n) on average, O(n^2) in the worst case.
    Space complexity: O(n)

    Examples:
    >>> library_sort([5, 2, 9, 1, 5, 6])
    [1, 2, 5, 5, 6, 9]
    >>> library_sort([])
    []
    >>> library_sort([1])
    [1]
    >>> library_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    >>> library_sort(["d", "a", "c", "b"])
    ['a', 'b', 'c', 'd']
    >>> import random
    >>> data = [random.randint(-100, 100) for _ in range(200)]
    >>> library_sort(data) == sorted(data)
    True
    """
    n = len(collection)
    if n < 2:
        return list(collection)

    slots: list = [_EMPTY] * (2 * n)
    next_spread = 1
    for count, item in enumerate(collection, start=1):
        _insert(slots, item)
        if count == next_spread:
            _spread(slots)
            next_spread *= 2
    return [x for x in slots if x is not _EMPTY]


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(library_sort(unsorted))
