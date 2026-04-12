"""
This is a pure Python implementation of Dynamic Programming solution to the edit
distance problem (also known as Levenshtein distance).

The Problem:
Given two strings A and B, find the minimum number of operations to transform
string A into string B. The permitted operations are:
1. Insertion - Add a character
2. Deletion - Remove a character  
3. Substitution - Replace one character with another

Time Complexity: O(m × n) where m and n are the lengths of the two strings
Space Complexity: O(m × n) for the DP table

Applications:
- Spell checkers and autocorrect
- DNA sequence alignment in bioinformatics
- Plagiarism detection
- Speech recognition
- Fuzzy string matching

Example:
    >>> EditDistance().min_dist_bottom_up("intention", "execution")
    5
    >>> # The 5 edits are: intention -> inention -> enention -> exention -> executon -> execution
"""


class EditDistance:
    """
    A class to compute the edit distance between two strings using dynamic programming.
    
    This implementation provides both top-down (memoization) and bottom-up (tabulation)
    approaches. The bottom-up approach is generally preferred for its iterative nature
    and better space efficiency potential.
    
    Attributes:
        word1 (str): First input string.
        word2 (str): Second input string.
        dp (list[list[int]]): Dynamic programming table for storing intermediate results.
    
    Example:
        >>> solver = EditDistance()
        >>> solver.min_dist_bottom_up("kitten", "sitting")
        3
    """
    
    def __init__(self):
        """Initialize the EditDistance solver with empty strings."""
        self.word1 = ""
        self.word2 = ""
        self.dp = []
    
    def __min_dist_top_down_dp(self, m: int, n: int) -> int:
        """
        Helper method for top-down dynamic programming with memoization.
        
        Recursively computes the minimum edit distance between word1[0:m+1] and 
        word2[0:n+1] by considering three possible operations at each step.
        
        Args:
            m (int): Current index in word1 (0-indexed).
            n (int): Current index in word2 (0-indexed).
        
        Returns:
            int: Minimum edit distance between the substrings.
        
        Base Cases:
            - If m == -1: Need to insert all n+1 characters from word2
            - If n == -1: Need to delete all m+1 characters from word1
        
        Recursive Case:
            - If characters match: No operation needed, move diagonally
            - Otherwise: Take minimum of insert, delete, replace + 1
        """
        if m == -1:
            return n + 1
        elif n == -1:
            return m + 1
        elif self.dp[m][n] > -1:
            return self.dp[m][n]
        else:
            if self.word1[m] == self.word2[n]:
                self.dp[m][n] = self.__min_dist_top_down_dp(m - 1, n - 1)
            else:
                insert = self.__min_dist_top_down_dp(m, n - 1)
                delete = self.__min_dist_top_down_dp(m - 1, n)
                replace = self.__min_dist_top_down_dp(m - 1, n - 1)
                self.dp[m][n] = 1 + min(insert, delete, replace)
            
            return self.dp[m][n]
    
    def min_dist_top_down(self, word1: str, word2: str) -> int:
        """
        Calculate edit distance using top-down approach with memoization.
        
        This approach starts from the full problem and recursively breaks it down
        into smaller subproblems, caching results to avoid redundant computations.
        
        Args:
            word1 (str): The source string.
            word2 (str): The target string.
        
        Returns:
            int: Minimum number of operations to transform word1 into word2.
        
        Examples:
            >>> EditDistance().min_dist_top_down("intention", "execution")
            5
            >>> EditDistance().min_dist_top_down("intention", "")
            9
            >>> EditDistance().min_dist_top_down("", "")
            0
            >>> EditDistance().min_dist_top_down("kitten", "sitting")
            3
        """
        self.word1 = word1
        self.word2 = word2
        self.dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        
        return self.__min_dist_top_down_dp(len(word1) - 1, len(word2) - 1)
    
    def min_dist_bottom_up(self, word1: str, word2: str) -> int:
        """
        Calculate edit distance using bottom-up approach with tabulation.
        
        This approach builds the solution iteratively from smaller subproblems,
        filling a DP table where dp[i][j] represents the edit distance between
        the first i characters of word1 and first j characters of word2.
        
        Args:
            word1 (str): The source string.
            word2 (str): The target string.
        
        Returns:
            int: Minimum number of operations to transform word1 into word2.
        
        Algorithm:
            1. Initialize DP table of size (m+1) × (n+1)
            2. Base cases: dp[i][0] = i (delete all), dp[0][j] = j (insert all)
            3. For each cell, if characters match: dp[i][j] = dp[i-1][j-1]
            4. Otherwise: dp[i][j] = 1 + min(insert, delete, replace)
        
        Examples:
            >>> EditDistance().min_dist_bottom_up("intention", "execution")
            5
            >>> EditDistance().min_dist_bottom_up("intention", "")
            9
            >>> EditDistance().min_dist_bottom_up("", "")
            0
            >>> EditDistance().min_dist_bottom_up("kitten", "sitting")
            3
            >>> EditDistance().min_dist_bottom_up("horse", "ros")
            3
        """
        self.word1 = word1
        self.word2 = word2
        m = len(word1)
        n = len(word2)
        self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:  # first string is empty - insert all characters
                    self.dp[i][j] = j
                elif j == 0:  # second string is empty - delete all characters
                    self.dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:  # last characters are equal
                    self.dp[i][j] = self.dp[i - 1][j - 1]
                else:
                    insert = self.dp[i][j - 1]      # Insert character
                    delete = self.dp[i - 1][j]      # Delete character
                    replace = self.dp[i - 1][j - 1] # Replace character
                    self.dp[i][j] = 1 + min(insert, delete, replace)
        return self.dp[m][n]


if __name__ == "__main__":
    solver = EditDistance()

    print("****************** Testing Edit Distance DP Algorithm ******************")
    print()

    S1 = input("Enter the first string: ").strip()
    S2 = input("Enter the second string: ").strip()

    print()
    print(f"The minimum edit distance is: {solver.min_dist_top_down(S1, S2)}")
    print(f"The minimum edit distance is: {solver.min_dist_bottom_up(S1, S2)}")
    print()
    print("*************** End of Testing Edit Distance DP Algorithm ***************")
