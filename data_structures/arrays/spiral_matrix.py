from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Traverses a 2D matrix in a spiral order and returns the elements in a list.

    Args:
        matrix (List[List[int]]): The input 2D matrix.

    Returns:
        List[int]: A list containing the elements of the matrix in spiral order.
    """
    ans = []
    row = len(matrix)
    column = len(matrix[0])
    count = 0
    total = row * column

    starting_row = 0
    starting_col = 0
    ending_row = row - 1
    ending_col = column - 1

    while count < total:
        # Left to Right
        for i in range(starting_col, ending_col + 1):
            if count >= total:
                break
            ans.append(matrix[starting_row][i])
            count += 1
        starting_row += 1

        # Top to Bottom
        for i in range(starting_row, ending_row + 1):
            if count >= total:
                break
            ans.append(matrix[i][ending_col])
            count += 1
        ending_col -= 1

        # Right to Left
        for i in range(ending_col, starting_col - 1, -1):
            if count >= total:
                break
            ans.append(matrix[ending_row][i])
            count += 1
        ending_row -= 1

        # Bottom to Top
        for i in range(ending_row, starting_row - 1, -1):
            if count >= total:
                break
            ans.append(matrix[i][starting_col])
            count += 1
        starting_col += 1

    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
