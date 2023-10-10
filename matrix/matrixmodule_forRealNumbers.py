from tabulate import tabulate


class Matrix:
    """
    Create Matrix and use methods for Matrix Algebra.
    Determinant and Diagonal Function is Global to the Matrix Class.
    """

    def __init__(self, r, c):
        self.matrix = []
        self.rows = r
        self.columns = c
        for i in range(r):
            self.matrix.append([0]*c)

    def list(self):
        '''
        Returns -> 2-D List.
        '''
        return self.matrix

    def inputAdd(self):
        """
        Enter Data to Matrix using User-Inout, Row-wise.
        """
        temp = []
        for i in range(self.rows):
            for j in range(self.columns):
                temp.append(
                    int(input("Enter A[{i},{j}] - ".format(i=i + 1, j=j + 1))))
            self.matrix[i] = temp
            temp = []

    def listTomatrix(self, lst: list):
        """
        Converts List to Matrix (Row-wise) Ex- [(0,0),(0,1),(1,0),(1,1)].
        """
        if lst.__class__ == list or lst.__class__ == tuple:
            if len(lst) == self.rows*self.columns:
                temp = []
                k = 0
                for i in range(self.rows):
                    for j in range(self.columns):
                        temp.append(lst[k])
                        k += 1
                    self.matrix[i] = temp
                    temp = []
            else:
                raise Exception(
                    "Length of List must be equal to matrix( R * C ).")
        else:
            raise TypeError("List/Tuple is required to generate the Matrix.")

    def printMatrix(self):
        """
        Prints Matrix using Tabulate Module.
        """
        print(tabulate(self.matrix))

    def transpose(self):
        """
        Returns Transpose of the Matrix.
        """
        matrix2 = Matrix(self.columns, self.rows)
        temp = []
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                temp.append(self.matrix[j][i])
            matrix2.matrix[i] = temp
            temp = []
        return matrix2

    def sizeMatrix(self):
        """
        Returns the Size of the Matrix (Tuple) -> (rows,cols)
        """
        if self.matrix[0].__class__ == int or self.matrix[0].__class__ == float:
            return (None, None)
        return (len(self.matrix), len(self.matrix[0]))

    def matrixMultiplicationConstant(self, int1: int):
        """
        Parameter - Integer
        Return - Matrix1 X Integer
        """
        if int1.__class__ == int or int1.__class__ == float:
            sm1 = self.sizeMatrix()
            for i in range(sm1[0]):
                for j in range(sm1[1]):
                    if self.matrix[i][j] != 0:
                        self.matrix[i][j] *= int1
        else:
            raise Exception("Constant must be int/float.")

    def adj(self):
        """
        Returns the Adjoint Matrix of the Object.
        """
        if self.rows==self.columns==1:
            tmp = Matrix(1,1)
            tmp.listTomatrix([1])
            return tmp
        l = Matrix(self.rows, self.columns)
        if self.rows == self.columns == 2:
            l.matrix = [[self.matrix[1][1], -self.matrix[0][1]],
                [-self.matrix[1][0], self.matrix[0][0]]]
            return l
        z = []
        for i in range(len(self.matrix)):
            temp = []
            for j in range(len(self.matrix[i])):
                temp2 = []
                for k in range(len(self.matrix)):
                    temp3 = []
                    for m in range(len(self.matrix[k])):
                        if k != i and j != m:
                            temp3.append(self.matrix[k][m])
                    if temp3 != []:
                        temp2.append(temp3)
                if (i+j) % 2 == 0:
                    temp.append(determinant(temp2))
                else:
                    temp.append(-1*determinant(temp2))
            z.append(temp)
        l.matrix = z
        return l.transpose()

    def inverse(self):
        """
        Returns Inverse Matrix of the Object.
        """
        a = determinant(self)
        m2 = Matrix(self.rows, self.columns)
        if a != 0:
            m2.matrix = self.matrix
            m2 = m2.adj()
            m2.matrixMultiplicationConstant(a**-1)
            return m2
        else:
            raise ZeroDivisionError("Determinant is 0, Inverse is Undefined.")

    def mean(self):
        """
        Returns Mean of the Matrix.
        """
        m = 0
        for i in range(self.rows):
            for j in range(self.columns):
                m += self.matrix[i][j]
        return float(m/(self.rows*self.columns))

    def rowMeans(self):
        """
        Returns Mean of Rows of the Matrix.
        """
        m2 = Matrix(self.rows, 1)
        for i in range(self.rows):
            temp = 0
            for j in range(self.columns):
                temp += self.matrix[i][j]
            temp = temp/self.columns
            m2.matrix[i][0] = temp
        return m2

    def colMeans(self):
        """
        Returns Mean of the Columns of the Matrix.
        """
        m2 = Matrix(1, self.columns)
        for i in range(self.columns):
            temp = 0
            for j in range(self.rows):
                temp += self.matrix[j][i]
            temp = temp/self.rows
            m2.matrix[0][i] = temp
        return m2

    def rowSum(self):
        """
        Returns Sum of the Rows of the Matrix.
        """
        l = Matrix(1, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                l.matrix[0][j] += self.matrix[i][j]
        return l

    def colSum(self):
        """
        Returns Sum of the Columns of the Matrix.
        """
        l = Matrix(self.rows, 1)
        for i in range(self.columns):
            for j in range(self.rows):
                l.matrix[j][0] += self.matrix[j][i]
        return l

    def sum(self):
        """
        Returns Sum of all Elements of the Matrix.
        """
        a = self.colSum().matrix
        s = 0
        for i in range(len(a)):
            s += a[i][0]
        return float(s)

    def orthogonalCheck(self):
        """
        Checks if the Matrix is Orthogonal (1) or not (0).
        """
        q = self.sizeMatrix()
        if q[0] == q[1]:
            if self.transpose().matrix == self.inverse().matrix:
                return 1
            else:
                return 0
        else:
            raise Exception("It Should be a Square Matrix.")

    def trace(self):
        """
        Returns the sum of all Diagonal Elements of the Matrix.
        """
        return sum(diag(self))

    def flatten(self):
        """
        Converts the Matrix to a 1-D List.
        """
        lst = []
        for i in range(self.rows):
            for j in range(self.columns):
                lst.append(self.matrix[i][j])
        return lst
    
    # def rank(self):
    #     for j in range(self.columns):
    #         self.matrix[1][j] = 2 * self.matrix[0][j] + self.matrix[1][j]
    #     for j in range(self.columns):
    #         self.matrix[2][j] = -3 * self.matrix[0][j] + self.matrix[2][j]
    #     for j in range(self.columns):
    #         self.matrix[2][j] = -3 * self.matrix[0][j] + self.matrix[2][j]


def matSum(m1, m2):
    """
    Parameter - Matrix1, Matrix2
    Return - Matrix1 + Matrix2
    """
    if m1.__class__ == m2.__class__ == Matrix:
        sm1, sm2 = m1.sizeMatrix(), m2.sizeMatrix()
        if sm1 == sm2:
            m3 = Matrix(sm1[0], sm1[1])
            for i in range(sm1[0]):
                temp = []
                for j in range(sm1[1]):
                    temp.append(m1.matrix[i][j] + m2.matrix[i][j])
                m3.matrix[i] = temp
            return m3
        else:
            raise Exception("Both Matrices must be in the same order.")
    else:
        raise Exception(
            "The Parameters must be an Instance of Class -> Matrix.")


def matSub(m1, m2):
    """
    Parameter - Matrix1, Matrix2
    Return - Matrix1 - Matrix2
    """
    if m1.__class__ == m2.__class__ == Matrix:
        sm1, sm2 = m1.sizeMatrix(), m2.sizeMatrix()
        if sm1 == sm2:
            m3 = Matrix(sm1[0], sm1[1])
            for i in range(sm1[0]):
                temp = []
                for j in range(sm1[1]):
                    temp.append(m1.matrix[i][j] - m2.matrix[i][j])
                m3.matrix[i] = temp
            return m3
        else:
            raise Exception("Both Matrices must be in the same order.")
    else:
        raise Exception(
            "The Parameters must be an Instance of Class -> Matrix.")


def matMul(m1, m2):
    """
    Parameter - Matrix1, Matrix2
    Return - Matrix1 * Matrix2
    """
    if m1.__class__ == m2.__class__ == Matrix:
        m1size = m1.sizeMatrix()
        m2size = m2.sizeMatrix()
        if m1size[1] == m2size[0]:
            m3 = Matrix(m1size[0], m2size[1])
            for i in range(m1size[0]):
                temp2 = []
                for j in range(m2size[1]):
                    temp = 0
                    for k in range(m1size[1]):
                        temp += m1.matrix[i][k] * m2.matrix[k][j]
                    temp2.append(temp)
                m3.matrix[i] = temp2
            return m3
        else:
            raise Exception(
                "Both Matrices must be in the order of A[m][n] and T[n][p].")
    else:
        raise Exception(
            "The Parameters must be an Instance of Class -> Matrix.")


def matDiv(m1, m2):
    """
    Parameter - Matrix1, Matrix2
    Return - Matrix1 * (Matrix2^-1)
    """
    if m1.__class__ == m2.__class__ == Matrix:
        m2 = m2.inverse()
        m1size = m1.sizeMatrix()
        m2size = m2.sizeMatrix()
        if m1size[1] == m2size[0]:
            m3 = Matrix(m1size[0], m2size[1])
            for i in range(m1size[0]):
                temp2 = []
                for j in range(m2size[1]):
                    temp = 0
                    for k in range(m1size[1]):
                        temp += m1.matrix[i][k] * m2.matrix[k][j]
                    temp2.append(temp)
                m3.matrix[i] = temp2
            return m3
        else:
            raise Exception(
                "Both Matrices must be in the order of A[m][n] and T[n][p].")
    else:
        raise Exception(
            "The Parameters must be an Instance of Class -> Matrix.")


def diag(m1: Matrix):
    """
    Parameter - List
    Return - A Diagonal Matrix, (List Elements = Diagonal Elements)
    Parameter - Matrix
    Return - A List with all the Diagonal Elements
    """
    if m1.__class__ == list:
        m2 = Matrix(len(m1), len(m1))
        k = 0
        for i in range(len(m1)):
            m2.matrix[i][i] = m1[k]
            k += 1
        return m2
    elif m1.__class__ == Matrix:
        m2 = []
        for i in range(m1.rows):
            m2.append(m1.matrix[i][i])
        return m2


def identity(m1: Matrix):
    """
    Returns an Identity Matrix.
    """
    if m1.__class__ == Matrix:
        s = m1.sizeMatrix()
        if s[0] == s[1]:
            for i in range(m1.rows):
                for j in range(m1.columns):
                    if i == j:
                        m1.matrix[i][i] = 1
                    else:
                        m1.matrix[i][j] = 0
            return m1
        else:
            raise Exception(
                "Identity Matrix is only Possible for a Square Matrix.")
    else:
        raise TypeError("Object should be an Instance of Class -> Matrix.")

def echelon(m1 : Matrix):
    """
    Converts the Matrix to it's Echelon Form
    Return - Changes are applied to the Original Matrix 
    """
    if m1.__class__ == Matrix:
        for i in range(m1.sizeMatrix()[0]):
            if m1.matrix[i][0]==1:
                tmp = list(m1.matrix[i])
                m1.matrix[i]=m1.matrix[0]
                m1.matrix[0]=tmp
                break
        k=0
        for i in range(1,m1.sizeMatrix()[0]):
            tmp2=m1.matrix[i][k]
            for j in range(m1.sizeMatrix()[1]):
                m1.matrix[i][j]=(tmp2*m1.matrix[0][j])-m1.matrix[i][j]
        k+=1
        for i in range(1,m1.sizeMatrix()[0]):
            tmp2=m1.matrix[i][k]
            for j in range(m1.sizeMatrix()[1]):
                m1.matrix[i][j]=m1.matrix[i][j]/tmp2
                
    return m1

def determinant(m1: Matrix):
    """
    Calculates the Determinant of the Matrix.
    """
    if m1.__class__==Matrix:
        if m1.sizeMatrix()==(1,1):
            return m1.matrix[0][0]
    def sM(m1):
        if m1[0].__class__ == int or m1[0].__class__ == float:
            return (None, None)
        return (len(m1), len(m1[0]))

    def det2(m1):
        if sM(m1) == (2, 2):
            return (m1[0][0]*m1[1][1]) - (m1[0][1]*m1[1][0])
        else:
            raise Exception(
                "This function only returns the determinant of Matrices with order 2x2."
            )
    if m1.__class__ == Matrix:
        m1 = m1.matrix
    elif m1.__class__ == list:
        pass
    else:
        raise Exception("Object must be an Instance of Class -> Matrix/List.")
    s = sM(m1)
    if s == (2, 2):
        return det2(m1)
    if s[0] != s[1]:
        raise Exception(
            "Determinant can only be calculated with the Matrices of order (NxN)."
        )
    m2 = []
    op = "+"
    for k in range(s[0]):
        temp2 = []
        for i in range(s[0]):
            temp = []
            for j in range(s[1]):
                if i != 0 and j != k:
                    temp.append(m1[i][j])
            if temp != []:
                temp2.append(temp)
        if sM(temp) == (2, 2):
            temp2 = det2(temp2)
        else:
            temp2 = determinant(temp2)
        m2.append([m1[0][k] * temp2])
        if op == "+":
            m2[-1] = m2[-1][0]
            op = "-"
        else:
            m2[-1] = -m2[-1][0]
            op = "+"
    return sum(m2)


if __name__ == '__main__':
    a = Matrix(4, 4)
    a.listTomatrix([2,4,1,10,4,8,6,11,1,8,9,12,1,2,3,4])
    a.printMatrix()
    echelon(a).printMatrix()
