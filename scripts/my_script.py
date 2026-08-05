import numpy as np


class Tableau:
    def __init__(self, tableau):
        self.tableau = tableau
        self.num_rows, self.num_cols = tableau.shape

    def pivot(self, row, col):
        # Divide the pivot row by the pivot element
        self.tableau[row] /= self.tableau[row, col]

        # Subtract multiples of the pivot row from all other rows
        for i in range(self.num_rows):
            if i != row:
                self.tableau[i] -= self.tableau[i, col] * self.tableau[row]

    def find_pivot_column(self):
        # The pivot column is the most negative value in the objective row
        obj_row = self.tableau[0, :-1]
        pivot_col = np.argmin(obj_row)
        if obj_row[pivot_col] >= 0:
            return -1  # No negative value, we are done
        return pivot_col

    def find_pivot_row(self, pivot_col):
        # Calculate the ratio of the righthand side to the pivotcolumnentries
        rhs = self.tableau[1:, -1]
        col = self.tableau[1:, pivot_col]
        ratios = []
        for i in range(len(rhs)):
            if col[i] > 0:
                ratios.append(rhs[i] / col[i])
            else:
                ratios.append(np.inf)  # Ignore non-positive entries

        pivot_row = np.argmin(ratios) + 1  # Add 1 because we ignored row 0
        if np.isinf(ratios[pivot_row - 1]):
            return -1  # No valid pivot row (unbounded)
        return pivot_row

    def run_simplex(self):
        while True:
            pivot_col = self.find_pivot_column()
            if pivot_col == -1:
                break  # Optimal solution found

            pivot_row = self.find_pivot_row(pivot_col)
            if pivot_row == -1:
                raise ValueError("Linear program is unbounded.")

            self.pivot(pivot_row, pivot_col)

        return self.extract_solution()

    def extract_solution(self):
        solution = np.zeros(self.num_cols - 1)
        for i in range(1, self.num_rows):
            col = self.tableau[i, :-1]
            if np.count_nonzero(col) == 1:
                solution[np.argmax(col)] = self.tableau[i, -1]
        return solution, -self.tableau[0, -1]  # Returnsolutionandoptimalvalue


def construct_tableau(objective, constraints, rhs):
    """
    Constructs the initial tableau for the simplex algorithm.

    Parameters:
    - objective: List of coefficients of the objective function (maximize).
    - constraints: List of lists representing coefficients of the constraints.
    - rhs: List of right-hand-side values of constraints.

    Returns:
    - tableau: A numpy array representing the initial simplex tableau.
    """
    n_constraints = len(constraints)
    n_vars = len(objective)

    # Creating the tableau matrix
    tableau = np.zeros((n_constraints + 1, n_vars + n_constraints + 1))

    # Fill the objective function (row 0, cols 0 to n_vars)
    tableau[0, :n_vars] = -np.array(objective)  # Maximization -> negate

    # Fill the constraints
    for i in range(n_constraints):
        tableau[i + 1, :n_vars] = constraints[i]
        tableau[i + 1, n_vars + i] = 1  # Slack variable
        tableau[i + 1, -1] = rhs[i]  # RHS of the constraints

    return tableau


def solve_linear_program(objective, constraints, rhs):
    # Constructing the tableau
    tableau = construct_tableau(objective, constraints, rhs)

    # Instantiate the Tableau class
    simplex_tableau = Tableau(tableau)

    # Run the simplex algorithm
    solution, optimal_value = simplex_tableau.run_simplex()

    # Output the solution
    print("Optimal Solution:", solution)
    print("Optimal Value:", optimal_value)


# Example usage
if __name__ == "__main__":
    # Coefficients of the objective function: maximize 3x1 + 2x2
    objective = [3, 2]

    # Coefficients of the constraints:
    # 2x1 + x2 <= 18
    # x1 + 2x2 <= 20
    constraints = [[2, 1], [1, 2]]

    # Right-hand side of the constraints
    rhs = [18, 20]

    # Solve the linear program
    solve_linear_program(objective, constraints, rhs)
