"""
Project Euler Problem 122: https://projecteuler.net/problem=122

Efficient Exponentiation
"""


def solve(nums: list[int], goal: int, depth: int) -> bool:
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
