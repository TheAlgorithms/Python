def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Rotates a given matrix 90 degrees clockwise.

    Args:
        matrix (List[List[int]]): The input matrix.

    Returns:
        List[List[int]]: The rotated matrix.

    Example:
        >>> rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        >>> rotate_matrix([[1, 2], [3, 4]])
        [[3, 1], [4, 2]]
    """
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    rotated = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            rotated[j][num_rows - 1 - i] = matrix[i][j]

    return rotated
