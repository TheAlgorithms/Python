def find_single_number(nums):
    """
    LeetCode 136: Single Number
    https://leetcode.com/problems/single-number/description/

    >>> find_single_number([1, 4, 1, 7, 9, 2, 9, 7, 2])
    4
    >>> find_single_number([1, 2, 4, 1, 4, 3, 2])
    3
    >>> find_single_number([4, 1, 2, 1, 2])
    4
    """
    single_num = 0

    for i in nums:
        single_num = single_num ^ i

    return single_num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
