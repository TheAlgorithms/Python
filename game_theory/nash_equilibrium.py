import numpy as np
from scipy.optimize import linprog

def find_nash_equilibrium(payoff_matrix_A, payoff_matrix_B):
    n = payoff_matrix_A.shape[0]
    m = payoff_matrix_A.shape[1]

    # Solve for player A
    c = [-1] * n  # Objective: maximize A's payoff
    A_ub = -payoff_matrix_A  # A's constraints
    b_ub = [-1] * m

    result_A = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0, None))
    p_A = result_A.x

    # Solve for player B
    c = [-1] * m  # Objective: maximize B's payoff
    A_ub = -payoff_matrix_B.T  # B's constraints
    b_ub = [-1] * n

    result_B = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0, None))
    p_B = result_B.x

    return p_A, p_B

# Example usage
payoff_A = np.array([[3, 0], [5, 1]])
payoff_B = np.array([[2, 4], [0, 2]])
equilibrium = find_nash_equilibrium(payoff_A, payoff_B)
print("Nash Equilibrium strategies:", equilibrium)
