"""
Longest Palindromic Subsequence Problem:
Find the longest sequence of characters from a given input string that
is the same backwards and forwards
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
"""


def LongestPalindromicSubsequence(string, n):

    """
    Computes the longest Palindromic sequence of a string

    :param string: str, the string we provide
    :param n: int, the length of the string
    :return L[0][n - 1]: int, the length of the longest Palindromic subsequence



    >>> LongestPalindromicSubsequence("ABBCDABBC",9)
    5
    >>> LongestPalindromicSubsequence("ABACCG",6)
    3
    >>> LongestPalindromicSubsequence("55055901565109",14)
    9
    """

    # creating an array to store the values generated
    L = [[1 for i in range(n)] for i in range(n)]

    # Filling in the array created
    for x in range(2, n + 1):
        for y in range(n + 1 - x):
            z = y + x - 1
            if string[y] == string[z] and x == 2:
                L[y][z] = 2
            elif string[y] == string[z]:
                L[y][z] = L[y + 1][z - 1] + 2
            else:
                L[y][z] = max(L[y][z - 1], L[y + 1][z])

    return L[0][n - 1]


if __name__ == "__main__":
    testCase = "ABAC"

    n = len(testCase)
    print(
        "The longest palindromic subsequence is: "
        + str(LongestPalindromicSubsequence(testCase, n))
    )

    import doctest

    doctest.testmod()
