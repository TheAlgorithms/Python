def fictitious_play(payoff_matrix_A, payoff_matrix_B, iterations=100):
    n = payoff_matrix_A.shape[0]
    m = payoff_matrix_A.shape[1]

    # Initialize counts and strategies
    counts_A = np.zeros(n)
    counts_B = np.zeros(m)
    strategy_A = np.ones(n) / n
    strategy_B = np.ones(m) / m

    for _ in range(iterations):
        # Update counts
        counts_A += strategy_A
        counts_B += strategy_B

        # Calculate best responses
        best_response_A = np.argmax(payoff_matrix_A @ strategy_B)
        best_response_B = np.argmax(payoff_matrix_B.T @ strategy_A)

        # Update strategies
        strategy_A = np.zeros(n)
        strategy_A[best_response_A] = 1
        strategy_B = np.zeros(m)
        strategy_B[best_response_B] = 1

    return strategy_A, strategy_B


# Example usage
payoff_A = np.array([[3, 0], [5, 1]])
payoff_B = np.array([[2, 4], [0, 2]])
strategies = fictitious_play(payoff_A, payoff_B)
print("Fictitious Play strategies:", strategies)
