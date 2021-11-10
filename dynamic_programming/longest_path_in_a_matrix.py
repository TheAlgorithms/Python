def find_longest_path_from_a_cell(
    y_coordinate: int, x_coordinate: int, mat: list[list[int]], dp: list[list[int]]
) -> int:
    """
    Find the length of longest path of increasing sequence in a matrix
    from cell at row = y_coordinate, column = x_coordinate in matrix mat,
    dp has the longest path from any cell (x,y), or else, -1.
    >>> find_longest_path_from_a_cell(0, 0, [[0, 1], [3, 2]], [[-1, -1], [-1, -1]])
    4
    """
    n = len(mat)
    if y_coordinate < 0 or y_coordinate >= n or x_coordinate < 0 or x_coordinate >= n:
        return 0
    if dp[y_coordinate][x_coordinate] != -1:
        return dp[y_coordinate][x_coordinate]

    x, y, z, w = -1, -1, -1, -1

    if x_coordinate < n - 1 and (
        (mat[y_coordinate][x_coordinate] + 1) == mat[y_coordinate][x_coordinate + 1]
    ):
        x = 1 + find_longest_path_from_a_cell(y_coordinate, x_coordinate + 1, mat, dp)
    if x_coordinate > 0 and (
        mat[y_coordinate][x_coordinate] + 1 == mat[y_coordinate][x_coordinate - 1]
    ):
        y = 1 + find_longest_path_from_a_cell(y_coordinate, x_coordinate - 1, mat, dp)
    if y_coordinate > 0 and (
        mat[y_coordinate][x_coordinate] + 1 == mat[y_coordinate - 1][x_coordinate]
    ):
        z = 1 + find_longest_path_from_a_cell(y_coordinate - 1, x_coordinate, mat, dp)
    if y_coordinate < n - 1 and (
        mat[y_coordinate][x_coordinate] + 1 == mat[y_coordinate + 1][x_coordinate]
    ):
        w = 1 + find_longest_path_from_a_cell(y_coordinate + 1, x_coordinate, mat, dp)

    dp[y_coordinate][x_coordinate] = max(x, max(y, max(z, max(w, 1))))
    return dp[y_coordinate][x_coordinate]


def find_longest_path_in_a_matrix(mat: list[list[int]]) -> int:
    """
    Find the length of longest path of increasing sequence in a matrix mat.
    >>> find_longest_path_in_a_matrix([[0, 1], [3, 2]])
    4
    """
    n = len(mat)
    result = 1
    dp = [[-1 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                find_longest_path_from_a_cell(i, j, mat, dp)
            result = max(result, dp[i][j])
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
