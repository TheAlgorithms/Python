def minsubarraysum(target: int, numbers: list[int]) -> int:
    """
    Returns the length of the shortest contiguous subarray
     in nums whose sum is at least target.

        >>> minsubarraysum(7, [2, 3, 1, 2, 4, 3])
        2
        >>> minsubarraysum(7, [2, 3, -1, 2, 4, -3])
        4
        >>> minsubarraysum(11, [1, 1, 1, 1, 1, 1, 1, 1])
        0
        >>> minsubarraysum(10, [1, 2, 3, 4, 5, 6, 7])
        2
        >>> minsubarraysum(5, [1, 1, 1, 1, 1, 5])
        1
        >>> minsubarraysum(0, [])
        0
        >>> minsubarraysum(10, [10, 20, 30])
        1
        >>> minsubarraysum(7, [1, 1, 1, 1, 1, 1, 10])
        1
    """

    if not numbers:
        return 0
    left = right = curr_sum = 0
    min_len = sys.maxsize

    while right < len(numbers):
        curr_sum += numbers[right]
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= numbers[left]
            left += 1
        right += 1

    return int(min_len) if min_len != float("inf") else 0
