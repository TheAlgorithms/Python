# Simplex

import numpy as np


class Tableau:
    """Generate and operate on simplex tableaus"""
    def __init__(self, tableau, n_vars, n_art_vars):
        """Initialise Tableau class

        Args:
            lin_prog : list[str]
                Line separated string input in list
            n_art_vars : int
                Number of artificial/ surplus variables needed
        """

        # Initial tableau with no entries
        self.tableau = tableau

        self.n_art_vars = n_art_vars

        # 2 if there are >= or == constraints (nonstandard), 1 otherwise (std)
        self.n_stages = (n_art_vars > 0) + 1

        # Number of rows the initial simplex tableau will have
        self.n_rows = len(tableau[:, 0])

        # Number of columns of the initial simplex tableau
        self.n_cols = len(tableau[0])

        # Number of slack variables added to make inequalities into equalities
        self.n_slack = self.n_rows - self.n_stages

        # Number of decision variables x1, x2, x3...
        self.n_vars = n_vars

        # Values of non-basic variables following iterations
        self.output_dict = {}

        # Objectives for each stage
        self.objectives = ["max"]

        if n_art_vars:
            self.objectives.append("min")

        self.col_titles = []

        # Index of current pivot row and column
        self.row_idx = None
        self.col_idx = None

        # Does objective row only contain (non)-negative values?
        self.stop_iter = False

    def generate_col_titles(self):
        """Simplex tableau contains variable, slack, artificial, and RHS
        columns e.g. x_1, x_2, s_1, s_2, a_1, RHS
        """
        string_starts = ["x_", "s_", "a_"]
        constants = self.n_vars, self.n_slack, self.n_art_vars
        titles = []
        for i in range(3):
            for j in range(constants[i]):
                titles.append(string_starts[i] + str(j + 1))
        titles.append("RHS")
        self.col_titles = titles

    def find_pivot(self):
        """Finds the pivot row and column."""
        tableau = self.tableau
        objective = self.objectives[-1]

        # Find entries of highest magnitude in objective rows
        sign = (objective == "min") - (objective == "max")
        self.col_idx = np.argmax(sign * tableau[0, :-1])

        # Check if choice is valid, or if iteration must be stopped
        if sign * self.tableau[0, self.col_idx] <= 0:
            self.stop_iter = True
            return

        # Pivot row is chosen as having the lowest quotient when elements of
        # the pivot column divide the right-hand side

        # Slice excluding the objective rows
        s = slice(self.n_stages, self.n_rows)

        # RHS
        dividend = tableau[s, -1]

        # Elements of pivot column within slice
        divisor = tableau[s, self.col_idx]

        # Array filled with nans
        nans = np.full(self.n_rows - self.n_stages, np.nan)

        # If element in pivot column is greater than zero, return quotient
        # or nan otherwise
        quotients = np.divide(dividend, divisor, out=nans, where=divisor > 0)

        # Arg of minimum quotient excluding the nan values. `n_stages` is added
        # to compensate for earlier exclusion of objective columns
        self.row_idx = np.nanargmin(quotients) + self.n_stages

    def pivot(self):
        """Pivots on value on the intersection of pivot row and column."""

        # Avoid changes to original tableau
        piv_row = self.tableau[self.row_idx].copy()

        piv_val = piv_row[self.col_idx]

        # Entry becomes 1
        piv_row *= 1 / piv_val

        # Variable in pivot column becomes basic, ie the only non-zero entry
        for idx, coeff in enumerate(self.tableau[:, self.col_idx]):
            self.tableau[idx] += -coeff * piv_row
        self.tableau[self.row_idx] = piv_row

    def change_stage(self):
        """Exits first phase of the two-stage method by deleting artificial
        rows and columns, or completes the algorithm if exiting the standard
        case."""
        # Objective of original objective row remains
        self.objectives.pop()

        if not self.objectives:
            return

        # Slice containing ids for artificial columns
        s = slice(-self.n_art_vars - 1, -1)

        # Delete the artificial variable columns
        self.tableau = np.delete(self.tableau, s, axis=1)

        # Delete the objective row of the first stage
        self.tableau = np.delete(self.tableau, 0, axis=0)

        self.n_stages = 1
        self.n_rows -= 1
        self.n_art_vars = 0
        self.stop_iter = False

    def run_simp(self):
        """Recursively operate on tableau until objective function cannot be
        improved further"""
        # If optimal solution reached
        if not self.objectives:
            self.interpret_tableau()
            raise Exception

        self.find_pivot()
        if self.stop_iter:
            self.change_stage()
            self.run_simp()
        self.pivot()
        self.run_simp()

    def interpret_tableau(self):
        """Given the final tableau, add the corresponding values of the basic
        variables to the `output_dict`"""
        # P = RHS of final tableau
        self.output_dict["P"] = self.tableau[0, -1]

        n_current_cols = len(self.tableau[0])
        for i in range(n_current_cols):

            # Gives ids of nonzero entries in the ith column
            nonzero = np.nonzero(self.tableau[:, i])
            n_nonzero = len(nonzero[0])

            # First entry in the nonzero ids
            nonzero_rowidx = nonzero[0][0]
            nonzero_val = self.tableau[nonzero_rowidx, i]

            # If there is only one nonzero value in column, which is one
            if n_nonzero == nonzero_val == 1:
                rhs_val = self.tableau[nonzero_rowidx, -1]
                self.output_dict[self.col_titles[i]] = rhs_val

tableau = np.array([
    [2, 0, 0, 0, -1, -1, 0, 0, 20],
    [-2, -3, -1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 40],
    [2, 1, -1, 0, -1, 0, 1, 0, 10],
    [0, -1, 1, 0, 0, -1, 0, 1, 10]
    ], dtype=float)

n_vars = 3
n_art_vars = 2

def main():
    t = Tableau(tableau, n_vars, n_art_vars)
    t.generate_col_titles()
    try:
        t.run_simp()
    except Exception:
        # If optimal solution is reached
        for key, value in t.output_dict.items():
            print(key, ":", value)

if __name__ == "__main__":
    main()