# An OOP approach to representing and manipulating matrices

from __future__ import annotations


class Matrix:
    """
    Matrix object generated from a 2D array where each element is an array representing
    a row. Supports both integer and float values.
    """

    __hash__: None = None  # Fix PLW1641: Mark class as unhashable with type annotation

    def __init__(self, rows: list[list[float]]) -> None:
        """
        Initialize matrix from 2D list. Validates input structure and types.
        Raises TypeError for invalid input structure or element types.
        """
        error = TypeError(
            "Matrices must be formed from a list of zero or more lists containing at "
            "least one and the same number of values, each of which must be of type "
            "int or float."
        )

        # Validate matrix structure and content
        if rows:
            cols = len(rows[0])
            if cols == 0:
                raise error
            for row in rows:
                if len(row) != cols:
                    raise error
                for value in row:
                    if not isinstance(value, (int, float)):
                        raise error
            self.rows = rows
        else:
            self.rows = []

    # MATRIX INFORMATION METHODS
    def columns(self) -> list[list[float]]:
        """Return matrix columns as 2D list"""
        return [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]

    @property
    def num_rows(self) -> int:
        """Get number of rows in matrix"""
        return len(self.rows)

    @property
    def num_columns(self) -> int:
        """Get number of columns in matrix"""
        return len(self.rows[0])

    @property
    def order(self) -> tuple[int, int]:
        """Get matrix dimensions as (rows, columns) tuple"""
        return self.num_rows, self.num_columns

    @property
    def is_square(self) -> bool:
        """Check if matrix is square (rows == columns)"""
        return self.order[0] == self.order[1]

    def identity(self) -> Matrix:
        """Generate identity matrix of same dimensions"""
        values = [
            [
                0.0 if column_num != row_num else 1.0
                for column_num in range(self.num_rows)
            ]
            for row_num in range(self.num_rows)
        ]
        return Matrix(values)

    def determinant(self) -> float:
        """Calculate matrix determinant. Returns 0 for non-square matrices."""
        if not self.is_square:
            return 0.0
        if self.order == (0, 0):
            return 1.0
        if self.order == (1, 1):
            return float(self.rows[0][0])
        if self.order == (2, 2):
            return float(
                (self.rows[0][0] * self.rows[1][1])
                - (self.rows[0][1] * self.rows[1][0])
            )
        return sum(
            self.rows[0][column] * self.cofactors().rows[0][column]
            for column in range(self.num_columns)
        )

    def is_invertable(self) -> bool:
        """Check if matrix is invertible (non-zero determinant)"""
        return bool(self.determinant())

    def get_minor(self, row: int, column: int) -> float:
        """Calculate minor for specified element (determinant of submatrix)"""
        values = [
            [
                self.rows[other_row][other_column]
                for other_column in range(self.num_columns)
                if other_column != column
            ]
            for other_row in range(self.num_rows)
            if other_row != row
        ]
        return Matrix(values).determinant()

    def get_cofactor(self, row: int, column: int) -> float:
        """Calculate cofactor for specified element (signed minor)"""
        return self.get_minor(row, column) * (-1 if (row + column) % 2 else 1)

    def minors(self) -> Matrix:
        """Generate matrix of minors"""
        return Matrix(
            [
                [self.get_minor(row, column) for column in range(self.num_columns)]
                for row in range(self.num_rows)
            ]
        )

    def cofactors(self) -> Matrix:
        """Generate cofactor matrix"""
        return Matrix(
            [
                [self.get_cofactor(row, column) for column in range(self.num_columns)]
                for row in range(self.num_rows)
            ]
        )

    def adjugate(self) -> Matrix:
        """Generate adjugate matrix (transpose of cofactor matrix)"""
        return Matrix(
            [
                [
                    self.cofactors().rows[column][row]
                    for column in range(self.num_columns)
                ]
                for row in range(self.num_rows)
            ]
        )

    def inverse(self) -> Matrix:
        """Calculate matrix inverse. Raises TypeError for singular matrices."""
        det = self.determinant()
        if abs(det) < 1e-10:  # Floating point tolerance
            raise TypeError("Only matrices with a non-zero determinant have an inverse")
        return self.adjugate() * (1 / det)

    def __repr__(self) -> str:
        """Official string representation of matrix"""
        return str(self.rows)

    def __str__(self) -> str:
        """User-friendly string representation of matrix"""
        if not self.rows:
            return "[]"
        if self.num_rows == 1:
            return "[[" + ". ".join(str(val) for val in self.rows[0]) + "]]"
        return (
            "["
            + "\n ".join(
                "[" + ". ".join(str(val) for val in row) + ".]" for row in self.rows
            )
            + "]"
        )

    # MATRIX MANIPULATION METHODS
    def add_row(self, row: list[float], position: int | None = None) -> None:
        """Add row to matrix. Validates type and length."""
        if not isinstance(row, list):
            raise TypeError("Row must be a list")
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("Row elements must be int or float")
        if len(row) != self.num_columns:
            raise ValueError("Row length must match matrix columns")

        if position is None:
            self.rows.append(row)
        else:
            # Fix RUF005: Use iterable unpacking instead of concatenation
            self.rows = [*self.rows[:position], row, *self.rows[position:]]

    def add_column(self, column: list[float], position: int | None = None) -> None:
        """Add column to matrix. Validates type and length."""
        if not isinstance(column, list):
            raise TypeError("Column must be a list")
        for value in column:
            if not isinstance(value, (int, float)):
                raise TypeError("Column elements must be int or float")
        if len(column) != self.num_rows:
            raise ValueError("Column length must match matrix rows")

        if position is None:
            for i, value in enumerate(column):
                self.rows[i].append(value)
        else:
            # Fix RUF005: Use iterable unpacking instead of concatenation
            for i, value in enumerate(column):
                self.rows[i] = [
                    *self.rows[i][:position],
                    value,
                    *self.rows[i][position:],
                ]

    # MATRIX OPERATIONS
    def __eq__(self, other: object) -> bool:
        """Check matrix equality"""
        if not isinstance(other, Matrix):
            return NotImplemented
        return self.rows == other.rows

    def __ne__(self, other: object) -> bool:
        """Check matrix inequality"""
        return not self == other

    def __neg__(self) -> Matrix:
        """Negate matrix elements"""
        return self * -1.0

    def __add__(self, other: Matrix) -> Matrix:
        """Matrix addition. Requires same dimensions."""
        if self.order != other.order:
            raise ValueError("Addition requires matrices of same dimensions")
        return Matrix(
            [
                [self.rows[i][j] + other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __sub__(self, other: Matrix) -> Matrix:
        """Matrix subtraction. Requires same dimensions."""
        if self.order != other.order:
            raise ValueError("Subtraction requires matrices of same dimensions")
        return Matrix(
            [
                [self.rows[i][j] - other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __mul__(self, other: Matrix | float) -> Matrix:
        """Matrix multiplication (scalar or matrix)"""
        if isinstance(other, (int, float)):
            # Preserve float precision by removing int conversion
            return Matrix([[element * other for element in row] for row in self.rows])
        elif isinstance(other, Matrix):
            if self.num_columns != other.num_rows:
                raise ValueError(
                    "Matrix multiplication requires columns of first matrix "
                    "to match rows of second matrix"
                )
            return Matrix(
                [
                    [Matrix.dot_product(row, col) for col in other.columns()]
                    for row in self.rows
                ]
            )
        raise TypeError("Matrix can only be multiplied by scalar or another matrix")

    def __pow__(self, exponent: int) -> Matrix:
        """Matrix exponentiation. Requires square matrix."""
        if not isinstance(exponent, int):
            raise TypeError("Exponent must be integer")
        if not self.is_square:
            raise ValueError("Only square matrices can be raised to a power")
        if exponent == 0:
            return self.identity()
        if exponent < 0:
            if self.is_invertable():
                return self.inverse() ** (-exponent)
            raise ValueError(
                "Only invertible matrices can be raised to negative powers"
            )
        result = self
        for _ in range(exponent - 1):
            result *= self
        return result

    @classmethod
    def dot_product(cls, row: list[float], column: list[float]) -> float:
        """Calculate dot product of two vectors"""
        return sum(row[i] * column[i] for i in range(len(row)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
