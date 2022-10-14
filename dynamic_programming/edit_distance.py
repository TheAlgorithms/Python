"""
Author  : Turfa Auliarachman
Date    : October 12, 2016

This is a pure Python implementation of Dynamic Programming solution to the edit
distance problem.

The problem is :
Given two strings A and B. Find the minimum number of operations to string B such that
A = B. The permitted operations are removal,  insertion, and substitution.
"""


class EditDistance:
    """
    Use :
    solver              = EditDistance()
    editDistanceResult  = solver.solve(firstString, secondString)
    """

    def __init__(self):
        self.__prepare__()

    def __prepare__(self, n=0, m=0):
        self.dp = [[-1 for y in range(0, m)] for x in range(0, n)]

    def __solve_dp(self, x, y):
        if x == -1:
            return y + 1
        elif y == -1:
            return x + 1
        elif self.dp[x][y] > -1:
            return self.dp[x][y]
        else:
            if self.a[x] == self.b[y]:
                self.dp[x][y] = self.__solve_dp(x - 1, y - 1)
            else:
                self.dp[x][y] = 1 + min(
                    self.__solve_dp(x, y - 1),
                    self.__solve_dp(x - 1, y),
                    self.__solve_dp(x - 1, y - 1),
                )

            return self.dp[x][y]

    def solve(self, a, b):
        if isinstance(a, bytes):
            a = a.decode("ascii")

        if isinstance(b, bytes):
            b = b.decode("ascii")

        self.a = str(a)
        self.b = str(b)

        self.__prepare__(len(a), len(b))

        return self.__solve_dp(len(a) - 1, len(b) - 1)


def min_distance_bottom_up(word1: str, word2: str) -> int:
    """
    >>> min_distance_bottom_up("intention", "execution")
    5
    >>> min_distance_bottom_up("intention", "")
    9
    >>> min_distance_bottom_up("", "")
    0
    """
    m = len(word1)
    n = len(word2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:  # first string is empty
                dp[i][j] = j
            elif j == 0:  # second string is empty
                dp[i][j] = i
            elif (
                word1[i - 1] == word2[j - 1]
            ):  # last character of both substing is equal
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
    print("The minimum Edit Distance is: %d" % (solver.solve(S1, S2)))
    print("The minimum Edit Distance is: %d" % (min_distance_bottom_up(S1, S2)))
    print()
    print("*************** End of Testing Edit Distance DP Algorithm ***************")
