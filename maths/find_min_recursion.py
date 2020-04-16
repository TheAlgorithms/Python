# Divide and Conquer algorithm
def find_min(nums, left, right):
    """
    find min value in list
    :param nums: contains elements
    :param left: index of first element
    :param right: index of last element
    :return: min in nums

    >>> nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    >>> find_min(nums, 0, len(nums) - 1) == min(nums)
    True
    """
    if left == right:
        return nums[left]
    mid = (left + right) >> 1  # the middle
    left_min = find_min(nums, left, mid)  # find min in range[left, mid]
    right_min = find_min(nums, mid + 1, right)  # find min in range[mid + 1, right]

    return left_min if left_min <= right_min else right_min


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    assert find_min(nums, 0, len(nums) - 1) == 1
