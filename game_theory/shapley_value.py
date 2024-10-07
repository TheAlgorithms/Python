def shapley_value(payoff_matrix):
    n = payoff_matrix.shape[0]
    shapley_values = np.zeros(n)

    for i in range(n):
        for s in range(1 << n):  # All subsets of players
            if (s & (1 << i)) == 0:  # i not in S
                continue

            s_without_i = s & ~(1 << i)
            marginal_contribution = payoff_matrix[s][i] - (
                payoff_matrix[s_without_i][i] if s_without_i else 0
            )
            shapley_values[i] += marginal_contribution / (
                len(bin(s)) - 2
            )  # Normalize by size of S

    return shapley_values


# Example usage
payoff_matrix = np.array([[1, 2], [3, 4]])
shapley_vals = shapley_value(payoff_matrix)
print("Shapley Values:", shapley_vals)
