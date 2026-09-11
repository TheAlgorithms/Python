"""
Problem 13: https://projecteuler.net/problem=13

Problem Statement:
Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.
"""

import os


def solution(n: int = 10) -> str:
    """
    Returns the first 'n' digits of the sum of the array elements
    from the file num.txt. n should be larger than 2.

    >>> solution(3)
    '553'
    >>> solution(6)
    '553737'
    """
    file_path = os.path.join(os.path.dirname(__file__), "num.txt")
    numbers: list[str] = []
    with open(file_path) as file_hand:
        for line in file_hand:
            numbers.append(line)

    ans = [0] * 50
    for d in range(49, -1, -1):
        for num in numbers:
            ans[d] += int(num[d])
        if d > 0:
            ans[d - 1] = ans[d] // 10
            ans[d] %= 10

    size_first = len(str(ans[0]))
    return "".join([str(x) for x in ans[: n - size_first + 1]])


if __name__ == "__main__":
    print(solution())
