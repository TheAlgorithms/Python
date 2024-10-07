def best_response_dynamics(payoff_matrix_a, payoff_matrix_b, iterations=10):
    n = payoff_matrix_a.shape[0]
    m = payoff_matrix_a.shape[1]

    # Initialize strategies
    strategy_a = np.ones(n) / n
    strategy_b = np.ones(m) / m

    for _ in range(iterations):
        # Update strategy A
        response_a = np.argmax(payoff_matrix_a @ strategy_b)
        strategy_a = np.zeros(n)
        strategy_a[response_a] = 1

        # Update strategy B
        response_b = np.argmax(payoff_matrix_b.T @ strategy_a)
        strategy_b = np.zeros(m)
        strategy_b[response_b] = 1

    return strategy_a, strategy_b

# Example usage
payoff_a = np.array([[3, 0], [5, 1]])
payoff_b = np.array([[2, 4], [0, 2]])
strategies = best_response_dynamics(payoff_a, payoff_b)
print("Final strategies:", strategies)
