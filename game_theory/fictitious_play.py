def fictitious_play(payoff_matrix_a, payoff_matrix_b, iterations=100):
    n = payoff_matrix_a.shape[0]
    m = payoff_matrix_a.shape[1]

    # Initialize counts and strategies
    counts_a = np.zeros(n)
    counts_b = np.zeros(m)
    strategy_a = np.ones(n) / n
    strategy_b = np.ones(m) / m

    for _ in range(iterations):
        # Update counts
        counts_a += strategy_a
        counts_b += strategy_b

        # Calculate best responses
        best_response_a = np.argmax(payoff_matrix_a @ strategy_b)
        best_response_b = np.argmax(payoff_matrix_b.T @ strategy_a)

        # Update strategies
        strategy_a = np.zeros(n)
        strategy_a[best_response_a] = 1
        strategy_b = np.zeros(m)
        strategy_b[best_response_b] = 1

    return strategy_a, strategy_b


# Example usage
payoff_a = np.array([[3, 0], [5, 1]])
payoff_b = np.array([[2, 4], [0, 2]])
strategies = fictitious_play(payoff_a, payoff_b)
print("Fictitious Play strategies:", strategies)
