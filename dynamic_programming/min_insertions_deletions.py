"""
Problem Statement :

Given two strings s1 & s2 of length m and n respectively,
transform s1 to s2 with minimum number of insertions and deletions

Algorithm :
Idea is to use classic DP algorithm, LCS(Longest Common Subsequence)
Example, given str1 = "foam" and str2 = "programming"

LCS(str1, str2) = L = "oam"  => length(L) = 3
Thus,
deletions = len(str1) - len(L), 
insertions = len(str2) - len(L)
"""


def longest_common_subsequence(str1: str, str2: str):
    """
    Finds the length of longest common subsequence between two strings.

    Parameters :
    Two strings str1 and str2

    Returns :
    length of the LCS found

    >>> longest_common_subsequence("foam", "programming")
    3
    >>> longest_common_subsequence("FVS", "ABCGFHs")
    1
    >>> longest_common_subsequence("applaud", "app")
    3

    """

    # length of the strings
    m = len(str1)
    n = len(str2)

    # array to store the subproblems
    dp = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # if characters match, increment the LCS of subproblem
            # LCS(str1[:i-1], str2[:j-1]) by 1
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            # else, try possible solutions and take maximum
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # required LCS(str1, str2)
    return dp[m][n]


def min_insertions_deletions(str1: str, str2: str):
    """
    Calculates the minimum numbers of insertions and deletions required
    to transform str1 to str2

    Parameters:
    Two strings str1 and str2

    Returns:
    A tuple of two integers (insertions, deletions), representing the insertions
    and deletions required

    >>> min_insertions_deletions("foam", "programming")
    (8, 1)
    >>> min_insertions_deletions("FVS", "ABCGFHs")
    (6, 2)
    >>> min_insertions_deletions("applaud", "app")
    (0, 4)
    >>> min_insertions_deletions(32, "app")
    Traceback (most recent call last):
      File "min_insertions_deletions.py", line 96, in <module>
        insertions, deletions = min_insertions_deletions(str1, str2)
      File "min_insertions_deletions.py", line 78, in min_insertions_deletions
        assert type(str1) is str, "str1 should be a string, not {}".format(type(str1))
    AssertionError: str1 should be a string, not <class 'int'>

    """

    assert type(str1) is str, "str1 should be a string, not {}".format(type(str1))
    assert type(str2) is str, "str2 shoul be a string, not {}".format(type(str2))
    # calculate the length of LCS of str1 and str2
    lcs = longest_common_subsequence(str1, str2)

    # insertions required
    insertions = len(str2) - lcs

    # deletions required
    deletions = len(str1) - lcs

    return insertions, deletions


if __name__ == "__main__":
    str1 = "foam"
    str2 = "programming"

    insertions, deletions = min_insertions_deletions(str1, str2)
    print(
        "insertions required : {}, deletions required : {}".format(
            insertions, deletions
        )
    )

    import doctest

    doctest.testmod()
