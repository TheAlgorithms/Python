"""
Project Euler Problem 122: https://projecteuler.net/problem=122

Efficient Exponentiation

It uses the fact that for rather small n, applicable for this problem, the solution
for each number
can be formed by increasing the largest element.

References:
- https://en.wikipedia.org/wiki/Addition_chain

>>> solution(14)
45
"""


def solve(nums: list[int], goal: int, depth: int) -> bool:
    """
    Checks if nums can can have a sum equal to goal, given that length of nums does
    not exceed depth.

    >>> solve([1], 2, 2)
    True
    >>> solve([1], 2, 0)
    False
    """
    if len(nums) > depth:
        return False
    for el in nums:
        if el + nums[-1] == goal:
            return True
        nums.append(el + nums[-1])
        if solve(nums, goal, depth):
            return True
        del nums[-1]
    return False


def solution(n: int = 200) -> int:
    """
    Calculates sum of smallest number of multiplactions for each number up to
    and including n.

    >>> solution(1)
    0
    >>> solution(2)
    1
    >>> solution(15)
    50
    """
    m = [0]
    for i in range(2, n + 1):
        max_length = 0
        while True:
            nums = [1]
            max_length += 1
            if solve(nums, i, max_length):
                break
        m.append(len(nums))
    return sum(m)


if __name__ == "__main__":
    print(f"{solution() = }")
