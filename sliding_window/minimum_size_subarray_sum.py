def minsubarraysum(target: int, nums: List[int]) -> int:
   """
    Returns the length of the shortest contiguous subarray
    in nums whose sum is at least target.

    Args:
        target (int): The minimum sum that the subarray should have.
        nums (List[int]): The array to search for subarrays in.

    Returns:
        int: The length of the shortest contiguous subarray
        in nums whose sum is at least target. If no such subarray exists, returns 0.

    Examples:
        >>> minsubarraysum(7, [2, 3, 1, 2, 4, 3])
        2
        >>> minsubarraysum(4, [1, 4, 4])
        1
        >>> minsubarraysum(11, [1, 1, 1, 1, 1, 1, 1, 1])
        0
    """
    n = len(nums)
    if n == 0:
        return 0

    left = 0
    right = 0
    curr_sum = 0
    min_len = float("inf")

    while right < n:
        curr_sum += nums[right]
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1
        right += 1

    return min_len if min_len != float("inf") else 0


nums = [2, 3, 1, 2, 4, 3]
target = 7
print(minsubarraysum(target, nums))
