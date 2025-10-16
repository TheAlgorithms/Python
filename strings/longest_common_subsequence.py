# longest_common_subsequence.py
# This program finds the Longest Common Subsequence (LCS) between two strings
# using Dynamic Programming and also prints the actual LCS string.


def longest_common_subsequence(x: str, y: str):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS string
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()
    lcs_str = "".join(lcs)

    # Print DP table (for visualization)
    print("DP Table:")
    for row in dp:
        print(row)

    print(f"\nLength of LCS: {dp[m][n]}")
    print(f"LCS String: {lcs_str}")

    return dp[m][n], lcs_str


if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    longest_common_subsequence(s1, s2)
