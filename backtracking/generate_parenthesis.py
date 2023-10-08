"""
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    Constraints: 1 <= n <= 8
    Problem source: https://leetcode.com/problems/generate-parentheses/
"""

class Solution:
    def generateParenthesis(self, n):
        valid = []

        # Helper function to generate valid combinations
        def generate(s, open_count, close_count):
            if open_count == 0 and close_count == 0:
                valid.append(s)
                return

            if open_count > 0:
                s += '('
                generate(s, open_count - 1, close_count)
                s = s[:-1]

            if close_count > 0 and open_count < close_count:
                s += ')'
                generate(s, open_count, close_count - 1)
                s = s[:-1]

        if n < 0:
            raise ValueError("Input value must be non-negative")

        # Start the generation process with an empty string and n opening and closing parentheses
        generate('', n, n)
        """
        The function employs backtracking to generate all valid combinations of n pairs of parentheses. It maintains two counters, open_count and close_count, representing available open and close parentheses.

        It starts with an empty string s and both counters set to n.

        It recursively explores two possibilities:

        Adding an open parenthesis '(' if open_count > 0.
        Adding a close parenthesis ')' if close_count > 0 and there are open parentheses available (i.e., open_count < close_count).
        When both counters reach zero, it means a valid combination is formed, and it's added to the valid list.

        The code then tries different combinations by backtracking (removing the last added parenthesis) and continues until all possibilities are exhausted.

        The input is validated to ensure it's a non-negative integer, and a ValueError is raised for invalid input.

        The valid combinations are returned as the result.
        """

        return valid


try:
    # Input the value of n from the user
    n = int(input("Enter a value for n: "))

    # Create an instance of the Solution class and generate valid combinations
    solution = Solution()
    result = solution.generateParenthesis(n)

    # Return the valid combinations
    print(result)
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")