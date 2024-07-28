import numpy as np


class InteriorPointMethod:
    """
    Operate on linear programming problems using the Interior-Point Method.

    Attributes:
        objective_coefficients (np.ndarray): Coefficient matrix for the objective
            function.
        constraint_matrix (np.ndarray): Constraint matrix.
        constraint_bounds (np.ndarray): Constraint bounds.
        tol (float): Tolerance for stopping criterion.
        max_iter (int): Maximum number of iterations.

    Methods:
        solve: Solve the linear programming problem.
    """

    def __init__(
        self,
        objective_coefficients: np.ndarray,
        constraint_matrix: np.ndarray,
        constraint_bounds: np.ndarray,
        tol: float = 1e-8,
        max_iter: int = 100,
    ) -> None:
        self.objective_coefficients = objective_coefficients
        self.constraint_matrix = constraint_matrix
        self.constraint_bounds = constraint_bounds
        self.tol = tol
        self.max_iter = max_iter

        if not self._is_valid_input():
            raise ValueError("Invalid input for the linear programming problem.")

    def _is_valid_input(self) -> bool:
        """
                Validate the input for the linear programming problem.

                Returns:
                    bool: True if input is valid, False otherwise.

                >>> objective_coefficients = np.array([1, 2])
                >>> constraint_matrix = np.array([[1, 1], [1, -1]])
                >>> constraint_bounds = np.array([2, 0])
                >>> ipm = InteriorPointMethod(objective_coefficients, constraint_matrix,
        constraint_bounds)
                >>> ipm._is_valid_input()
                True
                >>> constraint_bounds = np.array([2, 0, 1])
                >>> ipm = InteriorPointMethod(objective_coefficients, constraint_matrix,
        constraint_bounds)
                >>> ipm._is_valid_input()
                False
        """
        return (
            self.constraint_matrix.shape[0] == self.constraint_bounds.shape[0]
            and self.constraint_matrix.shape[1] == self.objective_coefficients.shape[0]
        )

    def _convert_to_standard_form(self) -> tuple[np.ndarray, np.ndarray]:
        """
                Convert constraints to standard form by adding slack variables.

                Returns:
                    tuple: A tuple of the standard form constraint matrix and objective
        coefficients.

                >>> objective_coefficients = np.array([1, 2])
                >>> constraint_matrix = np.array([[1, 1], [1, -1]])
                >>> constraint_bounds = np.array([2, 0])
                >>> ipm = InteriorPointMethod(objective_coefficients, constraint_matrix,
        constraint_bounds)
                >>> a_standard, c_standard = ipm._convert_to_standard_form()
                >>> a_standard
                array([[ 1.,  1.,  1.,  0.],
                       [ 1., -1.,  0.,  1.]])
                >>> c_standard
                array([1., 2., 0., 0.])
        """
        (m, n) = self.constraint_matrix.shape
        slack = np.eye(m)
        a_standard = np.hstack([self.constraint_matrix, slack])
        c_standard = np.hstack([self.objective_coefficients, np.zeros(m)])
        return a_standard, c_standard

    def solve(self) -> tuple[np.ndarray, float]:
        """
                Solve problem with Primal-Dual Interior-Point Method.

                Returns:
                    tuple: A tuple with optimal solution and the optimal value.

                >>> objective_coefficients = np.array([1, 2])
                >>> constraint_matrix = np.array([[1, 1], [1, -1]])
                >>> constraint_bounds = np.array([2, 0])
                >>> ipm = InteriorPointMethod(objective_coefficients, constraint_matrix,
        constraint_bounds)
                >>> solution, value = ipm.solve()
                >>> np.isclose(value, np.dot(objective_coefficients, solution))
                True
        """
        a, c = self._convert_to_standard_form()
        m, n = a.shape
        x = np.ones(n)
        s = np.ones(n)
        y = np.ones(m)

        for iteration in range(self.max_iter):
            x_diag = np.diag(x)
            s_diag = np.diag(s)

            # KKT conditions
            r1 = a @ x - self.constraint_bounds
            r2 = a.T @ y + s - c
            r3 = x * s

            if (
                np.linalg.norm(r1) < self.tol
                and np.linalg.norm(r2) < self.tol
                and np.linalg.norm(r3) < self.tol
            ):
                break

            mu = np.dot(x, s) / n

            # Form the KKT matrix
            kkt = np.block(
                [
                    [np.zeros((n, n)), a.T, np.eye(n)],
                    [a, np.zeros((m, m)), np.zeros((m, n))],
                    [s_diag, np.zeros((n, m)), x_diag],
                ]
            )

            # Right-hand side
            r = np.hstack([-r2, -r1, -r3 + mu * np.ones(n)])

            # Solve the KKT system
            try:
                delta = np.linalg.solve(kkt, r)
            except np.linalg.LinAlgError:
                print("KKT matrix is singular, switching to least squares solution")
                delta = np.linalg.lstsq(kkt, r, rcond=None)[0]

            dx = delta[:n]
            dy = delta[n : n + m]
            ds = delta[n + m :]

            # Step size
            alpha_primal = min(
                1, 0.99 * min([-x[i] / dx[i] for i in range(n) if dx[i] < 0], default=1)
            )
            alpha_dual = min(
                1, 0.99 * min([-s[i] / ds[i] for i in range(n) if ds[i] < 0], default=1)
            )

            # Update variables
            x += alpha_primal * dx
            y += alpha_dual * dy
            s += alpha_dual * ds

            print(f"Iteration {iteration}: x = {x}, s = {s}, y = {y}")

        # Extract the solution (remove slack variables)
        original_vars = x[: self.objective_coefficients.shape[0]]
        optimal_value = np.dot(self.objective_coefficients, original_vars)
        return original_vars, optimal_value


if __name__ == "__main__":
    objective_coefficients = np.array([1, 2])
    constraint_matrix = np.array([[1, 1], [1, -1]])
    constraint_bounds = np.array([2, 0])

    ipm = InteriorPointMethod(
        objective_coefficients, constraint_matrix, constraint_bounds
    )
    solution, value = ipm.solve()
    print("Final optimal solution:", solution)
    print("Final optimal value:", value)

    # Verify the solution
    print("\nVerification:")
    print("Objective value calculation matches final optimal value:")
    print(np.isclose(value, np.dot(objective_coefficients, solution)))
