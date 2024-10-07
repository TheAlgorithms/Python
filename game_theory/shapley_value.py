def shapley_value(payoff_matrix):
    n = payoff_matrix.shape[0]
    shapley_values = np.zeros(n)

    for i in range(n):
        for S in range(1 << n):  # All subsets of players
            if (S & (1 << i)) == 0:  # i not in S
                continue

            S_without_i = S & ~(1 << i)
            marginal_contribution = payoff_matrix[S][i] - (
                payoff_matrix[S_without_i][i] if S_without_i else 0
            )
            shapley_values[i] += marginal_contribution / (
                len(bin(S)) - 2
            )  # Normalize by size of S

    return shapley_values


# Example usage
payoff_matrix = np.array([[1, 2], [3, 4]])
shapley_vals = shapley_value(payoff_matrix)
print("Shapley Values:", shapley_vals)
