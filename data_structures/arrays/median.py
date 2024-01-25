def find_median(nums):
    """
    Find the median of a list of numbers.

    >>> find_median([1, 3, 2, 4, 5])
    3
    >>> find_median([5, 2, 10, 7, 1, 3, 8])
    5
    >>> find_median([2, 4, 6, 8])
    5.0
    >>> find_median([9, 7, 5, 3, 1])
    5
    """

    nums.sort()  # Sort the list in ascending order

    n = len(nums)
    if n % 2 == 0:
        # If the list has an even number of elements, return the average of the middle two elements
        middle1 = nums[n // 2 - 1]
        middle2 = nums[n // 2]
        median = (middle1 + middle2) / 2
    else:
        # If the list has an odd number of elements, return the middle element
        median = nums[n // 2]

    return median


if __name__ == "__main__":
    import doctest

    res = find_median([1, 3, 2, 4, 5, 6, 7, 8, 9])
    print(res)
    doctest.testmod()
