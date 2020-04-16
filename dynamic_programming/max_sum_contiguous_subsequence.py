def max_subarray_sum(nums: list) -> int:
    """
    >>> max_subarray_sum([6 , 9, -1, 3, -7, -5, 10])
    17
    """
    if not nums:
        return 0
    n = len(nums)

    res, s, s_pre = nums[0], nums[0], nums[0]
    for i in range(1, n):
        s = max(nums[i], s_pre + nums[i])
        s_pre = s
        res = max(res, s)
    return res


if __name__ == "__main__":
    nums = [6, 9, -1, 3, -7, -5, 10]
    print(max_subarray_sum(nums))
