# Divide and Conquer algorithm
def find_max(nums, left, right):
    """
    find max value in list
    :param nums: contains elements
    :param left: index of first element
    :param right: index of last element
    :return: max in nums
    
    >>> nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    >>> find_max(nums, 0, len(nums) - 1) == max(nums)
    True
    """
    if left == right:
        return nums[left]
    mid = (left + right) >> 1  # the middle
    left_max = find_max(nums, left, mid)  # find max in range[left, mid]
    right_max = find_max(nums, mid + 1, right)  # find max in range[mid + 1, right]

    return left_max if left_max >= right_max else right_max


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    assert find_max(nums, 0, len(nums) - 1) == 10
