def to_sum(nums, target):
    """
    This function finds two numbers in the list 'nums' that add up to 'target'.

    :param nums: List of integers
    :param target: Integer target sum
    :return: Tuple of the two numbers that add up to target, or None if no such pair exists
    """
    num_set = set()

    for num in nums:
        complement = target - num
        if complement in num_set:
            return (complement, num)
        num_set.add(num)

    return None


if __name__ == "__main__":
    print(to_sum([2, 7, 11, 15], 9))
