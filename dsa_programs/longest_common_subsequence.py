"""Longest common subsequence reconstruction."""

from typing import List, Sequence, TypeVar

T = TypeVar("T")


def longest_common_subsequence(a: Sequence[T], b: Sequence[T]) -> List[T]:
    len_a, len_b = len(a), len(b)
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    for i in range(len_a - 1, -1, -1):
        for j in range(len_b - 1, -1, -1):
            if a[i] == b[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    i = j = 0
    result: List[T] = []
    while i < len_a and j < len_b:
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    return result
