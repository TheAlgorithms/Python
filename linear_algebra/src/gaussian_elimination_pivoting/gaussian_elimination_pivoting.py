import numpy as np

matrix = np.array(
    [
        [5.0, -5.0, -3.0, 4.0, -11.0],
        [1.0, -4.0, 6.0, -4.0, -10.0],
        [-2.0, -5.0, 4.0, -5.0, -12.0],
        [-3.0, -3.0, 5.0, -5.0, 8.0],
    ],
    dtype=float,
)


def solve_linear_system(matrix: np.ndarray) -> np.ndarray:
    """
    Solve a linear system of equations using Gaussian elimination with partial pivoting

    Args:
    - matrix: Coefficient matrix with the last column representing the constants.

    Returns:
    - Solution vector.

    Raises:
    - ValueError: If the matrix is not correct (i.e., singular).

    https://courses.engr.illinois.edu/cs357/su2013/lect.htm Lecture 7

    Example:
    >>> A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float)
    >>> B = np.array([8, -11, -3], dtype=float)
    >>> solution = solve_linear_system(np.column_stack((A, B)))
    >>> np.allclose(solution, np.array([2., 3., -1.]))
    True
    >>> solve_linear_system(np.array([[0, 0], [0, 0]],  dtype=float))
    array([nan, nan])
    """
    ab = np.copy(matrix)
    num_of_rows = ab.shape[0]
    num_of_columns = ab.shape[1] - 1
    x_lst: list[float] = []

    # Lead element search
    for column_num in range(num_of_rows):
        for i in range(column_num, num_of_columns):
            if abs(ab[i][column_num]) > abs(ab[column_num][column_num]):
                ab[[column_num, i]] = ab[[i, column_num]]
                if ab[column_num, column_num] == 0.0:
                    raise ValueError("Matrix is not correct")
            else:
                pass
        if column_num != 0:
            for i in range(column_num, num_of_rows):
                ab[i, :] -= (
                    ab[i, column_num - 1]
                    / ab[column_num - 1, column_num - 1]
                    * ab[column_num - 1, :]
                )

    # Upper triangular matrix
    for column_num in range(num_of_rows):
        for i in range(column_num, num_of_columns):
            if abs(ab[i][column_num]) > abs(ab[column_num][column_num]):
                ab[[column_num, i]] = ab[[i, column_num]]
                if ab[column_num, column_num] == 0.0:
                    raise ValueError("Matrix is not correct")
            else:
                pass
        if column_num != 0:
            for i in range(column_num, num_of_rows):
                ab[i, :] -= (
                    ab[i, column_num - 1]
                    / ab[column_num - 1, column_num - 1]
                    * ab[column_num - 1, :]
                )

    # Find x vector (Back Substitution)
    for column_num in range(num_of_rows - 1, -1, -1):
        x = ab[column_num, -1] / ab[column_num, column_num]
        x_lst.insert(0, x)
        for i in range(column_num - 1, -1, -1):
            ab[i, -1] -= ab[i, column_num] * x

    # Return the solution vector
    return np.asarray(x_lst)


if __name__ == "__main__":
    from doctest import testmod
    from pathlib import Path

    testmod()
    file_path = Path(__file__).parent / "matrix.txt"
    try:
        matrix = np.loadtxt(file_path)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.  Using default matrix instead.")

    # Example usage:
    print(f"Matrix:\n{matrix}")
    print(f"{solve_linear_system(matrix) = }")
