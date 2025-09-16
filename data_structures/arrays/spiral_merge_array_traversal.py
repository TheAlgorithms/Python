from typing import List


def spiral_traverse(matrix: List[List[int]]) -> List[int]:
    """
    Takes a 2D array (matrix) and returns its elements in spiral order (clockwise from the top-left).

    Uses four pointers: top, bottom, left, right to track the current layer of the matrix.
    Loops through top row → right column → bottom row → left column until all elements are visited.
    """
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse top row from left to right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1  # move top boundary down

        # Traverse right column from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1  # move right boundary left

        if top <= bottom:
            # Traverse bottom row from right to left
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1  # move bottom boundary up

        if left <= right:
            # Traverse left column from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1  # move left boundary right

    return result


def spiral_merge_matrices(matrices: List[List[List[int]]]) -> List[int]:
    """
    Accepts a list of matrices.

    First, converts each matrix into its spiral order list using spiral_traverse.
    Then merges them alternately: take the first element from each spiral, then the second, etc., until all are merged.
    """
    merged = []
    # Convert each matrix to spiral order
    spirals = [spiral_traverse(m) for m in matrices]
    max_len = max(len(s) for s in spirals)

    # Merge elements alternately from each spiral
    for i in range(max_len):
        for s in spirals:
            if i < len(s):
                merged.append(s[i])
    return merged


if __name__ == "__main__":
    """
    Ensures that the example usage code runs only if the script is executed directly,
    not when imported as a module.

    Example Output for the given mat1 and mat2:
    Merged Spiral Array: [1, 10, 2, 11, 3, 12, 6, 15, 9, 18, 8, 17, 7, 16, 4, 13, 5, 14]
    """
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    mat2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

    merged = spiral_merge_matrices([mat1, mat2])
    print("Merged Spiral Array:", merged)
