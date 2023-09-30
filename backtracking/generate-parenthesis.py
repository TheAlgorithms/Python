// Problem Link: https://leetcode.com/problems/generate-parentheses/ 
// Title: 22. Generate Parentheses
// This python program generates all valid combinations of n pairs of parentheses.
// It uses a recursive approach with backtracking to explore and construct valid combinations.


def generateParenthesis(n):
    ans = []

    # Helper function to generate valid parentheses
    def solve(open, close, output):
        # Base case: If both open and close parentheses are used up, add the current output to the result list
        if open == 0 and close == 0:
            ans.append(output)
            return

        # Add an open parenthesis if there are remaining open parentheses
        if open > 0:
            solve(open - 1, close, output + "(")

        # Add a close parenthesis if there are more open than close parentheses
        if close > open:
            solve(open, close - 1, output + ")")

    solve(n, n, "")  # Call the recursive solver
    return ans  # Return the list of valid parentheses

n = 3  # Example input
parentheses = generateParenthesis(n)

# Display the generated valid parentheses
print(f"Valid parentheses of length {n}:")
for parenthesis in parentheses:
    print(parenthesis)
