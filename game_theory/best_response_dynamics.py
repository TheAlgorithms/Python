def best_response_dynamics(payoff_matrix_A, payoff_matrix_B, iterations=10):
    n = payoff_matrix_A.shape[0]
    m = payoff_matrix_A.shape[1]

    # Initialize strategies
    strategy_A = np.ones(n) / n
    strategy_B = np.ones(m) / m

    for _ in range(iterations):
        # Update strategy A
        response_A = np.argmax(payoff_matrix_A @ strategy_B)
        strategy_A = np.zeros(n)
        strategy_A[response_A] = 1

        # Update strategy B
        response_B = np.argmax(payoff_matrix_B.T @ strategy_A)
        strategy_B = np.zeros(m)
        strategy_B[response_B] = 1

    return strategy_A, strategy_B


# Example usage
payoff_A = np.array([[3, 0], [5, 1]])
payoff_B = np.array([[2, 4], [0, 2]])
strategies = best_response_dynamics(payoff_A, payoff_B)
print("Final strategies:", strategies)
