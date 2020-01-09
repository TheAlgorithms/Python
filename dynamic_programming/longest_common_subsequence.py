"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily continuous.
Example:"abc", "abg" are subsequences of "abcdefgh".
"""
'''
Hey This Is the Bottom-Up Approach of the Dynamic Programming.
'''

def longest_common_subsequence(x: str, y: str):
    """
    Finds the longest common subsequence between two strings. Also returns the
    The subsequence found

    Parameters
    ----------

    x: str, one of the strings
    y: str, the other string

    Returns
    -------
    L[m][n]: int, the length of the longest subsequence. Also equal to len(seq)
    Seq: str, the subsequence found

    >>> longest_common_subsequence("programming", "gaming")
    (6, 'gaming')
    >>> longest_common_subsequence("physics", "smartphone")
    (2, 'ph')
    >>> longest_common_subsequence("computer", "food")
    (1, 'o')
    """
    # find the length of strings

    assert x is not None
    assert y is not None

    m = len(x)
    n = len(y)

    # declaring the array for storing the dp values
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                match = 1
            else:
                match = 0

            L[i][j] = max(L[i - 1][j], L[i][j - 1], L[i - 1][j - 1] + match)

    seq = ""
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            match = 1
        else:
            match = 0

        if L[i][j] == L[i - 1][j - 1] + match:
            if match == 1:
                seq = x[i - 1] + seq
            i -= 1
            j -= 1
        elif L[i][j] == L[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return L[m][n], seq
'''
This is the Top-Down Approach (Memoization) of Dynamic Programming.
'''
def longest_common_subsequence_memoization(X, Y, m, n, dp):
    '''
    :param X: String 1st
    :param Y: String 2nc
    :param m: length of String 1
    :param n: length of String 2
    :param dp: Array for Storage of The Pre Calculate Value
    :return: length of Common Subsequence
    '''
    """
    >>> longest_common_subsequence_memoization("programming", "gaming")
    6
    >>> longest_common_subsequence_memoization("physics", "smartphone")
    2
    >>> longest_common_subsequence_memoization("computer", "food")
    1
    """
    # base case
    if (m == 0 or n == 0):
        return 0

    # if the same state has already been
    # computed
    if (dp[m - 1][n - 1] != -1):
        return dp[m - 1][n - 1]

        # if equal, then we store the value of the
    # function call
    if (X[m - 1] == Y[n - 1]):

        # store it in arr to avoid further repetitive
        # work in future function calls
        dp[m - 1][n - 1] = 1 + longest_common_subsequence_memoization(X, Y, m - 1, n - 1, dp)
        return dp[m - 1][n - 1]

    else:

        # store it in arr to avoid further repetitive
        # work in future function calls
        dp[m - 1][n - 1] = max(longest_common_subsequence_memoization(X, Y, m, n - 1, dp),
                               longest_common_subsequence_memoization(X, Y, m - 1, n, dp))
        return dp[m - 1][n - 1]

if __name__ == "__main__":
    a = "AGGTAB"
    b = "GXTXAYB"
    expected_ln = 4
    expected_subseq = "GTAB"
    m = len(a)
    n = len(b)
    maximum  = 1000
    ln, subseq = longest_common_subsequence(a, b)
    ##    print("len =", ln, ", sub-sequence =", subseq)

    dp = [[-1 for _ in range(maximum)] for _ in range(m)]
    lcsm = longest_common_subsequence_memoization(a,b,m,n,dp)
    ##print(lcsm)
    import doctest

    doctest.testmod()


