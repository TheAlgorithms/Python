"""Levenshtein edit distance via dynamic programming."""

from typing import Sequence


def edit_distance(a: Sequence[str], b: Sequence[str]) -> int:
    if isinstance(a, str):
        seq_a = list(a)
    else:
        seq_a = list(a)
    if isinstance(b, str):
        seq_b = list(b)
    else:
        seq_b = list(b)
    m = len(seq_a)
    n = len(seq_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if seq_a[i - 1] == seq_b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost,
            )
    return dp[m][n]
