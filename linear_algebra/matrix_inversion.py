import numpy as np

def invert_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """
    Returns the inverse of a square matrix using NumPy.

    Parameters:
    matrix (list[list[float]]): A square matrix.

    Returns:
    list[list[float]]: Inverted matrix if invertible, else raises error.
    """
    try:
        np_matrix = np.array(matrix)
        inv_matrix = np.linalg.inv(np_matrix)
        return inv_matrix.tolist()
    except np.linalg.LinAlgError:
        raise ValueError("Matrix is not invertible")


if __name__ == "__main__":
    mat = [
        [4, 7],
        [2, 6]
    ]
    print("Original Matrix:")
    print(mat)
    print("Inverted Matrix:")
    print(invert_matrix(mat))
