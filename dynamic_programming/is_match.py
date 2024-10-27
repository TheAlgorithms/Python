"""You are given a string s and a pattern p. Write a function to determine if the pattern p matches the entire string s.
The pattern p may contain the special characters:"""
"""  ? which matches any single character.
     * which matches any sequence of characters (including the empty sequence).
 Return True if p matches the entire string s; otherwise, return False."""
 
"""Example :
Input: s = "aa", p = "a"
Output: False
Explanation: The pattern "a" does not match the entire string "aa"."""




def is_match(s, p):
    m, n = len(s), len(p)
    
    # Initialize a DP table where dp[i][j] represents whether s[:i] matches p[:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # Empty pattern matches empty string

    # Fill the first row (when s is empty)
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]  # '*' can match an empty sequence
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' can match zero or more of the previous characters
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                # '?' matches any single character, or if characters match exactly
                dp[i][j] = dp[i - 1][j - 1]
    
    # The result is whether the entire string s matches the entire pattern p
    return dp[m][n]

# Take user input for string and pattern
s = input("Enter the string: ")
p = input("Enter the pattern: ")

# Print the result
print("Does the pattern match the string?", is_match(s, p))
