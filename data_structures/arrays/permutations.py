# All permutations:
def permute(nums: list[int]) -> list[list[int]]:
    """
    >>> from itertools import permutations
    >>> numbers in ([], [1], [1, 2], [2, 1], [-1, -3, -2], [5.5, 3.3, 4.4, 1.1, 2.2])
    >>> all(permute(nums) == permutations(nums) for nums in numbers)
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


def main() -> None:  # Main function for testing.
    nums = [1, 2, 3]
    print("permutations are:", permute(nums))


if __name__ == "__main__":
    main()
