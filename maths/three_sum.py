"""
https://en.wikipedia.org/wiki/3SUM
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in a sorted array of integers that sum up to zero.

    Args:
        nums: A sorted list of integers.

    Returns:
        A list of lists containing unique triplets that sum up to zero.

    >>> three_sum([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    >>> three_sum([1, 2, 3, 4])
    []
    """
    nums.sort()
    ans = []
    for i in range(len(nums) - 2):
        if i == 0 or (nums[i] != nums[i - 1]):
            low, high, c = i + 1, len(nums) - 1, 0 - nums[i]
            while low < high:
                if nums[low] + nums[high] == c:
                    ans.append([nums[i], nums[low], nums[high]])

                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1

                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < c:
                    low += 1
                else:
                    high -= 1
    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
