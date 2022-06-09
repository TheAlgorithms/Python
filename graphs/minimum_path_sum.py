def min_path_sum(grid: list) -> int:
    """
    Find the path from top left to bottom right of array of numbers
    with the lowest possible sum and return the sum along this path.
    >>> min_path_sum([
    ...     [1, 3, 1],
    ...     [1, 5, 1],
    ...     [4, 2, 1],
    ... ])
    7

    >>> min_path_sum([
    ...     [1, 0, 5, 6, 7],
    ...     [8, 9, 0, 4, 2],
    ...     [4, 4, 4, 5, 1],
    ...     [9, 6, 3, 1, 0],
    ...     [8, 4, 3, 2, 7],
    ... ])
    20

    >>> min_path_sum(None)
    Traceback (most recent call last):
        ...
    TypeError: The grid does not contain the appropriate information

    >>> min_path_sum([[]])
    Traceback (most recent call last):
        ...
    TypeError: The grid does not contain the appropriate information
    """

    if not grid or not grid[0]:
        raise TypeError("The grid does not contain the appropriate information")

    for cell_n in range(1, len(grid[0])):
        grid[0][cell_n] += grid[0][cell_n - 1]
    row_above = grid[0]

    for row_n in range(1, len(grid)):
        current_row = grid[row_n]
        grid[row_n] = fill_row(current_row, row_above)
        row_above = grid[row_n]

    return grid[-1][-1]


def fill_row(current_row: list, row_above: list) -> list:
    """
    >>> fill_row([2, 2, 2], [1, 2, 3])
    [3, 4, 5]
    """

    current_row[0] += row_above[0]
    for cell_n in range(1, len(current_row)):
        current_row[cell_n] += min(current_row[cell_n - 1], row_above[cell_n])

    return current_row


if __name__ == "__main__":
    import doctest

    doctest.testmod()
