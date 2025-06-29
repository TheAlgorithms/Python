"""
This implementation demonstrates how to generate the elements of Pascal's Triangle.
An element with row index r and column index c can be derived as:
triangle[r][c] = triangle[r-1][c-1] + triangle[r-1][c]

Pascal's Triangle is a triangular array containing binomial coefficients.
https://en.wikipedia.org/wiki/Pascal%27s_triangle
"""

from collections.abc import Callable
from timeit import timeit


def print_pascal_triangle(num_rows: int) -> None:
    """
    Print Pascal's triangle for the specified number of rows
    >>> print_pascal_triangle(5)
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    """
    triangle = generate_pascal_triangle(num_rows)
    for row_idx in range(num_rows):
        # Print leading spaces
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
    Generate Pascal's triangle for the specified number of rows
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
    ValueError: Input value 'num_rows' must be >= 0
    >>> generate_pascal_triangle(7.89)
    Traceback (most recent call last):
        ...
    TypeError: Input value 'num_rows' must be an integer
    """

    if not isinstance(num_rows, int):
        raise TypeError("Input value 'num_rows' must be an integer")

    if num_rows == 0:
        return []
    if num_rows < 0:
        raise ValueError("Input value 'num_rows' must be >= 0")

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
    # First and last elements of current row are always 1
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
    above_left = triangle[current_row_idx - 1][current_col_idx - 1]
    above_right = triangle[current_row_idx - 1][current_col_idx]
    current_row[current_col_idx] = above_left + above_right


def generate_pascal_triangle_optimized(num_rows: int) -> list[list[int]]:
    """
    Returns a matrix representing Pascal's triangle.
    Reduces operations by half by eliminating redundant calculations.
    
    :param num_rows: Number of rows in the Pascal's triangle
    :return: 2D list representing the Pascal's triangle
    
    >>> generate_pascal_triangle_optimized(3)
    [[1], [1, 1], [1, 2, 1]]
    >>> generate_pascal_triangle_optimized(1)
    [[1]]
    >>> generate_pascal_triangle_optimized(0)
    []
    >>> generate_pascal_triangle_optimized(-5)
    Traceback (most recent call last):
        ...
    ValueError: Input value 'num_rows' must be >= 0
    >>> generate_pascal_triangle_optimized(7.89)
    Traceback (most recent call last):
        ...
    TypeError: Input value 'num_rows' must be an integer
    """

    if not isinstance(num_rows, int):
        raise TypeError("Input value 'num_rows' must be an integer")

    if num_rows == 0:
        return []
    if num_rows < 0:
        raise ValueError("Input value 'num_rows' must be >= 0")

    result: list[list[int]] = [[1]]

    for row_index in range(1, num_rows):
        temp_row = [0] + result[-1] + [0]
        row_length = row_index + 1
        # Calculate number of distinct elements in row
        distinct_elements = sum(divmod(row_length, 2))
        row_first_half = [
            temp_row[i - 1] + temp_row[i] for i in range(1, distinct_elements + 1)
        ]
        row_second_half = row_first_half[: (row_index + 1) // 2]
        row_second_half.reverse()
        row = row_first_half + row_second_half
        result.append(row)

    return result



def benchmark() -> None:
    """
    Benchmark functions with different input sizes
    """
    def benchmark_a_function(func: Callable, value: int) -> None:
        call = f"{func.__name__}({value})"
        timing = timeit(f"__main__.{call}", setup="import __main__")
        print(f"{call:38} -- {timing:.4f} seconds")

    for value in range(15):  # (1, 7, 14):
        for func in (generate_pascal_triangle, generate_pascal_triangle_optimized):
            benchmark_a_function(func, value)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
