"""
Python Program to find prefix sum of a 2D array
"""


def calculate_prefix_sum(matrix: list[list[int]]) -> list[list[int]]:
    """
    Calculate the prefix sum of a 2D matrix.
    Prefix Sum Formula:
    prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1]
    - prefix_sum[i - 1][j - 1] + matrix[i][j]

    :param matrix: A 2D matrix.
    :return: A matrix containing the prefix sums.

    >>> calculate_prefix_sum([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

    >>> calculate_prefix_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 3, 6], [5, 12, 21], [12, 27, 45]]
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize the prefix sum matrix with zeros, with the
    # same dimensions as the original matrix.
    prefix_sum = [[0 for _ in range(cols)] for _ in range(rows)]

    # Calculate the prefix sum for the top-left cell.
    prefix_sum[0][0] = matrix[0][0]

    # Calculate cumulative sums for the first row.
    for i in range(1, cols):
        prefix_sum[0][i] = prefix_sum[0][i - 1] + matrix[0][i]

    # Calculate cumulative sums for the first column.
    for i in range(1, rows):
        prefix_sum[i][0] = prefix_sum[i - 1][0] + matrix[i][0]

    # Update the values in the cells using the general formula.
    for i in range(1, rows):
        for j in range(1, cols):
            # The value in each cell is the sum of:
            # - The cell above it
            # - The cell to the left of it
            # - Subtracting the overlapping cell
            # - Adding the value from the original matrix
            prefix_sum[i][j] = (
                prefix_sum[i - 1][j]
                + prefix_sum[i][j - 1]
                - prefix_sum[i - 1][j - 1]
                + matrix[i][j]
            )

    return prefix_sum


def display_matrix(matrix: list[list[int]]) -> None:
    """
    Display a 2D matrix.

    :param matrix: A 2D matrix.

    Display a 2D matrix by printing each row's elements separated by spaces.

    >>> display_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    1 2 3
    4 5 6
    7 8 9

    >>> display_matrix([[10, 20, 30], [40, 50, 60]])
    10 20 30
    40 50 60
    """
    for row in matrix:
        # Join the elements of each row with spaces and print the result.
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    # Calculate the prefix sum of the 2D matrix
    prefix_sum_matrix = calculate_prefix_sum(matrix)

    # Display the prefix sum matrix
    display_matrix(prefix_sum_matrix)
