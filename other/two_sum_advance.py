"""Pointer Solution
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9.
Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6.
Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1.
Therefore index1 = 1, index2 = 2. We return [1, 2].
"""


def two_sum(self, numbers: list[int], target: int) -> list[int]:
    n = len(numbers)
    l = 0
    r = n - 1
    res = []
    while l < r:
        if numbers[l] + numbers[r] == target:
            res.append(l + 1)
            res.append(r + 1)
        if numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1
    res.sort()
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
