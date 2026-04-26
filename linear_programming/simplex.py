from typing import Any
import numpy as np


class Tableau:
    """Operate on simplex tableaus"""

    maxiter = 100

    def __init__(
        self, tableau: np.ndarray, n_vars: int, n_artificial_vars: int
    ) -> None:
        if tableau.dtype != "float64":
            raise TypeError("Tableau must have type float64")

        if not (tableau[:, -1] >= 0).all():
            raise ValueError("RHS must be > 0")

        if n_vars < 2 or n_artificial_vars < 0:
            raise ValueError(
                "number of (artificial) variables must be a natural number"
            )

        self.tableau = tableau
        self.n_rows, n_cols = tableau.shape

        self.n_vars = n_vars
        self.n_artificial_vars = n_artificial_vars

        self.n_stages = (self.n_artificial_vars > 0) + 1
        self.n_slack = n_cols - self.n_vars - self.n_artificial_vars - 1

        self.objectives = ["max"]
        if self.n_artificial_vars:
            self.objectives.append("min")

        self.col_titles = self.generate_col_titles()

        self.stop_iter = False

    def generate_col_titles(self) -> list[str]:
        string_starts = ["x", "s"]
        titles = []

        for i in range(2):
            for j in range((self.n_vars, self.n_slack)[i]):
                titles.append(string_starts[i] + str(j + 1))

        titles.append("RHS")
        return titles

    def find_pivot(self) -> tuple[Any, Any]:
        objective = self.objectives[-1]

        sign = (objective == "min") - (objective == "max")
        col_idx = np.argmax(sign * self.tableau[0, :-1])

        if sign * self.tableau[0, col_idx] <= 0:
            self.stop_iter = True
            return 0, 0

        s = slice(self.n_stages, self.n_rows)

        dividend = self.tableau[s, -1]
        divisor = self.tableau[s, col_idx]

        nans = np.full(self.n_rows - self.n_stages, np.nan)
        quotients = np.divide(dividend, divisor, out=nans, where=divisor > 0)

        row_idx = np.nanargmin(quotients) + self.n_stages
        return row_idx, col_idx

    # 🔥 OPTIMIZED PIVOT (major speed improvement)
    def pivot(self, row_idx: int, col_idx: int) -> np.ndarray:
        tableau = self.tableau

        piv_row = tableau[row_idx].copy()
        piv_val = piv_row[col_idx]

        # normalize pivot row
        piv_row /= piv_val

        # vectorized elimination (FAST)
        tableau -= tableau[:, col_idx][:, None] * piv_row

        tableau[row_idx] = piv_row
        self.tableau = tableau

        return tableau

    def change_stage(self) -> np.ndarray:
        self.objectives.pop()

        if not self.objectives:
            return self.tableau

        s = slice(-self.n_artificial_vars - 1, -1)

        self.tableau = np.delete(self.tableau, s, axis=1)
        self.tableau = np.delete(self.tableau, 0, axis=0)

        self.n_stages = 1
        self.n_rows -= 1
        self.n_artificial_vars = 0
        self.stop_iter = False

        return self.tableau

    def run_simplex(self) -> dict[Any, Any]:
        """Run simplex algorithm until optimal solution is found."""

        maxiter = Tableau.maxiter

        for iteration in range(maxiter):

            if not self.objectives:
                return self.interpret_tableau()

            row_idx, col_idx = self.find_pivot()

            if self.stop_iter:
                self.tableau = self.change_stage()
            else:
                self.tableau = self.pivot(row_idx, col_idx)

        #  FIXED: no silent failure anymore
        raise ValueError(
            "Simplex algorithm failed to converge.\n"
            f"- Iterations performed: {maxiter}\n"
            f"- Remaining objectives: {self.objectives}\n"
            "Possible causes:\n"
            "- Cycling (degeneracy)\n"
            "- Unbounded solution\n"
            "- Ill-conditioned input"
        )

    def interpret_tableau(self) -> dict[str, float]:
        output_dict = {"P": abs(self.tableau[0, -1])}

        for i in range(self.n_vars):
            nonzero = np.nonzero(self.tableau[:, i])
            if len(nonzero[0]) == 0:
                continue

            r = nonzero[0][0]
            val = self.tableau[r, i]

            if len(nonzero[0]) == 1 and val == 1:
                output_dict[self.col_titles[i]] = self.tableau[r, -1]

        return output_dict


if __name__ == "__main__":
    import doctest
    doctest.testmod()