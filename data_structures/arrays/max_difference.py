def max_difference(nums: list[int]) -> int:
    """
    The function returns the max difference in the
    array where result = arr[i] - arr[j] and i > j

    Runtime: O(n)
    Space: O(1)

    >>> max_difference(([2, 3, 10 , 6, 4, 8, 1])
    8
    >>> max_difference(([7, 9, 5, 6, 3, 2])
    2
    >>> max_difference(([10, 20, 30])
    20

    """
    result = nums[1] - nums[0]

    min_val = nums[0]

    for i in range(len(nums)):

        result = max(nums[i] - min_val, result)

        if nums[i] < min_val:
            min_val = nums[i]

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
