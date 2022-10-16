#############################
# Author: Avi Mehta
# File: Longest_palindromic_subsequence
# comments: This programme outputs the Longest Strictly Palindromic Subsequence in
#           O(NLogN) Where N is the Number of elements in the string
#############################
from __future__ import annotations

#  sentence is string parameter for the function


def longest_palindrome(sentence: str) -> str:
    """

    >>> longest_palindrome("cbbd")
    2
    >>> longest_palindrome("bbbab")
    4
    >>> longest_palindrome("zzakz")
    3
    >>> longest_palindromic(" ")
    0

    """

    dp = [[False for i in range(len(sentence))] for j in range(len(sentence))]
    for i in range(len(sentence)):
        dp[i][i] = True
    maxl = 1
    begin = 0

    # bottom up DP always start from base case, so we will scan backward
    for i in range(len(sentence) - 1, -1, -1):
        for j in range(i + 1, len(sentence)):
            if sentence[i] == sentence[j]:
                # if i+1=j and they are same character,of course this is a panlindrome
                if j - i == 1:
                    dp[i][j] = True
                else:  # if the substring between i and j are panlindrome
                    dp[i][j] = dp[i + 1][j - 1]
            if dp[i][j]:  # update the result
                if j - i + 1 > maxl:
                    maxl = j - i + 1
                    begin = i

    return sentence[begin : begin + maxl]


if __name__ == "__main__":

    import doctest

    doctest.testmod()
