def compute_transform_tables(
    s1, s2, insert_cost, delete_cost, replace_cost, swap_cost, ignore_case=False
):
    if ignore_case:
        s1, s2 = s1.lower(), s2.lower()

    m, n = len(s1), len(s2)

    # cost table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # operation table
    op = [["0"] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(1, m + 1):
        dp[i][0] = i * delete_cost
        op[i][0] = "D" + s1[i - 1]
    for j in range(1, n + 1):
        dp[0][j] = j * insert_cost
        op[0][j] = "I" + s2[j - 1]

    # Fill DP tables
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                op[i][j] = "C" + s1[i - 1]
            else:
                replace = dp[i - 1][j - 1] + replace_cost
                insert = dp[i][j - 1] + insert_cost
                delete = dp[i - 1][j] + delete_cost

                # Choose min cost, tie-breaking in order: replace > insert > delete
                min_cost = min(replace, insert, delete)
                dp[i][j] = min_cost

                if min_cost == replace:
                    op[i][j] = "R" + s2[j - 1]
                elif min_cost == insert:
                    op[i][j] = "I" + s2[j - 1]
                else:
                    op[i][j] = "D" + s1[i - 1]

    return dp, op
