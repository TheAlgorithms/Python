def maxDiff(nums: list[int]) -> int:
    """
    The function returns the max difference in the
    array where result = arr[i] - arr[j] and i > j

    Runtime: O(n)
    Space: O(1)

    >>> maxDiff([2, 3, 10 , 6, 4, 8, 1])
    8
    >>> maxDiff([7, 9, 5, 6, 3, 2])
    2
    >>> maxDiff([10, 20, 30])
    20

    """
    result = nums[1] - nums[0]

    minVal = nums[0]

    for i in range(len(nums)):

        result = max(nums[i] - minVal, result)

        if nums[i] < minVal:
            minVal = nums[i]

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
