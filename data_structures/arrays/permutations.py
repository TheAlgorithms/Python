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
        return [nums.copy()] #returns a copy of list nums
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutations = permute(nums)
        for perm in permutations:
            perm.append(n)
        result.extend(permutations)
        nums.append(n)
    return result


if __name__ == "__main__":
     '''this is used to examine the docstrings in the module, it does not return anything but
if any error is there it will print the error and its cause in stdout'''
    import doctest
    doctest.testmod()
