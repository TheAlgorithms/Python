"""
Longest common Subsequence problem
If we are given two sequences, find the length of longest common subsequences present in both of them.
For example:
String1: helloworld
String2: ellorald
Longest common substring should be "ellorld" of size 7
"""

def lcs(str1, str2):
    """Function to calculate longest common substring between str1 and str2"""
    m = len(str1)
    n = len(str2)

    dp = [[None] * (n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


if __name__ == "__main__":
    str1 = "helloworld"
    str2 = "ellorald"

    print(F"The length of longest common subsequence between '{str1}' and '{str2}' is:", lcs(str1, str2))
