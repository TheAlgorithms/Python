from typing import list


def spiralorder(matrix: list[list[int]]) -> list[int]:
    """
    Get the elements of a 2D matrix in spiral order.

    Args:
    matrix (list[list[int]]): The input 2D matrix.

    Returns:
    List[int]: A list containing the elements of the matrix in spiral order.

    Example:
    >>> a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    >>> spiralOrder(a)
    [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    """
    ans = []

    if not matrix:
        return ans

    m = len(matrix)
    n = len(matrix[0])
    seen = [[False for _ in range(n)] for _ in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0

    for _ in range(m * n):  # Removed the unnecessary loop variable `i`
        ans.append(matrix[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]

        if 0 <= cr < m and 0 <= cc < n and not seen[cr][cc]:
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]

    return ans


# Driver code
if __name__ == "__main__":
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    # Function call
    for x in spiralorder(a):
        print(x, end=" ")
    print()
