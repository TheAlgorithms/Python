from sys import stdin


def largestRoworCol(mat, nRows, mCols):
    # Row wise Sum
    rowSumList = []
    for i in range(nRows):
        sumRow = 0
        for j in range(mCols):
            sumRow += mat[i][j]
        rowSumList.append(sumRow)
    print(rowSumList)

    # Column wise Sum
    colSumList = []
    i = 0
    j = 0
    for j in range(mCols):
        sumCol = 0
        for i in range(nRows):
            sumCol += mat[i][j]
        colSumList.append(sumCol)
    print(colSumList)

    maxElementOfRow = max(rowSumList)
    maxElementOfCol = max(colSumList)

    if maxElementOfRow >= maxElementOfCol:
        return (
            "row"
            + " "
            + str(rowSumList.index(maxElementOfRow))
            + " "
            + str(maxElementOfRow)
        )

    else:
        return (
            "column"
            + " "
            + str(colSumList.index(maxElementOfCol))
            + " "
            + str(maxElementOfCol)
        )


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    largestRoworCol(mat, nRows, mCols)

    t -= 1
