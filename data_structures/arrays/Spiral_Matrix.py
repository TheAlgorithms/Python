def spiral_order(matrix):
    ans = []
    row = len(matrix)
    column = len(matrix[0])
    count = 0
    total = row * column

    startingrow = 0
    startingcol = 0
    endingrow = row - 1
    endingcolumn = column - 1
    while count < total:
        for i in range(startingcol, endingcolumn + 1):
            if count >= total:
                break
            ans.append(matrix[startingrow][i])
            count += 1
        startingrow += 1

        for i in range(startingrow, endingrow + 1):
            if count >= total:
                break
            ans.append(matrix[i][endingcolumn])
            count += 1
        endingcolumn -= 1

        for i in range(endingcolumn, startingcol - 1, -1):
            if count >= total:
                break
            ans.append(matrix[endingrow][i])
            count += 1
        endingrow -= 1

        for i in range(endingrow, startingrow - 1, -1):
            if count >= total:
                break
            ans.append(matrix[i][startingcol])
            count += 1
        startingcol += 1

    return ans


if __name__ == "__main__":
    import doctest

    result = spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(result)
    doctest.testmod()
