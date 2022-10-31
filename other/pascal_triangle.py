"""
This implementation demonstrates how to generate the
elements of a Pascal's triangle. The element having
a row index of r and column index of c can be derived
as follows:
triangle[r][c] = triangle[r-1][c-1]+triangle[r-1][c]
What is Pascal's triangle?
- It is a triangular array containing binomial coefficients.
Refer to (https://en.wikipedia.org/wiki/Pascal%27s_triangle)
for more info about this triangle.
"""


def print_pascal_triangle(num_rows: int) -> None:
    """
    Print Pascal's triangle for different number of rows
    >>> print_pascal_triangle(5)
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    """
    triangle = generate_pascal_triangle(num_rows)
    for row_idx in range(num_rows):
        # Print left spaces
        for _ in range(num_rows - row_idx - 1):
            print(end=" ")
        # Print row values
        for col_idx in range(row_idx + 1):
            if col_idx != row_idx:
                print(triangle[row_idx][col_idx], end=" ")
            else:
                print(triangle[row_idx][col_idx], end="")
        print()


def generate_pascal_triangle(num_rows: int) -> list[list[int]]:
    """
    Create Pascal's triangle for different number of rows
    >>> generate_pascal_triangle(0)
    []
    >>> generate_pascal_triangle(1)
    [[1]]
    >>> generate_pascal_triangle(2)
    [[1], [1, 1]]
    >>> generate_pascal_triangle(3)
    [[1], [1, 1], [1, 2, 1]]
    >>> generate_pascal_triangle(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    >>> generate_pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> generate_pascal_triangle(-5)
    Traceback (most recent call last):
        ...
    ValueError: The input value of 'num_rows' should be greater than or equal to 0
    >>> generate_pascal_triangle(7.89)
    Traceback (most recent call last):
        ...
    TypeError: The input value of 'num_rows' should be 'int'
    """

    if not isinstance(num_rows, int):
        raise TypeError("The input value of 'num_rows' should be 'int'")

    if num_rows == 0:
        return []
    elif num_rows < 0:
        raise ValueError(
            "The input value of 'num_rows' should be greater than or equal to 0"
        )

    triangle: list[list[int]] = []
    for current_row_idx in range(num_rows):
        current_row = populate_current_row(triangle, current_row_idx)
        triangle.append(current_row)
    return triangle


def populate_current_row(triangle: list[list[int]], current_row_idx: int) -> list[int]:
    """
    >>> triangle = [[1]]
    >>> populate_current_row(triangle, 1)
    [1, 1]
    """
    current_row = [-1] * (current_row_idx + 1)
    # first and last elements of current row are equal to 1
    current_row[0], current_row[-1] = 1, 1
    for current_col_idx in range(1, current_row_idx):
        calculate_current_element(
            triangle, current_row, current_row_idx, current_col_idx
        )
    return current_row


def calculate_current_element(
    triangle: list[list[int]],
    current_row: list[int],
    current_row_idx: int,
    current_col_idx: int,
) -> None:
    """
    >>> triangle = [[1], [1, 1]]
    >>> current_row = [1, -1, 1]
    >>> calculate_current_element(triangle, current_row, 2, 1)
    >>> current_row
    [1, 2, 1]
    """
    above_to_left_elt = triangle[current_row_idx - 1][current_col_idx - 1]
    above_to_right_elt = triangle[current_row_idx - 1][current_col_idx]
    current_row[current_col_idx] = above_to_left_elt + above_to_right_elt


def generate_pascal_triangle_optimized(num_rows: int) -> list[list[int]]:
    """
    This function returns a matrix representing the corresponding pascal's triangle
    according to the given input of number of rows of Pascal's triangle to be generated.
    It reduces the operations done to generate a row by half
    by eliminating redundant calculations.

    :param num_rows: Integer specifying the number of rows in the Pascal's triangle
    :return: 2-D List (matrix) representing the Pascal's triangle

    Return the Pascal's triangle of given rows
    >>> generate_pascal_triangle_optimized(3)
    [[1], [1, 1], [1, 2, 1]]
    >>> generate_pascal_triangle_optimized(1)
    [[1]]
    >>> generate_pascal_triangle_optimized(0)
    []
    >>> generate_pascal_triangle_optimized(-5)
    Traceback (most recent call last):
        ...
    ValueError: The input value of 'num_rows' should be greater than or equal to 0
    >>> generate_pascal_triangle_optimized(7.89)
    Traceback (most recent call last):
        ...
    TypeError: The input value of 'num_rows' should be 'int'
    """

    if not isinstance(num_rows, int):
        raise TypeError("The input value of 'num_rows' should be 'int'")

    if num_rows == 0:
        return []
    elif num_rows < 0:
        raise ValueError(
            "The input value of 'num_rows' should be greater than or equal to 0"
        )

    result: list[list[int]] = [[1]]

    for row_index in range(1, num_rows):
        temp_row = [0] + result[-1] + [0]
        row_length = row_index + 1

        # It calculates the number of distinct elements in a row
        distinct_elements = (
            row_length // 2 if row_length % 2 == 0 else row_length // 2 + 1
        )

        row_first_half = [
            temp_row[x - 1] + temp_row[x] for x in range(1, distinct_elements + 1)
        ]

        row_second_half = row_first_half[: (row_index + 1) // 2]
        row_second_half.reverse()
        row = row_first_half + row_second_half
        result.append(row)

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
