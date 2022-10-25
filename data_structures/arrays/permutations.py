# All permutations:
def permute(nums: list[int]) -> list[list[int]]:
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


# Unique permutations:
def permute_unique(nums: list[int]) -> list[list[int]]:
    result = []
    if len(nums) == 1:
        return [nums.copy()]
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutations = permute_unique(nums)
        for perm in permutations:
            perm.append(n)
        result.extend(permutations)
        nums.append(n)
    ans = []
    for i in result:
        if i not in ans:
            ans.append(i)
    return ans
