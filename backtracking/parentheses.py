def generateParenthesis(n):
    def backtrack(combination, open_count, close_count):
        if len(combination) == 2 * n:
            valid_combinations.append(combination)
            return
        if open_count < n:
            backtrack(combination + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(combination + ")", open_count, close_count + 1)

    valid_combinations = []
    backtrack("", 0, 0)
    return valid_combinations


n = 3  # You can change the value of n to generate combinations for a different number of pairs of parentheses
result = generateParenthesis(n)
for combination in result:
    print(combination)
