def majorityElement(nums: list[int]) -> int:

    """
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

    Solution is based on the Moore's Voting Algorithm

    >>> majorityElement([3,2,3])
    3
    >>> majorityElement([2,2,1,1,1,2,2])
    2
    """

    ele = cnt = 0

    for i in nums:
        if cnt == 0:
            ele = i
        if ele == i:
            cnt += 1
        else:
            cnt -= 1

    return ele


if __name__ == "__main__":
    print(majorityElement([3, 2, 3]))
