import sys


def minimum_subarray_sum(target: int, numbers: list[int]) -> int:
    """
    Returns the length of the shortest contiguous subarray
     in a list of numbers whose sum is at least target.

    >>> minimum_subarray_sum(7, [2, 3, 1, 2, 4, 3])
    2
    >>> minimum_subarray_sum(7, [2, 3, -1, 2, 4, -3])
    4
    >>> minimum_subarray_sum(11, [1, 1, 1, 1, 1, 1, 1, 1])
    0
    >>> minimum_subarray_sum(10, [1, 2, 3, 4, 5, 6, 7])
    2
    >>> minimum_subarray_sum(5, [1, 1, 1, 1, 1, 5])
    1
    >>> minimum_subarray_sum(0, [])
    0
    >>> minimum_subarray_sum(0, [1, 2, 3])
    0
    >>> minimum_subarray_sum(10, [10, 20, 30])
    1
    >>> minimum_subarray_sum(7, [1, 1, 1, 1, 1, 1, 10])
    1
    >>> minimum_subarray_sum(6, [])
    0
    >>> minimum_subarray_sum(2, [1, 2, 3])
    1
    >>> minimum_subarray_sum(-6, [])
    0
    >>> minimum_subarray_sum(-6, [3, 4, 5])
    0
    >>> minimum_subarray_sum(8, None)
    0
    >>> minimum_subarray_sum(2, "ABC")
    Traceback (most recent call last):
        ...
    ValueError: numbers must be an iterable of integers
    """

    if not numbers:
        return 0
    if not isinstance(numbers, (list, tuple)) or not all(
        isinstance(number, int) for number in numbers
    ):
        raise ValueError("numbers must be an iterable of integers")

    left = right = curr_sum = 0
    min_len = sys.maxsize
    for right, number in enumerate(numbers):
        curr_sum += number
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= numbers[left]
            left += 1

    return 0 if min_len == sys.maxsize else min_len


if __name__ == "__main__":
    from doctest import testmod

    testmod()()
