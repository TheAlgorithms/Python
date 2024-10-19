def longest_palindromic_subsequence(input_string: str) -> int:
    """
    Function to find the length of the longest palindromic subsequence
    in a given string using dynamic programming.

    :param input_string: Input string
    :return: Length of the longest palindromic subsequence

    >>> longest_palindromic_subsequence("bbbab")
    4
    >>> longest_palindromic_subsequence("cbbd")
    2
    >>> longest_palindromic_subsequence("")
    0
    >>> longest_palindromic_subsequence("a")
    1
    >>> longest_palindromic_subsequence("abcd")
    1
    >>> longest_palindromic_subsequence("agbdba")
    5
    """
    n = len(input_string)

    # Base case: if string is empty, return 0
    if n == 0:
        return 0

    # dp[i][j] will represent the length of the longest palindromic subsequence
    # within the substring input_string[i...j]
    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the DP table for substrings of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if input_string[i] == input_string[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The longest palindromic subsequence length for the full string is dp[0][n-1]
    return dp[0][n - 1]


# Example usage:
if __name__ == "__main__":
    input_string = "bbbab"
    result = longest_palindromic_subsequence(input_string)
    print(f"Length of Longest Palindromic Subsequence: {result}")
