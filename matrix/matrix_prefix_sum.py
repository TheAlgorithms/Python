# Python Program to find prefix sum of a 2D array


def calculate_prefix_sum(matrix: list[list[int]]) -> list[list[int]]:
    """
    Calculate the prefix sum of a 2D matrix.

    Prefix sum is a technique used to efficiently calculate the cumulative sum of subarrays in a 2D array.
    The idea is to compute a new array where each element represents the sum of all elements in the original array
    up to that position.

    Prefix Sum Formula:
    prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + matrix[i][j]

    :param matrix: A 2D matrix.
    :return: A matrix containing the prefix sums.

    >>> calculate_prefix_sum([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

    >>> calculate_prefix_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 3, 6], [5, 12, 21], [12, 27, 45]]
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize the prefix sum matrix with zeros, with the same dimensions as the original matrix.
    prefix_sum = [[0 for _ in range(cols)] for _ in range(rows)]

    # The prefix sum at the top-left corner is the same as the original matrix value.
    prefix_sum[0][0] = matrix[0][0]

    # Calculate cumulative sums for the first row.
    for i in range(1, cols):
        # The value in the first row is the sum of the previous value in the same row
        # and the value from the original matrix at the current column.
        prefix_sum[0][i] = prefix_sum[0][i - 1] + matrix[0][i]

    # Calculate cumulative sums for the first column.
    for i in range(1, rows):
        # The value in the first column is the sum of the previous value in the same column
        # and the value from the original matrix at the current row.
        prefix_sum[i][0] = prefix_sum[i - 1][0] + matrix[i][0]

    # Update the values in the cells using the general formula.
    for i in range(1, rows):
        for j in range(1, cols):
            # The value in each cell is the sum of:
            # - The cell above it (prefix_sum[i-1][j])
            # - The cell to the left of it (prefix_sum[i][j-1])
            # - Subtracting the overlapping cell (top-left: prefix_sum[i-1][j-1])
            # - Adding the value from the original matrix (matrix[i][j])
            prefix_sum[i][j] = (
                prefix_sum[i - 1][j]  # Sum of values above
                + prefix_sum[i][j - 1]  # Sum of values to the left
                - prefix_sum[i - 1][j - 1]  # Subtract the overlapping cell
                + matrix[i][j]  # Add the value from the original matrix
            )

    return prefix_sum


def display_matrix(matrix) -> None:
    """
    Display a 2D matrix.

    :param matrix: A 2D matrix.
    """
    for row in matrix:
        # Join the elements of each row with spaces and print the result.
        print(" ".join(str(cell) for cell in row))


if __name__ == "__main__":
    a = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    # Calculate the prefix sum of the 2D matrix
    prefix_sum_matrix = calculate_prefix_sum(matrix)

    # Display the prefix sum matrix
    display_matrix(prefix_sum_matrix)
