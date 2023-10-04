def spiral_order(matrix) -> None:
    """
    Traverses a 2D matrix in a spiral order and returns the elements in a list.

    Args:
        matrix (List[List[int]]): The input 2D matrix.

    Returns:
        List[int]: A list containing the elements of the matrix in spiral order.

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6],
        ...     [7, 8, 9]
        ... ]
        >>> spiral_order(matrix)
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
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
    doctest.testmod()
