"""Longest Repeated Subsequence
Given a string, print the longest repeating subsequence such that the two subsequence don’t have same string character at same position, 
i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.



Input: str = "aabb"
Output: "ab"

Input: str = "aab"
Output: "a"
The two subsequence are 'a'(first) and 'a' 
(second). Note that 'b' cannot be considered 
as part of subsequence as it would be at same
index in both.

This problem is just the modification of Longest Common Subsequence problem. The idea is to find the LCS(str, str) where str 
is the input string with the restriction that when both the characters are same, 
they shouldn’t be on the same index in the two strings.


PROGRAM:"""

def findLongestRepeatingSubSeq(str): 
    n = len(str) 
  
    # Create and initialize DP table 
    dp = [[0 for k in range(n+1)] for l in range(n+1)] 
  
    # Fill dp table (similar to LCS loops) 
    for i in range(1, n+1): 
        for j in range(1, n+1): 
            # If characters match and indices are not same 
            if (str[i-1] == str[j-1] and i != j): 
                dp[i][j] = 1 + dp[i-1][j-1] 
  
            # If characters do not match 
            else: 
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 
  
    return dp[n][n] 
  

#Time Complexity: O(n^2)
