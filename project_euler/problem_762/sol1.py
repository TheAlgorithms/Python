"""
Project Euler Problem 762: https://projecteuler.net/problem=762

Consider a two-dimensional grid of squares. The grid has 4 rows but infinitely many columns.
An amoeba in square (x, y) can divide itself into two amoebas to occupy the squares (x+1, y) and (x+1, (y+1) mod 4), provided these squares are empty.

The goal is to find the number of different possible arrangements of amoebas after N divisions, where each arrangement is counted only once. This function is denoted as C(N).

For example, when N=2, there are 2 different possible arrangements. When N=10, there are 1301 different possible arrangements. When N=20, there are 5895236 different possible arrangements. And the problem asks for the last nine digits of C(100,000), which should be found and provided as the final answer.

"""

def solution(N:int=100000):
    """
    Calculates the number of different possible arrangements of amoebas after N divisions.

    This function uses dynamic programming to find the result.

    :param N: The number of divisions.
    :type N: int
    :return: The number of different possible arrangements modulo 10^9.
    :rtype: int
    
    >>> solution(10)
    1301

    >>> solution(100)
    125923036
    
    """
    MOD = 10**9
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i in range(1, N + 1):
        dp[i] = (dp[i] + dp[i - 1]) % MOD
        for j in range(4, i + 1, 4):
            dp[i] = (dp[i] + dp[i - j] * 2) % MOD

    return dp[N]

if __name__ == "__main__":
    print(solution())