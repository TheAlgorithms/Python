# Print all subset combinations of n element in given set of r element.


def subset_combinations_dp(elements, n):
    r = len(elements)

    dp = [[] for _ in range(r + 1)]

    dp[0].append(())

    for i in range(1, r + 1):
        for j in range(i, 0, -1):
            for prev_combination in dp[j - 1]:
                dp[j].append(tuple(prev_combination) + (elements[i - 1],))

    combinations = dp[n]

    return combinations

if __name__ == "__main__":
    elements = [10,20,30,40]
    n = 2
    result = subset_combinations_dp(elements, n)
    print(result)
