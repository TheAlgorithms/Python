# An OOP approach to representing and manipulating matrices


class Matrix:
    """
    Matrix object generated from a 2D array where each element is an array representing a row.
    Rows can contain type int or float.
    Common operations and information available.
    >>> rows = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ]
    >>> matrix = Matrix(rows)
    >>> print(matrix)
    [[1. 2. 3.]
     [4. 5. 6.]
     [7. 8. 9.]]
    
    Matrix rows and columns are available as 2D arrays
    >>> print(matrix.rows)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> print(matrix.columns())
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    
    Order is returned as a tuple
    >>> matrix.order
    (3, 3)

    Squareness and invertability are represented as bool
    >>> matrix.is_square
    True
    >>> matrix.is_invertable()
    False

    Identity, Minors, Cofactors and Adjugate are returned as Matrices.  Inverse can be a Matrix or Nonetype
    >>> print(matrix.identity())
    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    >>> print(matrix.minors())
    [[-3. -6. -3.]
     [-6. -12. -6.]
     [-3. -6. -3.]]
    >>> print(matrix.cofactors())
    [[-3. 6. -3.]
     [6. -12. 6.]
     [-3. 6. -3.]]
    >>> print(matrix.adjugate()) # won't be apparent due to the nature of the cofactor matrix
    [[-3. 6. -3.]
     [6. -12. 6.]
     [-3. 6. -3.]]
    >>> print(matrix.inverse())
    None

    Determinant is an int, float, or Nonetype
    >>> matrix.determinant()
    0

    Negation, scalar multiplication, addition, subtraction, multiplication and exponentiation are available and all return a Matrix
    >>> print(-matrix)
    [[-1. -2. -3.]
     [-4. -5. -6.]
     [-7. -8. -9.]]
    >>> matrix2 = matrix * 3
    >>> print(matrix2)
    [[3. 6. 9.]
     [12. 15. 18.]
     [21. 24. 27.]]
    >>> print(matrix + matrix2)
    [[4. 8. 12.]
     [16. 20. 24.]
     [28. 32. 36.]]
    >>> print(matrix - matrix2)
    [[-2. -4. -6.]
     [-8. -10. -12.]
     [-14. -16. -18.]]
    >>> print(matrix ** 3)
    [[468. 576. 684.]
     [1062. 1305. 1548.]
     [1656. 2034. 2412.]]

    Matrices can also be modified
    >>> matrix.add_row([10, 11, 12])
    >>> print(matrix)
    [[1. 2. 3.]
     [4. 5. 6.]
     [7. 8. 9.]
     [10. 11. 12.]]
    >>> matrix2.add_column([8, 16, 32])
    >>> print(matrix2)
    [[3. 6. 9. 8.]
     [12. 15. 18. 16.]
     [21. 24. 27. 32.]]
    >>> print(matrix *  matrix2)
    [[90. 108. 126. 136.]
     [198. 243. 288. 304.]
     [306. 378. 450. 472.]
     [414. 513. 612. 640.]]

    """

    def __init__(self, rows):
        error = TypeError(
            "Matrices must be formed from a list of zero or more lists containing at least "
            "one and the same number of values, each of which must be of type int or float."
        )
        if len(rows) != 0:
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

    # MATRIX INFORMATION
    def columns(self):
        return [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]

    @property
    def num_rows(self):
        return len(self.rows)

    @property
    def num_columns(self):
        return len(self.rows[0])

    @property
    def order(self):
        return (self.num_rows, self.num_columns)

    @property
    def is_square(self):
        return self.order[0] == self.order[1]

    def identity(self):
        values = [
            [0 if column_num != row_num else 1 for column_num in range(self.num_rows)]
            for row_num in range(self.num_rows)
        ]
        return Matrix(values)

    def determinant(self):
        if not self.is_square:
            return None
        if self.order == (0, 0):
            return 1
        if self.order == (1, 1):
            return self.rows[0][0]
        if self.order == (2, 2):
            return (self.rows[0][0] * self.rows[1][1]) - (
                self.rows[0][1] * self.rows[1][0]
            )
        else:
            return sum(
                [
                    self.rows[0][column] * self.cofactors().rows[0][column]
                    for column in range(self.num_columns)
                ]
            )

    def is_invertable(self):
        return bool(self.determinant())

    def get_minor(self, row, column):
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

    def get_cofactor(self, row, column):
        if (row + column) % 2 == 0:
            return self.get_minor(row, column)
        return -1 * self.get_minor(row, column)

    def minors(self):
        return Matrix(
            [
                [self.get_minor(row, column) for column in range(self.num_columns)]
                for row in range(self.num_rows)
            ]
        )

    def cofactors(self):
        return Matrix(
            [
                [
                    self.minors().rows[row][column]
                    if (row + column) % 2 == 0
                    else self.minors().rows[row][column] * -1
                    for column in range(self.minors().num_columns)
                ]
                for row in range(self.minors().num_rows)
            ]
        )

    def adjugate(self):
        values = [
            [self.cofactors().rows[column][row] for column in range(self.num_columns)]
            for row in range(self.num_rows)
        ]
        return Matrix(values)

    def inverse(self):
        determinant = self.determinant()
        return None if not determinant else self.adjugate() * (1 / determinant)

    def __repr__(self):
        return str(self.rows)

    def __str__(self):
        if self.num_rows == 0:
            return "[]"
        if self.num_rows == 1:
            return "[[" + ". ".join(self.rows[0]) + "]]"
        return (
            "["
            + "\n ".join(
                [
                    "[" + ". ".join([str(value) for value in row]) + ".]"
                    for row in self.rows
                ]
            )
            + "]"
        )

    # MATRIX MANIPULATION
    def add_row(self, row, position=None):
        type_error = TypeError("Row must be a list containing all ints and/or floats")
        if not isinstance(row, list):
            raise type_error
        for value in row:
            if not isinstance(value, (int, float)):
                raise type_error
        if len(row) != self.num_columns:
            raise ValueError(
                "Row must be equal in length to the other rows in the matrix"
            )
        if position is None:
            self.rows.append(row)
        else:
            self.rows = self.rows[0:position] + [row] + self.rows[position:]

    def add_column(self, column, position=None):
        type_error = TypeError(
            "Column must be a list containing all ints and/or floats"
        )
        if not isinstance(column, list):
            raise type_error
        for value in column:
            if not isinstance(value, (int, float)):
                raise type_error
        if len(column) != self.num_rows:
            raise ValueError(
                "Column must be equal in length to the other columns in the matrix"
            )
        if position is None:
            self.rows = [self.rows[i] + [column[i]] for i in range(self.num_rows)]
        else:
            self.rows = [
                self.rows[i][0:position] + [column[i]] + self.rows[i][position:]
                for i in range(self.num_rows)
            ]

    # MATRIX OPERATIONS
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("A Matrix can only be compared with another Matrix")
        return self.rows == other.rows

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        return self * -1

    def __add__(self, other):
        if self.order != other.order:
            raise ValueError("Addition requires matrices of the same order")
        return Matrix(
            [
                [self.rows[i][j] + other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __sub__(self, other):
        if self.order != other.order:
            raise ValueError("Subtraction requires matrices of the same order")
        return Matrix(
            [
                [self.rows[i][j] - other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[element * other for element in row] for row in self.rows])
        elif isinstance(other, Matrix):
            if self.num_columns != other.num_rows:
                raise ValueError(
                    "The number of columns in the first matrix must "
                    "be equal to the number of rows in the second"
                )
            return Matrix(
                [
                    [Matrix.dot_product(row, column) for column in other.columns()]
                    for row in self.rows
                ]
            )
        else:
            raise TypeError(
                "A Matrix can only be multiplied by an int, float, or another matrix"
            )

    def __pow__(self, other):
        if not isinstance(other, int):
            raise TypeError("A Matrix can only be raised to the power of an int")
        if not self.is_square:
            raise ValueError("Only square matrices can be raised to a power")
        if other == 0:
            return self.identity()
        if other < 0:
            if self.is_invertable:
                return self.inverse() ** (-other)
            raise ValueError(
                "Only invertable matrices can be raised to a negative power"
            )
        result = self
        for i in range(other - 1):
            result *= self
        return result

    @classmethod
    def dot_product(cls, row, column):
        return sum([row[i] * column[i] for i in range(len(row))])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
