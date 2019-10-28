# NguyenU


def find_max(nums):
    """
    >>> for nums in ([3, 2, 1], [-3, -2, -1], [3, -3, 0], [3.0, 3.1, 2.9]):
    ...     find_max(nums) == max(nums)
    True
    True
    True
    True
    """
    max = nums[0]
    for x in nums:
        if x > max:
            max = x
    return max


def main():
    print(find_max([2, 4, 9, 7, 19, 94, 5]))  # 94


if __name__ == "__main__":
    main()
