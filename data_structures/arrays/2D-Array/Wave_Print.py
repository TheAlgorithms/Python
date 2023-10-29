from sys import stdin


def wavePrint(mat, nRows, mCols):
    # Your code goes here
    for j in range(mCols):
        if j % 2 == 0:
            for i in range(nRows):
                print(mat[i][j], end=" ")
        else:
            for i in range(nRows - 1, -1, -1):
                print(mat[i][j], end=" ")


# Taking Iput Using Fast I/O
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
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1
