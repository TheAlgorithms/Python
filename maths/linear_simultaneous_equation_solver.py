"""
https://en.wikipedia.org/wiki/Augmented_matrix

This algorithm solves simultaneous linear equations of the form
γa + γb + γc + γd + ... = γ as [γ, γ, γ, γ, ..., γ]
Where γ are individual coefficients, the no. of equations = no. of coefficients - 1

Note in order to work there must exist 1 equation where all instances of γ != 0
"""


class EquationSolver:
    def __init__(self, data: list[list[int | float]]) -> None:
        if len(data) == 0:
            raise IndexError("EquationSolver() requires n lists of length n+1")
        self.size = len(data)
        _length = self.size + 1
        if any(len(item) != _length for item in data):
            raise IndexError("EquationSolver() requires n lists of length n+1")
        for row in data:
            if any(not isinstance(column, (int, float)) for column in row):
                raise ValueError("EquationSolver() requires lists of integers")
        self.data = data

    def __repr__(self) -> str:
        string_builder = "["
        for i in range(self.size):
            string_builder += "["
            for j in range(self.size):
                if j == self.size - 1:
                    string_builder += f"{self.data[i][j]: >4}"
                    continue
                string_builder += f"{str(self.data[i][j]) + ',': >5}"
            string_builder += f"{'|': ^5}{self.data[i][-1]:<2}]\n "
        string_builder = string_builder[:-2] + "]"
        return string_builder

    def solve(self) -> list[int | float]:
        useable_form = self.make_useable_form()
        # Generate a simplified upper triangular matrix
        simplified = self.simplify(useable_form)
        # Reverse the matrix
        simplified = simplified[::-1]
        solutions = []
        for row in simplified:
            current_solution = row[-1]
            if not solutions:
                if row[-2] == 0:
                    solutions.append(0)
                    continue
                solutions.append(current_solution / row[-2])
                continue
            temp_row = row.copy()[: len(row) - 1 :]
            while temp_row[0] == 0:
                temp_row.pop(0)
            if len(temp_row) == 0:
                solutions.append(0)
                continue
            temp_row = temp_row[1::]
            temp_row = temp_row[::-1]
            for column_index, column in enumerate(temp_row):
                current_solution -= column * solutions[column_index]
            solutions.append(current_solution)
        final = []
        for item in solutions:
            final.append(round(item, 5))
        return final[::-1]

    def make_useable_form(self) -> list[list[int]]:
        data_set = self.data.copy()
        if any(0 in row for row in data_set):
            temp_data = data_set.copy()
            full_row = []
            for row_index, row in enumerate(temp_data):
                if 0 not in row:
                    full_row = data_set.pop(row_index)
                    break
            if not full_row:
                raise ValueError("EquationSolver() requires at least 1 full equation")
            data_set.insert(0, full_row)
        return data_set

    def simplify(self, current_set: list[list[int | float]]) -> list[list[int | float]]:
        # Divide each row by magnitude of first term --> creates 'unit' matrix
        duplicate_set = current_set.copy()
        for row_index, row in enumerate(duplicate_set):
            magnitude = row[0]
            for column_index, column in enumerate(row):
                if magnitude == 0:
                    current_set[row_index][column_index] = column
                    continue
                current_set[row_index][column_index] = column / magnitude
        # Subtract to cancel term
        first_row = current_set[0]
        final_set = [first_row]
        current_set = current_set[1::]
        for row in current_set:
            temp_row = []
            # If first term is 0, it is already in form we want, so we preserve it
            if row[0] == 0:
                final_set.append(row)
                continue
            for column_index in range(len(row)):
                temp_row.append(first_row[column_index] - row[column_index])
            final_set.append(temp_row)
        # Create next recursion iteration set
        if len(final_set[0]) != 3:
            current_first_row = final_set[0]
            current_first_column = []
            next_iteration = []
            for row in final_set[1::]:
                current_first_column.append(row[0])
                next_iteration.append(row[1::])
            resultant = self.simplify(next_iteration)
            for i in range(len(resultant)):
                resultant[i].insert(0, current_first_column[i])
            resultant.insert(0, current_first_row)
            final_set = resultant
        return final_set


def solve_simultaneous(equations: list[list[int | float]]) -> list[int | float]:
    """
    >>> solve_simultaneous([[1, 2, 3],[4, 5, 6]])
    [-1.0, 2.0]
    >>> solve_simultaneous([[0, -3, 1, 7],[3, 2, -1, 11],[5, 1, -2, 12]])
    [6.4, 1.2, 10.6]
    >>> solve_simultaneous([])
    Traceback (most recent call last):
        ...
    IndexError: EquationSolver() requires n lists of length n+1
    >>> solve_simultaneous([[1, 2, 3],[1, 2]])
    Traceback (most recent call last):
        ...
    IndexError: EquationSolver() requires n lists of length n+1
    >>> solve_simultaneous([[1, 2, 3],["a", 7, 8]])
    Traceback (most recent call last):
        ...
    ValueError: EquationSolver() requires lists of integers
    >>> solve_simultaneous([[0, 2, 3],[4, 0, 6]])
    Traceback (most recent call last):
        ...
    ValueError: EquationSolver() requires at least 1 full equation
    """
    aug = EquationSolver(equations)
    return aug.solve()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    eq = [
        [2, 1, 1, 1, 1, 4],
        [1, 2, 1, 1, 1, 5],
        [1, 1, 2, 1, 1, 6],
        [1, 1, 1, 2, 1, 7],
        [1, 1, 1, 1, 2, 8],
    ]
    print(solve_simultaneous(eq))
