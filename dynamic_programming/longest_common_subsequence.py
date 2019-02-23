"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily continious.
Example:"abc", "abg" are subsequences of "abcdefgh".
"""
from __future__ import print_function

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

def lcs_dp(x, y):
    # find the length of strings
    m = len(x)
    n = len(y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in xrange(m + 1)]
    seq = []

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i - 1] == y[ j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                seq.append(x[i -1])
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n], seq

if __name__=='__main__':
    x = 'AGGTAB'
    y = 'GXTXAYB'
    print(lcs_dp(x, y))
