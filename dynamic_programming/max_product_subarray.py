def max_product_subarray(numbers: list[int]) -> int:
    """
    Returns the maximum product that can be obtained by multiplying a
    contiguous subarray of the given integer list `nums`.

    Example:
    >>> max_product_subarray([2, 3, -2, 4])
    6
    >>> max_product_subarray([-2, 0, -1])
    0
    >>> max_product_subarray([2, 3, -2, 4, -1])
    48
    """
    n = len(nums)

    if n == 0:
        return 0

    max_till_now = nums[0]
    min_till_now = nums[0]
    max_prod = nums[0]

    for i in range(1, n):
        # update the maximum and minimum subarray products
        if nums[i] < 0:
            max_till_now, min_till_now = min_till_now, max_till_now
        max_till_now = max(nums[i], max_till_now * nums[i])
        min_till_now = min(nums[i], min_till_now * nums[i])

        # update the maximum product found till now
        max_prod = max(max_prod, max_till_now)

    return max_prod
