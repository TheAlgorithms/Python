def find_nth_largest(nums: list, k: int) -> int:
    """
    Finds the nth largest element in a list.
    >>> find_nth_largest([3, 5, 2, 4, 6, 8], 2)
    6
    >>> find_nth_largest([70, 140, 99, 16, 17, 56], 5)
    17
    """
    nums = list(dict.fromkeys(nums))
    nums.sort(reverse=True)
    return nums[k - 1]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
