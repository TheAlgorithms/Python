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


def permute2(nums):
    """
    Return all permutations of the given list.

    >>> permute2([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    """

    def backtrack(start):
        if start == len(nums) - 1:
            output.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack

    output = []
    backtrack(0)
    return output


if __name__ == "__main__":
    import doctest

    # use res to print the data in permute2 function
    res = permute2([1, 2, 3])
    print(res)
    doctest.testmod()
