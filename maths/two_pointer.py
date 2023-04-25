"""
Given a sorted array of integers, return indices of the two numbers such
that they add up to a specific target using the two pointers technique.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

This is an alternative solution of the two-sum problem, which uses a
map to solve the problem. Hence can not solve the issue if there is a
constraint not use the same index twice. [1]

Referencing the Big O Notation, this algorithm has a liner time
complexity, O(N). In the worst case scenario, the sum of all pointers'
movements would be equals to the list's size.
E.g:
list = [5,12,13,21,40]
Meanwhile the left pointer will have to move three times, the right
pointer will move twice, totaling 5 moves.
Pointers Moviments == List's size == Algorithm's number of operations.
[https://en.wikipedia.org/wiki/Big_O_notation#Use_in_computer_science]

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

[1]: https://github.com/TheAlgorithms/Python/blob/master/other/two_sum.py
"""
from __future__ import annotations


def two_pointer(nums: list[int], target: int) -> list[int]:
    """
    >>> two_pointer([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_pointer([2, 7, 11, 15], 17)
    [0, 3]
    >>> two_pointer([2, 7, 11, 15], 18)
    [1, 2]
    >>> two_pointer([2, 7, 11, 15], 26)
    [2, 3]
    >>> two_pointer([1, 3, 3], 6)
    [1, 2]
    >>> two_pointer([2, 7, 11, 15], 8)
    []
    >>> two_pointer([3 * i for i in range(10)], 19)
    []
    >>> two_pointer([1, 2, 3], 6)
    []
    """
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] < target:
            i = i + 1
        else:
            j = j - 1

    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{two_pointer([2, 7, 11, 15], 9) = }")
