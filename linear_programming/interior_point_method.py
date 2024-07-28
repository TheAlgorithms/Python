"""
Python implementation of the Primal-Dual Interior-Point Method for solving linear programs with
- `>=`, `<=`, and `=` constraints and
- each variable `x1, x2, ... >= 0`.

Resources:
https://en.wikipedia.org/wiki/Interior-point_method
"""

import numpy as np

class InteriorPointMethod:
    """
    Operate on linear programming problems using the Primal-Dual Interior-Point Method.

    Attributes:
        c (np.ndarray): Coefficient matrix for the objective function.
        a (np.ndarray): Constraint matrix.
        b (np.ndarray): Constraint bounds.
        tol (float): Tolerance for stopping criterion.
        max_iter (int): Maximum number of iterations.
    """

    def __init__(self, c: np.ndarray, a: np.ndarray, b: np.ndarray, tol: float = 1e-8, max_iter: int = 100) -> None:
        self.c = c
        self.a = a
        self.b = b
        self.tol = tol
        self.max_iter = max_iter

        if not self._is_valid_input():
            raise ValueError("Invalid input for the linear programming problem.")

    def _is_valid_input(self) -> bool:
        """Validate the input for the linear programming problem."""
        return (self.a.shape[0] == self.b.shape[0]) and (self.a.shape[1] == self.c.shape[0])

    def _convert_to_standard_form(self):
        """Convert constraints to standard form by adding slack and surplus variables."""
        (m, n) = self.a.shape
        slack_surplus = np.eye(m)
        a_standard = np.hstack([self.a, slack_surplus])
        c_standard = np.hstack([self.c, np.zeros(m)])
        return a_standard, c_standard

    def solve(self) -> tuple[np.ndarray, float]:
        """
        Solve the linear programming problem using the Primal-Dual Interior-Point Method.

        Returns:
            tuple: A tuple containing the optimal solution and the optimal value.
        """
        a, c = self._convert_to_standard_form()
        m, n = a.shape
        x = np.ones(n)
        s = np.ones(n)
        y = np.ones(m)

        for _ in range(self.max_iter):
            x_diag = np.diag(x)
            s_diag = np.diag(s)

            # KKT conditions
            r1 = a @ x - self.b
            r2 = a.T @ y + s - c
            r3 = x * s

            if np.linalg.norm(r1) < self.tol and np.linalg.norm(r2) < self.tol and np.linalg.norm(r3) < self.tol:
                break

            mu = np.dot(x, s) / n

            # Form the KKT matrix
            kkt = np.block([
                [np.zeros((n, n)), a.T, np.eye(n)],
                [a, np.zeros((m, m)), np.zeros((m, n))],
                [s_diag, np.zeros((n, m)), x_diag]
            ])

            # Right-hand side
            r = np.hstack([-r2, -r1, -r3 + mu * np.ones(n)])

            # Solve the KKT system
            delta = np.linalg.solve(kkt, r)

            dx = delta[:n]
            dy = delta[n:n+m]
            ds = delta[n+m:]

            # Step size
            alpha_primal = min(1, 0.99 * min(-x[dx < 0] / dx[dx < 0], default=1))
            alpha_dual = min(1, 0.99 * min(-s[ds < 0] / ds[ds < 0], default=1))

            # Update variables
            x += alpha_primal * dx
            y += alpha_dual * dy
            s += alpha_dual * ds

        optimal_value = np.dot(c, x)
        return x, optimal_value


if __name__ == "__main__":
    c = np.array([1, 2])
    a = np.array([[1, 1], [1, -1]])
    b = np.array([2, 0])

    ipm = InteriorPointMethod(c, a, b)
    solution, value = ipm.solve()
    print("Optimal solution:", solution)
    print("Optimal value:", value)
