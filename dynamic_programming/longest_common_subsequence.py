"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence
present in both of them.  A subsequence is a sequence that appears in the same relative
order, but not necessarily continuous.
Example:"abc", "abg" are subsequences of "abcdefgh".
 """       
"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence
present in both of them.  A subsequence is a sequence that appears in the same relative
order, but not necessarily continuous.
Example:"abc", "abg" are subsequences of "abcdefgh".
"""


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
    # Get the lengths of the input strings
    m, n = len(x), len(y)

    # Initialize a matrix to store dynamic programming values
    l = [[0] * (n + 1) for _ in range(m + 1)]

    # Populate the matrix using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the characters match, add 1 to the LCS length
            l[i][j] = max(
                l[i - 1][j], l[i][j - 1], l[i - 1][j - 1] + (x[i - 1] == y[j - 1])
            )

    # Trace back to find the LCS itself
    seq = ""
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            # Add matching character to the LCS
            seq = x[i - 1] + seq
            i, j = i - 1, j - 1
        elif l[i - 1][j] > l[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Return the length of LCS and the LCS sequence
    return l[m][n], seq


if __name__ == "__main__":
    # Example usage
    a, b = "AGGTAB", "GXTXAYB"
    ln, subseq = longest_common_subsequence(a, b)
    print("len =", ln, ", sub-sequence =", subseq)



