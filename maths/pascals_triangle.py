"""
This module contains functions for and helpful for generating pascals triangle
"""


def pascals_triangle(num_rows: int) -> list:
    """
    This function returns a matrix representing the corresponding pascal's triangle
    according to the given input of number of rows of Pascal's triangle to be generated.
    The function has O(n^2) time complexity.
    :param num_rows: Integer specifying the number of rows in the Pascal's triangle
    :return: 2-D List (matrix) representing the Pascal's triangle

    Return the Pascal's triangle of given rows
    >>> pascals_triangle(3)
    [[1], [1, 1], [1, 2, 1]]
    >>> pascals_triangle(1)
    [[1]]
    >>> pascals_triangle(0)
    []
    >>> pascals_triangle(-5)
    Traceback (most recent call last):
        ...
    ValueError: The input value of 'num_rows' should be greater than or equal to 0
    >>> pascals_triangle(7.89)
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

    result = [[1]]

    for i in range(1, num_rows):
        temp_row = [0] + result[-1] + [0]

        # unique length calculates the len of pascal's triangle row
        # that has distinct elements
        # Calculating unique length will be helpful in reducing
        # redundant calculations
        unique_length = (i + 1) // 2 if (i + 1) % 2 == 0 else (i + 1) // 2 + 1
        row_first_half = [
            temp_row[x - 1] + temp_row[x] for x in range(1, unique_length + 1)
        ]
        row_second_half = row_first_half[: (i + 1) // 2]
        row_second_half.reverse()
        row = row_first_half + row_second_half
        result.append(row)

    return result


if __name__ == "__main__":
    from doctest import testmod
    testmod()
