def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()

    result = []
    candidates.sort()  # Sort the candidates for easier pruning
    backtrack(0, target, [])
    return result

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))
