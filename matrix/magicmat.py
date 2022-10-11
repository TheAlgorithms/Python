"""       MAGIC MATRIX

A n×n square matrix of positive integers is called a magic square if the following sums are equal:

(1) row-sum : sum of numbers in every row; there are nn such values, one for each row

(2) column-sum : sum of numbers in every column; there are nn such values, one for each column

(3) diagonal-sum : sum of numbers in both the diagonals; there are two values


"""


def magic(mat):

    # first get the dimension of the matrix

    m = len(mat)

    # the sum of the two diagonals
    d1sum, d2sum = 0, 0

    # (i, i) goes from top-left -> bottom-right
    # (i, m - i - 1) goes from top-right -> bottom-left
    # note that a single loop is enough; no nesting required

    for i in range(m):

        d1sum += mat[i][i]

        d2sum += mat[i][m - i - 1]

    # if the two diagonal sums are unequal, we can return NO
    # unnecessary computation can be avoided

    if not (d1sum == d2sum):
        return "NO"

    # get row-sum and column-sum

    for i in range(m):
        rsum, csum = 0, 0

        for j in range(m):
            rsum += mat[i][j]
            csum += mat[j][i]

        if not (rsum == csum == d1sum):
            return "NO"

    # if the code reaches this level
    # then all requirements of a magic-square are satisfied
    # so we can safely return YES

    return "YES"


mat = [[1, 2], [2, 1]]
print(magic(mat))

# OUTPUT -> NO

mat = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
print(magic(mat))
