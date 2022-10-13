"""
        The sum-of-subsetsproblem states that a set of non-negative integers, and a
        value M, determine all possible subsets of the given set whose summation sum
        equal to given M.

        Summation of the chosen numbers must be equal to given number M and one number
        can be used only once.
"""
from __future__ import annotations


def generate_sum_of_subsets_soln(nums: list[int], max_sum: int) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []
    num_index = 0
    remaining_nums_sum = sum(nums)
    create_state_space_tree(nums, max_sum, num_index, path, result, remaining_nums_sum)
    return result


def create_state_space_tree(
    nums: list[int],
    max_sum: int,
    num_index: int,
    path: list[int],
    result: list[list[int]],
    remaining_nums_sum: int,
) -> None:
    """
    Creates a state space tree to iterate through each branch using DFS.
    It terminates the branching of a node when any of the two conditions
    given below satisfy.
    This algorithm follows depth-fist-search and backtracks when the node is not
    branchable.

    """
    if sum(path) > max_sum or (remaining_nums_sum + sum(path)) < max_sum:
        return
    if sum(path) == max_sum:
        result.append(path)
        return
    for index in range(num_index, len(nums)):
        create_state_space_tree(
            nums,
            max_sum,
            index + 1,
            path + [nums[index]],
            result,
            remaining_nums_sum - nums[index],
        )


"""
remove the comment to take an input from the user

print("Enter the elements")
nums = list(map(int, input().split()))
print("Enter max_sum sum")
max_sum = int(input())

"""
nums = [3, 34, 4, 12, 5, 2]
max_sum = 9
result = generate_sum_of_subsets_soln(nums, max_sum)
print(*result)
