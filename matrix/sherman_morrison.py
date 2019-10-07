class Matrix:
    """
    <class Matrix>
    Matrix structure.
    """

    def __init__(self, row: int, column: int, default_value: float = 0):
        """
        <method Matrix.__init__>
        Initialize matrix with given size and default value.

        Example:
        >>> a = Matrix(2, 3, 1)
        >>> a 
        Matrix consist of 2 rows and 3 columns
        [1, 1, 1]
        [1, 1, 1]
        """

        self.row, self.column = row, column
        self.array = [[default_value for c in range(column)] for r in range(row)]

    def __str__(self):
        """
        <method Matrix.__str__>
        Return string representation of this matrix.
        """

        # Prefix
        s = "Matrix consist of %d rows and %d columns\n" % (self.row, self.column)

        # Make string identifier
        max_element_length = 0
        for row_vector in self.array:
            for obj in row_vector:
                max_element_length = max(max_element_length, len(str(obj)))
        string_format_identifier = "%%%ds" % (max_element_length,)

        # Make string and return
        def single_line(row_vector):
            nonlocal string_format_identifier
            line = "["
            line += ", ".join(string_format_identifier % (obj,) for obj in row_vector)
            line += "]"
            return line

        s += "\n".join(single_line(row_vector) for row_vector in self.array)
        return s

    def __repr__(self):
        return str(self)

    def validateIndices(self, loc: tuple):
        """
        <method Matrix.validateIndices>
        Check if given indices are valid to pick element from matrix.

        Example:
        >>> a = Matrix(2, 6, 0)
        >>> a.validateIndices((2, 7))
        False
        >>> a.validateIndices((0, 0))
        True
        """
        if not (isinstance(loc, (list, tuple)) and len(loc) == 2):
            return False
        elif not (0 <= loc[0] < self.row and 0 <= loc[1] < self.column):
            return False
        else:
            return True

    def __getitem__(self, loc: tuple):
        """
        <method Matrix.__getitem__>
        Return array[row][column] where loc = (row, column).

        Example:
        >>> a = Matrix(3, 2, 7)
        >>> a[1, 0]
        7
        """
        assert self.validateIndices(loc)
        return self.array[loc[0]][loc[1]]

    def __setitem__(self, loc: tuple, value: float):
        """
        <method Matrix.__setitem__>
        Set array[row][column] = value where loc = (row, column).

        Example:
        >>> a = Matrix(2, 3, 1)
        >>> a[1, 2] = 51
        >>> a
        Matrix consist of 2 rows and 3 columns
        [ 1,  1,  1]
        [ 1,  1, 51]
        """
        assert self.validateIndices(loc)
        self.array[loc[0]][loc[1]] = value

    def __add__(self, another):
        """
        <method Matrix.__add__>
        Return self + another.

        Example:
        >>> a = Matrix(2, 1, -4)
        >>> b = Matrix(2, 1, 3)
        >>> a+b
        Matrix consist of 2 rows and 1 columns
        [-1]
        [-1]
        """

        # Validation
        assert isinstance(another, Matrix)
        assert self.row == another.row and self.column == another.column

        # Add
        result = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                result[r, c] = self[r, c] + another[r, c]
        return result

    def __neg__(self):
        """
        <method Matrix.__neg__>
        Return -self.

        Example:
        >>> a = Matrix(2, 2, 3)
        >>> a[0, 1] = a[1, 0] = -2
        >>> -a
        Matrix consist of 2 rows and 2 columns
        [-3,  2]
        [ 2, -3]
        """

        result = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                result[r, c] = -self[r, c]
        return result

    def __sub__(self, another):
        return self + (-another)

    def __mul__(self, another):
        """
        <method Matrix.__mul__>
        Return self * another.

        Example:
        >>> a = Matrix(2, 3, 1)
        >>> a[0,2] = a[1,2] = 3
        >>> a * -2
        Matrix consist of 2 rows and 3 columns
        [-2, -2, -6]
        [-2, -2, -6]
        """

        if isinstance(another, (int, float)):  # Scalar multiplication
            result = Matrix(self.row, self.column)
            for r in range(self.row):
                for c in range(self.column):
                    result[r, c] = self[r, c] * another
            return result
        elif isinstance(another, Matrix):  # Matrix multiplication
            assert self.column == another.row
            result = Matrix(self.row, another.column)
            for r in range(self.row):
                for c in range(another.column):
                    for i in range(self.column):
                        result[r, c] += self[r, i] * another[i, c]
            return result
        else:
            raise TypeError(
                "Unsupported type given for another (%s)" % (type(another),)
            )

    def transpose(self):
        """
        <method Matrix.transpose>
        Return self^T.

        Example:
        >>> a = Matrix(2, 3)
        >>> for r in range(2):       
        ...     for c in range(3):
        ...             a[r,c] = r*c
        ... 
        >>> a.transpose()
        Matrix consist of 3 rows and 2 columns
        [0, 0]
        [0, 1]
        [0, 2]
        """

        result = Matrix(self.column, self.row)
        for r in range(self.row):
            for c in range(self.column):
                result[c, r] = self[r, c]
        return result

    def ShermanMorrison(self, u, v):
        """
        <method Matrix.ShermanMorrison>
        Apply Sherman-Morrison formula in O(n^2).
        To learn this formula, please look this: https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula
        This method returns (A + uv^T)^(-1) where A^(-1) is self. Returns None if it's impossible to calculate.
        Warning: This method doesn't check if self is invertible. 
            Make sure self is invertible before execute this method.

        Example:
        >>> ainv = Matrix(3, 3, 0)
        >>> for i in range(3): ainv[i,i] = 1
        ... 
        >>> u = Matrix(3, 1, 0) 
        >>> u[0,0], u[1,0], u[2,0] = 1, 2, -3
        >>> v = Matrix(3, 1, 0)
        >>> v[0,0], v[1,0], v[2,0] = 4, -2, 5
        >>> ainv.ShermanMorrison(u, v)
        Matrix consist of 3 rows and 3 columns
        [  1.2857142857142856, -0.14285714285714285,   0.3571428571428571]
        [  0.5714285714285714,   0.7142857142857143,   0.7142857142857142]
        [ -0.8571428571428571,  0.42857142857142855,  -0.0714285714285714]
        """

        # Size validation
        assert isinstance(u, Matrix) and isinstance(v, Matrix)
        assert self.row == self.column == u.row == v.row  # u, v should be column vector
        assert u.column == v.column == 1  # u, v should be column vector

        # Calculate
        vT = v.transpose()
        numerator_factor = (vT * self * u)[0, 0] + 1
        if numerator_factor == 0:
            return None  # It's not invertable
        return self - ((self * u) * (vT * self) * (1.0 / numerator_factor))


# Testing
if __name__ == "__main__":

    def test1():
        # a^(-1)
        ainv = Matrix(3, 3, 0)
        for i in range(3):
            ainv[i, i] = 1
        print("a^(-1) is %s" % (ainv,))
        # u, v
        u = Matrix(3, 1, 0)
        u[0, 0], u[1, 0], u[2, 0] = 1, 2, -3
        v = Matrix(3, 1, 0)
        v[0, 0], v[1, 0], v[2, 0] = 4, -2, 5
        print("u is %s" % (u,))
        print("v is %s" % (v,))
        print("uv^T is %s" % (u * v.transpose()))
        # Sherman Morrison
        print("(a + uv^T)^(-1) is %s" % (ainv.ShermanMorrison(u, v),))

    def test2():
        import doctest

        doctest.testmod()

    test2()
