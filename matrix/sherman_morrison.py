class Matrix:

    def __init__(self, row: int, column: int, default_value: float = 0):
        """
        <method Matrix.__init__>
        Initialize matrix with given size and default value.
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
        for row_vector in self.array:
            s += "["
            s += ", ".join(string_format_identifier % (obj,) for obj in row_vector)
            s += "]\n"
        return s

    def __getitem__(self, loc: tuple):
        """
        <method Matrix.__getitem__>
        Return array[row][column] where loc = (row, column).
        """
        assert(isinstance(loc, (list, tuple)) and len(loc) == 2)
        assert(0 <= loc[0] < self.row and 0 <= loc[1] < self.column)
        return self.array[loc[0]][loc[1]]

    def __setitem__(self, loc: tuple, value: float):
        """
        <method Matrix.__setitem__>
        Set array[row][column] = value where loc = (row, column).
        """
        assert(isinstance(loc, (list, tuple)) and len(loc) == 2)
        assert(0 <= loc[0] < self.row and 0 <= loc[1] < self.column)
        self.array[loc[0]][loc[1]] = value

    def __add__(self, another):
        """
        <method Matrix.__add__>
        Return self + another.
        """

        # Validation
        assert(self.row == another.row and self.column == another.column)
        assert(isinstance(another, Matrix))

        # Add
        result = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                result[r,c] = self[r,c] + another[r,c]
        return result

    def __neg__(self):
        """
        <method Matrix.__neg__>
        Return -self.
        """

        result = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                result[r,c] = -self[r,c]
        return result

    def __sub__(self, another): return self + (-another)

    def __mul__(self, another):
        """
        <method Matrix.__mul__>
        Return self * another.
        """

        if isinstance(another, (int, float)): # Scalar multiplication
            result = Matrix(self.row, self.column)
            for r in range(self.row):
                for c in range(self.column):
                    result[r,c] = self[r,c] * another
            return result
        elif isinstance(another, Matrix): # Matrix multiplication
            assert(self.column == another.row)
            result = Matrix(self.row, another.column)
            for r in range(self.row):
                for c in range(another.column):
                    for i in range(self.column):
                        result[r,c] += self[r,i] * another[i,c]
            return result
        else: raise TypeError("Unsupported type given for another (%s)" % (type(another),))

    def transpose(self):
        """
        <method Matrix.transpose>
        Return self^T.
        """

        result = Matrix(self.column, self.row)
        for r in range(self.row):
            for c in range(self.column):
                result[c,r] = self[r,c]
        return result

    def ShermanMorrison(self, u, v):
        """
        <method Matrix.ShermanMorrison>
        Apply Sherman-Morrison formula in O(n^2).
        To learn this formula, please look this: https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula
        This method returns (A + uv^T)^(-1) where A^(-1) is self. Returns None if it's impossible to calculate.
        Warning: This method doesn't check if self is invertible. 
            Make sure self is invertible before execute this method.
        """

        # Size validation
        assert(isinstance(u, Matrix) and isinstance(v, Matrix))
        assert(self.row == self.column == u.row == v.row) # u, v should be column vector
        assert(u.column == v.column == 1) # u, v should be column vector

        # Calculate
        vT = v.transpose()
        numerator_factor = (vT * self * u)[0, 0] + 1
        if numerator_factor == 0: return None # It's not invertable
        return self - ((self * u) * (vT * self) * (1.0 / numerator_factor))

# Testing
if __name__ == "__main__":

    # a^(-1)
    ainv = Matrix(3, 3, 0)
    for i in range(3): ainv[i,i] = 1
    print("a^(-1) is %s" % (ainv,))
    
    # u, v
    u = Matrix(3, 1, 0)
    u[0,0], u[1,0], u[2,0] = 1, 2, -3
    v = Matrix(3, 1, 0)
    v[0,0], v[1,0], v[2,0] = 4, -2, 5
    print("u is %s" % (u,))
    print("v is %s" % (v,))
    print("uv^T is %s" % (u * v.transpose()))

    # Sherman Morrison
    print("(a + uv^T)^(-1) is %s" % (ainv.ShermanMorrison(u, v),))
