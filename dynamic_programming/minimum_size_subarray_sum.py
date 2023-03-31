def minsubarraysum(target: int, numbers: list[int]) -> int:
    """
    Returns the length of the shortest contiguous subarray
     in nums whose sum is at least target.

    Examples :
        >>> minsubarraysum(7, [2, 3, 1, 2, 4, 3])
        2
        >>> minsubarraysum(7, [2, 3, -1, 2, 4, -3])
        4
        >>> minsubarraysum(11, [1, 1, 1, 1, 1, 1, 1, 1])
        0
    """

    if len(numbers) == 0:
        return 0

    left = right = curr_sum = 0
    min_len = float("inf")

    while right < len(numbers):
        curr_sum += numbers[right]
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= numbers[left]
            left += 1
        right += 1

    return int(min_len) if min_len != float("inf") else 0
