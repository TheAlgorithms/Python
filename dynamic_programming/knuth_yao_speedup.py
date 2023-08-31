"""
Knuth-Yao dynamic programming speedup, also known as the Knuth-Yao optimization, 
is a technique used to accelerate the computation of certain types of dynamic programming algorithms. 
It was introduced by Donald Knuth and Andrew Yao in their paper "Efficient Binary-Search Trees" in 1976. 

This implementation the following recurrence relation

dp[i][j] = min(i < k < j){dp[i][k] + dp[k][j] + cost[i][j]},

where opt[i][j-1] <= opt[i][j] <= opt[i+1][j] with opt[i][j] representing 
the value of 'k' that minimizes the given expression.

Equivalently, the cost function satisfies either of the following conditions.

1) cost[b][c] <= cost[a][d]
2) cost[a][c]+cost[b][d] <= cost[a][d]+cost[b][c]

Reference: https://cp-algorithms.com/dynamic_programming/knuth-optimization.html

- time complexity: O(n^2)
- space complexity: O(n^2)

>>> knuth_yao_speedup([[1,2,3,4],[3,4,5,1],[1,1,1,3],[2,2,2,2]])
15
"""
from __future__ import annotations


def knuth_yao_speedup(cost: list[list[int]]) -> int:
    n = len(cost)
    dp = [[0] * n for _ in range(n)]
    opt_k = [[0] * n for _ in range(n)]

    # default assignment along the diagonal (no k exists between i and i+1)
    for i in range(n - 1):
        opt_k[i][i + 1] = i + 1  # i + 1 is the first k such that i < k
        dp[i][i + 1] = cost[i][i + 1]

    # fill in the dp matrix diagonally
    for d in range(2, n):
        for i in range(n - d):
            j = i + d
            dp[i][j] = float("inf")
            for k in range(opt_k[i][j - 1], opt_k[i + 1][j] + 1):
                val = dp[i][k] + dp[k][j] + cost[i][j]
                if val < dp[i][j]:
                    dp[i][j] = val
                    opt_k[i][j] = k

    return dp[0][n - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
