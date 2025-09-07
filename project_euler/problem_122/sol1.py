"""
Project Euler Problem 122: https://projecteuler.net/problem=122

Efficient Exponentiation

The most naive way of computing n^15 requires fourteen multiplications:

                                               n x n x ... x n = n^15.

But using a "binary" method you can compute it in six multiplications:

                                                         n x n = n^2
                                                     n^2 x n^2 = n^4
                                                     n^4 x n^4 = n^8
                                                     n^8 x n^4 = n^12
                                                    n^12 x n^2 = n^14
                                                      n^14 x n = n^15

However it is yet possible to compute it in only five multiplications:

                                                                n x n = n^2
                                                              n^2 x n = n^3
                                                            n^3 x n^3 = n^6
                                                            n^6 x n^6 = n^12
                                                           n^12 x n^3 = n^15

We shall define m(k) to be the minimum number of multiplications to compute n^k;
for example m(15) = 5.

Find sum_{k = 1}^200 m(k).

It uses the fact that for rather small n, applicable for this problem, the solution
for each number can be formed by increasing the largest element.

References:
- https://en.wikipedia.org/wiki/Addition_chain
"""


def solve(nums: list[int], goal: int, depth: int) -> bool:
    """
    Checks if nums can have a sum equal to goal, given that length of nums does
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
        if solve(nums=nums, goal=goal, depth=depth):
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
    >>> solution(14)
    45
    >>> solution(15)
    50
    """
    total = 0
    for i in range(2, n + 1):
        max_length = 0
        while True:
            nums = [1]
            max_length += 1
            if solve(nums=nums, goal=i, depth=max_length):
                break
        total += max_length
    return total


if __name__ == "__main__":
    print(f"{solution() = }")
