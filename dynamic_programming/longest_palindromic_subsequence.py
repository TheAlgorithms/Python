# Author: Sankalp Gupta
# https://leetcode.com/problems/longest-palindromic-subsequence/

from __future__ import annotations

# function for length of longest palindromic subsequence 
def longestPalindromeSubseq(s: str) -> int:

    """
    Some examples
    >>> longestPalindromeSubseq('sdsda')
    3
    >>> longestPalindromeSubseq('cbbd')
    2
    >>> longestPalindromeSubseq('as')
    1
    >>> longestPalindromeSubseq('l')
    1
    >>> longestPalindromeSubseq('')
    0
    """
    
    N = len(s)

    if N == 0:
        return 0

    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1
    for r in range(N-2, -1, -1):
        for c in range(r+1, N):
            if s[r] == s[c]:
                dp[r][c] = 2 + dp[r+1][c-1] 
            else:
                dp[r][c] = max(dp[r+1][c], dp[r][c-1])
    return dp[0][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()