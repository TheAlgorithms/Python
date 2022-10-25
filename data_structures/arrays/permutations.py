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


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))
