import numpy as np


def shapley_value(payoff_matrix):
    n = payoff_matrix.shape[1]  # Number of players
    shapley_values = np.zeros(n)  # Initialize Shapley values

    # Iterate over each player
    for i in range(n):
        # Iterate over all subsets of players (from 0 to 2^n - 1)
        for s in range(1 << n):  # All subsets of players
            if (s & (1 << i)) == 0:  # If player i is not in subset S
                continue

            # Calculate the value of the subset S without player i
            s_without_i = s & ~(1 << i)  # Remove player i from the subset
            marginal_contribution = payoff_matrix[s][i] - (
                payoff_matrix[s_without_i][i] if s_without_i else 0
            )

            # Count the size of the subset S
            size_of_s = bin(s).count("1")  # Number of players in subset S
            shapley_values[i] += marginal_contribution / (
                size_of_s * (n - size_of_s)
            )  # Normalize by size of S

    return shapley_values


# Example usage
# Payoff matrix with payoffs for 4 coalitions: {}, {1}, {2}, {1, 2}
payoff_matrix = np.array([[0, 0], [1, 0], [0, 2], [3, 4]])
shapley_vals = shapley_value(payoff_matrix)
print("Shapley Values:", shapley_vals)
