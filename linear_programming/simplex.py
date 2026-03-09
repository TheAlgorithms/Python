"""
Python implementation of the simplex algorithm for solving linear programs in
tabular form with
- `>=`, `<=`, and `=` constraints and
- each variable `x1, x2, ...>= 0`.

See https://gist.github.com/imengus/f9619a568f7da5bc74eaf20169a24d98 for how to
convert linear programs to simplex tableaus, and the steps taken in the simplex
algorithm.

Resources:
https://en.wikipedia.org/wiki/Simplex_algorithm
https://tinyurl.com/simplex4beginners
"""

from typing import Any

import numpy as np


class Tableau:
    """Operate on simplex tableaus

    >>> Tableau(np.array([[-1,-1,0,0,1],[1,3,1,0,4],[3,1,0,1,4]]), 2, 2)
    Traceback (most recent call last):
    ...
    TypeError: Tableau must have type float64

    >>> Tableau(np.array([[-1,-1,0,0,-1],[1,3,1,0,4],[3,1,0,1,4.]]), 2, 2)
    Traceback (most recent call last):
    ...
    ValueError: RHS must be > 0

    >>> Tableau(np.array([[-1,-1,0,0,1],[1,3,1,0,4],[3,1,0,1,4.]]), -2, 2)
    Traceback (most recent call last):
    ...
    ValueError: number of (artificial) variables must be a natural number
    """

    # Max iteration number to prevent cycling
    maxiter = 100

    def __init__(
        self, tableau: np.ndarray, n_vars: int, n_artificial_vars: int
    ) -> None:
        if tableau.dtype != "float64":
            raise TypeError("Tableau must have type float64")

        # Check if RHS is negative
        if not (tableau[:, -1] >= 0).all():
            raise ValueError("RHS must be > 0")

        if n_vars < 2 or n_artificial_vars < 0:
            raise ValueError(
                "number of (artificial) variables must be a natural number"
            )

        self.tableau = tableau
        self.n_rows, n_cols = tableau.shape

        # Number of decision variables x1, x2, x3...
        self.n_vars, self.n_artificial_vars = n_vars, n_artificial_vars

        # 2 if there are >= or == constraints (nonstandard), 1 otherwise (std)
        self.n_stages = (self.n_artificial_vars > 0) + 1

        # Number of slack variables added to make inequalities into equalities
        self.n_slack = n_cols - self.n_vars - self.n_artificial_vars - 1

        # Objectives for each stage
        self.objectives = ["max"]

        # In two stage simplex, first minimise then maximise
        if self.n_artificial_vars:
            self.objectives.append("min")

        self.col_titles = self.generate_col_titles()

        # Index of current pivot row and column
        self.row_idx = None
        self.col_idx = None

        # Does objective row only contain (non)-negative values?
        self.stop_iter = False

    def generate_col_titles(self) -> list[str]:
        """Generate column titles for tableau of specific dimensions

        >>> Tableau(np.array([[-1,-1,0,0,1],[1,3,1,0,4],[3,1,0,1,4.]]),
        ... 2, 0).generate_col_titles()
        ['x1', 'x2', 's1', 's2', 'RHS']

        >>> Tableau(np.array([[-1,-1,0,0,1],[1,3,1,0,4],[3,1,0,1,4.]]),
        ... 2, 2).generate_col_titles()
        ['x1', 'x2', 'RHS']
        """
        args = (self.n_vars, self.n_slack)

        # decision | slack
        string_starts = ["x", "s"]
        titles = []
        for i in range(2):
            for j in range(args[i]):
                titles.append(string_starts[i] + str(j + 1))
        titles.append("RHS")
        return titles

    def find_pivot(self) -> tuple[Any, Any]:
        """Finds the pivot row and column.
        >>> tuple(int(x) for x in Tableau(np.array([[-2,1,0,0,0], [3,1,1,0,6],
        ... [1,2,0,1,7.]]), 2, 0).find_pivot())
        (1, 0)
        """
        objective = self.objectives[-1]

        # Find entries of highest magnitude in objective rows
        sign = (objective == "min") - (objective == "max")
        col_idx = np.argmax(sign * self.tableau[0, :-1])

        # Choice is only valid if below 0 for maximise, and above for minimise
        if sign * self.tableau[0, col_idx] <= 0:
            self.stop_iter = True
            return 0, 0

        # Pivot row is chosen as having the lowest quotient when elements of
        # the pivot column divide the right-hand side

        # Slice excluding the objective rows
        s = slice(self.n_stages, self.n_rows)

        # RHS
        dividend = self.tableau[s, -1]

        # Elements of pivot column within slice
        divisor = self.tableau[s, col_idx]

        # Array filled with nans
        nans = np.full(self.n_rows - self.n_stages, np.nan)

        # If element in pivot column is greater than zero, return
        # quotient or nan otherwise
        quotients = np.divide(dividend, divisor, out=nans, where=divisor > 0)

        # Arg of minimum quotient excluding the nan values. n_stages is added
        # to compensate for earlier exclusion of objective columns
        row_idx = np.nanargmin(quotients) + self.n_stages
        return row_idx, col_idx

    def pivot(self, row_idx: int, col_idx: int) -> np.ndarray:
        """Pivots on value on the intersection of pivot row and column.

        >>> Tableau(np.array([[-2,-3,0,0,0],[1,3,1,0,4],[3,1,0,1,4.]]),
        ... 2, 2).pivot(1, 0).tolist()
        ... # doctest: +NORMALIZE_WHITESPACE
        [[0.0, 3.0, 2.0, 0.0, 8.0],
        [1.0, 3.0, 1.0, 0.0, 4.0],
        [0.0, -8.0, -3.0, 1.0, -8.0]]
        """
        # Avoid changes to original tableau
        piv_row = self.tableau[row_idx].copy()

        piv_val = piv_row[col_idx]

        # Entry becomes 1
        piv_row *= 1 / piv_val

        # Variable in pivot column becomes basic, ie the only non-zero entry
        for idx, coeff in enumerate(self.tableau[:, col_idx]):
            self.tableau[idx] += -coeff * piv_row
        self.tableau[row_idx] = piv_row
        return self.tableau

    def change_stage(self) -> np.ndarray:
        """Exits first phase of the two-stage method by deleting artificial
        rows and columns, or completes the algorithm if exiting the standard
        case.

        >>> Tableau(np.array([
        ... [3, 3, -1, -1, 0, 0, 4],
        ... [2, 1, 0, 0, 0, 0, 0.],
        ... [1, 2, -1, 0, 1, 0, 2],
        ... [2, 1, 0, -1, 0, 1, 2]
        ... ]), 2, 2).change_stage().tolist()
        ... # doctest: +NORMALIZE_WHITESPACE
        [[2.0, 1.0, 0.0, 0.0, 0.0],
        [1.0, 2.0, -1.0, 0.0, 2.0],
        [2.0, 1.0, 0.0, -1.0, 2.0]]
        """
        # Objective of original objective row remains
        self.objectives.pop()

        if not self.objectives:
            return self.tableau

        # Slice containing ids for artificial columns
        s = slice(-self.n_artificial_vars - 1, -1)

        # Delete the artificial variable columns
        self.tableau = np.delete(self.tableau, s, axis=1)

        # Delete the objective row of the first stage
        self.tableau = np.delete(self.tableau, 0, axis=0)

        self.n_stages = 1
        self.n_rows -= 1
        self.n_artificial_vars = 0
        self.stop_iter = False
        return self.tableau

    def run_simplex(self) -> dict[Any, Any]:
        """Operate on tableau until objective function cannot be
        improved further.

        # Standard linear program:
        Max:  x1 +  x2
        ST:   x1 + 3x2 <= 4
             3x1 +  x2 <= 4
        >>> {key: float(value) for key, value in Tableau(np.array([[-1,-1,0,0,0],
        ... [1,3,1,0,4],[3,1,0,1,4.]]), 2, 0).run_simplex().items()}
        {'P': 2.0, 'x1': 1.0, 'x2': 1.0}

        # Standard linear program with 3 variables:
        Max: 3x1 +  x2 + 3x3
        ST:  2x1 +  x2 +  x3 ≤ 2
              x1 + 2x2 + 3x3 ≤ 5
             2x1 + 2x2 +  x3 ≤ 6
        >>> {key: float(value) for key, value in Tableau(np.array([
        ... [-3,-1,-3,0,0,0,0],
        ... [2,1,1,1,0,0,2],
        ... [1,2,3,0,1,0,5],
        ... [2,2,1,0,0,1,6.]
        ... ]),3,0).run_simplex().items()} # doctest: +ELLIPSIS
        {'P': 5.4, 'x1': 0.199..., 'x3': 1.6}


        # Optimal tableau input:
        >>> {key: float(value) for key, value in Tableau(np.array([
        ... [0, 0, 0.25, 0.25, 2],
        ... [0, 1, 0.375, -0.125, 1],
        ... [1, 0, -0.125, 0.375, 1]
        ... ]), 2, 0).run_simplex().items()}
        {'P': 2.0, 'x1': 1.0, 'x2': 1.0}

        # Non-standard: >= constraints
        Max: 2x1 + 3x2 +  x3
        ST:   x1 +  x2 +  x3 <= 40
             2x1 +  x2 -  x3 >= 10
                 -  x2 +  x3 >= 10
        >>> {key: float(value) for key, value in Tableau(np.array([
        ... [2, 0, 0, 0, -1, -1, 0, 0, 20],
        ... [-2, -3, -1, 0, 0, 0, 0, 0, 0],
        ... [1, 1, 1, 1, 0, 0, 0, 0, 40],
        ... [2, 1, -1, 0, -1, 0, 1, 0, 10],
        ... [0, -1, 1, 0, 0, -1, 0, 1, 10.]
        ... ]), 3, 2).run_simplex().items()}
        {'P': 70.0, 'x1': 10.0, 'x2': 10.0, 'x3': 20.0}

        # Non standard: minimisation and equalities
        Min: x1 +  x2
        ST: 2x1 +  x2 = 12
            6x1 + 5x2 = 40
        >>> {key: float(value) for key, value in Tableau(np.array([
        ... [8, 6, 0, 0, 52],
        ... [1, 1, 0, 0, 0],
        ... [2, 1, 1, 0, 12],
        ... [6, 5, 0, 1, 40.],
        ... ]), 2, 2).run_simplex().items()}
        {'P': 7.0, 'x1': 5.0, 'x2': 2.0}


        # Pivot on slack variables
        Max: 8x1 + 6x2
        ST:   x1 + 3x2 <= 33
             4x1 + 2x2 <= 48
             2x1 + 4x2 <= 48
              x1 +  x2 >= 10
             x1        >= 2
        >>> {key: float(value) for key, value in Tableau(np.array([
        ... [2, 1, 0, 0, 0, -1, -1, 0, 0, 12.0],
        ... [-8, -6, 0, 0, 0, 0, 0, 0, 0, 0.0],
        ... [1, 3, 1, 0, 0, 0, 0, 0, 0, 33.0],
        ... [4, 2, 0, 1, 0, 0, 0, 0, 0, 60.0],
        ... [2, 4, 0, 0, 1, 0, 0, 0, 0, 48.0],
        ... [1, 1, 0, 0, 0, -1, 0, 1, 0, 10.0],
        ... [1, 0, 0, 0, 0, 0, -1, 0, 1, 2.0]
        ... ]), 2, 2).run_simplex().items()} # doctest: +ELLIPSIS
        {'P': 132.0, 'x1': 12.000... 'x2': 5.999...}
        """
        # Stop simplex algorithm from cycling.
        for _ in range(Tableau.maxiter):
            # Completion of each stage removes an objective. If both stages
            # are complete, then no objectives are left
            if not self.objectives:
                # Find the values of each variable at optimal solution
                return self.interpret_tableau()

            row_idx, col_idx = self.find_pivot()

            # If there are no more negative values in objective row
            if self.stop_iter:
                # Delete artificial variable columns and rows. Update attributes
                self.tableau = self.change_stage()
            else:
                self.tableau = self.pivot(row_idx, col_idx)
        return {}

    def interpret_tableau(self) -> dict[str, float]:
        """Given the final tableau, add the corresponding values of the basic
        decision variables to the `output_dict`
        >>> {key: float(value) for key, value in Tableau(np.array([
        ... [0,0,0.875,0.375,5],
        ... [0,1,0.375,-0.125,1],
        ... [1,0,-0.125,0.375,1]
        ... ]),2, 0).interpret_tableau().items()}
        {'P': 5.0, 'x1': 1.0, 'x2': 1.0}
        """
        # P = RHS of final tableau
        output_dict = {"P": abs(self.tableau[0, -1])}

        for i in range(self.n_vars):
            # Gives indices of nonzero entries in the ith column
            nonzero = np.nonzero(self.tableau[:, i])
            n_nonzero = len(nonzero[0])

            # First entry in the nonzero indices
            nonzero_rowidx = nonzero[0][0]
            nonzero_val = self.tableau[nonzero_rowidx, i]

            # If there is only one nonzero value in column, which is one
            if n_nonzero == 1 and nonzero_val == 1:
                rhs_val = self.tableau[nonzero_rowidx, -1]
                output_dict[self.col_titles[i]] = rhs_val
        return output_dict


if __name__ == "__main__":
    import doctest

    doctest.testmod()
