import numpy as np
from scipy.optimize import linprog


def find_nash_equilibrium(payoff_matrix_a, payoff_matrix_b):
    n = payoff_matrix_a.shape[0]
    m = payoff_matrix_a.shape[1]

    # Solve for player A
    c = [-1] * n  # Objective: maximize A's payoff
    a_ub = -payoff_matrix_a  # A's constraints
    b_ub = [-1] * m

    result_a = linprog(c, A_ub=a_ub, b_ub=b_ub, bounds=(0, None))
    p_a = result_a.x

    # Solve for player B
    c = [-1] * m  # Objective: maximize B's payoff
    a_ub = -payoff_matrix_b.T  # B's constraints
    b_ub = [-1] * n

    result_b = linprog(c, A_ub=a_ub, b_ub=b_ub, bounds=(0, None))
    p_b = result_b.x

    return p_a, p_b


# Example usage
payoff_a = np.array([[3, 0], [5, 1]])
payoff_b = np.array([[2, 4], [0, 2]])
equilibrium = find_nash_equilibrium(payoff_a, payoff_b)
print("Nash Equilibrium strategies:", equilibrium)
