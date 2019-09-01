# An OOP aproach to representing and manipulating matrices

class Matrix:
    '''
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
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    >>> print(matrix.rows)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> print(matrix.columns)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    
    Order is returned as a tuple
    >>> matrix.order
    (3, 3)
    
    Scalar multiplication, addition, subtraction, and multiplication are available
    >>> matrix2 = matrix * 3
    >>> print(matrix2)
    [3, 6, 9]
    [12, 15, 18]
    [21, 24, 27]
    >>> print(matrix + matrix2)
    [4, 8, 12]
    [16, 20, 24]
    [28, 32, 36]
    >>> print(matrix - matrix2)
    [-2, -4, -6]
    [-8, -10, -12]
    [-14, -16, -18]
    >>> print(matrix * matrix2)
    [90, 108, 126]
    [198, 243, 288]
    [306, 378, 450]

    Matrices can also be modified
    >>> matrix.add_row([10, 11, 12])
    >>> print(matrix)
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    [10, 11, 12]
    >>> matrix2.add_column([8, 16, 32])
    >>> print(matrix2)
    [3, 6, 9, 8]
    [12, 15, 18, 16]
    [21, 24, 27, 32]
    >>> print(matrix *  matrix2)
    [90, 108, 126, 136]
    [198, 243, 288, 304]
    [306, 378, 450, 472]
    [414, 513, 612, 640]

    '''
    def __init__(self, rows):
        error = TypeError('Matrices must be formed from a list of zero or more lists containing at least one and the same number of values, \
                each of which must be of type int or float')
        if len(rows) != 0:
            cols = len(rows[0])
            if cols == 0:
                raise error
            for row in rows:
                if not len(row) == cols:
                    raise error
                for value in row:
                    if not isinstance(value, (int, float)):
                        raise error
            self.rows = rows
        else:
            self.rows = []
    
    # MATRIX INFORMATION
    @property
    def columns(self):
        return [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]
    @property
    def num_rows(self):
        return len(self.rows)
    @property
    def num_columns(self):
        return len(self.columns)
    @property
    def order(self):
        return (self.num_rows, self.num_columns)
    def __repr__(self):
        return str(self.rows)
    def __str__(self):
        if self.num_rows == 0:
            return str(self.rows)
        if self.num_rows == 1:
            return str(self.rows[0])
        return '\n'.join([str(row) for row in self.rows])

    # MATRIX MANIPULATION
    def add_row(self, row, position = None):
        type_error = TypeError('Row must be a list containing all ints and/or floats')
        if not isinstance(row, list):
            raise type_error
        for value in row:
            if not isinstance(value, (int, float)):
                raise type_error
        if len(row) != self.num_columns:
            raise ValueError('Row must be equal in length to the other rows in the matrix')
        if position is None:
            self.rows.append(row)
        else:
            self.rows = self.rows[0:position] + [row] + self.rows[position:]
    def add_column(self, column, position = None):
        type_error = TypeError('Column must be a list containing all ints and/or floats')
        if not isinstance(column, list):
            raise type_error
        for value in column:
            if not isinstance(value, (int, float)):
                raise type_error
        if len(column) != self.num_rows:
            raise ValueError('Column must be equal in length to the other columns in the matrix')
        if position is None:
            self.rows = [self.rows[i] + [column[i]] for i in range(self.num_rows)]
        else:
            self.rows = [self.rows[i][0:position] + [column[i]] + self.rows[i][position:] for i in range(self.num_rows)]

    # MATRIX OPERATIONS
    def __add__(self, other):
        if self.order != other.order:
            raise ValueError('Addition requires matrices of the same order')
        return Matrix([[self.rows[i][j] + other.rows[i][j] for j in range(self.num_columns)] for i in range(self.num_rows)])
    def __sub__(self, other):
        if self.order != other.order:
            raise ValueError('Subtraction requires matrices of the same order')
        return Matrix([[self.rows[i][j] - other.rows[i][j] for j in range(self.num_columns)] for i in range(self.num_rows)])
    def __mul__(self, other):
        if not isinstance(other, (int, float, Matrix)):
            raise TypeError('A matrix can only be multiplied by an int, float, or another matrix')
        if type(other) in (int, float):
            return Matrix([[element * other for element in row] for row in self.rows])
        if type(other) is Matrix:
            if self.num_columns != other.num_rows:
                raise ValueError('The number of columns in the first matrix must be equal to the number of rows in the second')
            return Matrix([[Matrix.dot_product(row, column) for column in other.columns] for row in self.rows])

    @classmethod
    def dot_product(cls, row, column):
        return sum([row[i] * column[i] for i in range(len(row))])


if __name__ == '__main__':
    import doctest
    test = doctest.testmod()
    print(test)