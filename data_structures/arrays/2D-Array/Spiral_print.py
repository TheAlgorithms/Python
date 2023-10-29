from sys import stdin


def spiralPrint(mat, nRows, mCols):
    top = 0
    left = 0
    bottom = nRows - 1
    right = mCols - 1

    i = 0
    j = 0
    while left <= right and top <= bottom:
        j = left
        c = 0
        while j <= right:
            print(mat[i][j], end=" ")
            j += 1
            c += 1
        if left > right or top > bottom:
            return
        # as the j wiil be past the right we need to correct it now
        j = right
        top += 1  # the top row is traversed
        i = top
        while i <= bottom:
            print(mat[i][j], end=" ")
            i += 1
            c += 1
        if left > right or top > bottom:
            return
        i = bottom
        right -= 1  # just as top
        j = right
        if left > right or top > bottom:
            return
        while j >= left:
            print(mat[i][j], end=" ")
            j -= 1
            c += 1
        bottom -= 1
        j = left
        i = bottom
        if left > right or top > bottom:
            return
        while i >= top:
            print(mat[i][j], end=" ")
            i -= 1
            c += 1
        i = top
        left += 1


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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
