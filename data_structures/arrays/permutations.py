from typing import List
def permute(nums: List[int]) -> List[List[int]]:
    """
    Return all permutations.

    >>> from itertools import permutations
    >>> numbers= [1,2,3]
    >>> all(list(nums) in permute(numbers) for nums in permutations(numbers))
    True
    """
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
    res = permute([1,2,3])
    print(res)
    doctest.testmod()
