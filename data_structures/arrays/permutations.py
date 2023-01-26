from typing import List


def permute(nums: list[int]) -> list[list[int]]:
    """
    Return all permutations.
    >>> from itertools import permutations
    >>> numbers= [1,2,3]
    >>> all(list(nums) in permute(numbers) for nums in permutations(numbers))
    True
    """
    result = []
    if len(nums) == 1:
        return [nums.copy()]
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutations = permute(nums)
        for perm in permutations:
            perm.append(n)
        result.extend(permutations)
        nums.append(n)
    return result


def permute2(nums: list[int]) -> list[list[int]]:
    def backtrack(first=0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output

    # return result


if __name__ == "__main__":
    import doctest

    # use res to print the data in permute2 function
    res = permute2([1, 2, 3])
    print(res)
    doctest.testmod()
