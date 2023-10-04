def spiralOrder(matrix):
    ans = []
    Row = len(matrix)
    Column = len(matrix[0])
    count = 0
    total = Row * Column

    startingRow = 0
    startingcol = 0
    endingRow = Row - 1
    endingColumn = Column - 1
    while count < total:
        for i in range(startingcol, endingColumn + 1):
            if count >= total:
                break
            ans.append(matrix[startingRow][i])
            count += 1
        startingRow += 1

        for i in range(startingRow, endingRow + 1):
            if count >= total:
                break
            ans.append(matrix[i][endingColumn])
            count += 1
        endingColumn -= 1

        for i in range(endingColumn, startingcol - 1, -1):
            if count >= total:
                break
            ans.append(matrix[endingRow][i])
            count += 1
        endingRow -= 1

        for i in range(endingRow, startingRow - 1, -1):
            if count >= total:
                break
            ans.append(matrix[i][startingcol])
            count += 1
        startingcol += 1

    return ans
