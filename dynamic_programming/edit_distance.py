"""
Author  : Turfa Auliarachman
Date    : October 12, 2016

This is a pure Python implementation of Dynamic Programming solution to the edit
distance problem.

The problem is :
Given two strings A and B. Find the minimum number of operations to string B such that
A = B. The permitted operations are removal, insertion, and substitution.
"""


class EditDistance:
    """
    Use :
    solver              = EditDistance()
    editDistanceResult  = solver.solve(firstString, secondString)
    """

    def __init__(self):
        self.dp = []
        self.word1 = ""
        self.word2 = ""

    def __prepare(self, word1: str, word2: str) -> None:
        self.word1 = word1
        self.word2 = word2
        self.dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]

    def solve(self, word1: str, word2: str) -> int:
        """
        >>> EditDistance().solve("intention", "execution")
        5
        >>> EditDistance().solve("intention", "")
        9
        >>> EditDistance().solve("", "")
        0
        """
        self.__prepare(word1, word2)
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:  # first string is empty
                    dp[i][j] = j
                elif j == 0:  # second string is empty
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:  # last chars are equal
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = dp[i][j - 1]
                    delete = dp[i - 1][j]
                    replace = dp[i - 1][j - 1]
                    dp[i][j] = 1 + min(insert, delete, replace)
        return dp[m][n]


if __name__ == "__main__":
    solver = EditDistance()

    print("****************** Testing Edit Distance DP Algorithm ******************")
    print()

    S1 = input("Enter the first string: ").strip()
    S2 = input("Enter the second string: ").strip()

    print()
    print(f"The minimum Edit Distance is: {solver.solve(S1, S2)}")
    print()
    print("*************** End of Testing Edit Distance DP Algorithm ***************")
