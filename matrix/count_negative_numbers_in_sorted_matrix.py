"""
Given an matrix of numbers in which all rows and all columns are sorted in decreasing
order, return the number of negative numbers in grid.

Reference: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
"""


def generate_large_matrix() -> list[list[int]]:
    """
    >>> generate_large_matrix() # doctest: +ELLIPSIS
    [[1000, ..., -999], [999, ..., -1001], ..., [2, ..., -1998]]
    """
    return [list(range(1000 - i, -1000 - i, -1)) for i in range(1000)]


grid = generate_large_matrix()
test_grids = (
    [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
    [[3, 2], [1, 0]],
    [[7, 7, 6]],
    [[7, 7, 6], [-1, -2, -3]],
    grid,
)


def validate_grid(grid: list[list[int]]) -> None:
    """
    Validate that the rows and columns of the grid is sorted in decreasing order.
    >>> for grid in test_grids:
    ...     validate_grid(grid)
    """
    assert all(row == sorted(row, reverse=True) for row in grid)
    assert all(list(col) == sorted(col, reverse=True) for col in zip(*grid))


def find_negative_index(array: list[int]) -> int:
    """
    Find the smallest negative index

    >>> find_negative_index([0,0,0,0])
    4
    >>> find_negative_index([4,3,2,-1])
    3
    >>> find_negative_index([1,0,-1,-10])
    2
    >>> find_negative_index([0,0,0,-1])
    3
    >>> find_negative_index([11,8,7,-3,-5,-9])
    3
    >>> find_negative_index([-1,-1,-2,-3])
    0
    >>> find_negative_index([5,1,0])
    3
    >>> find_negative_index([-5,-5,-5])
    0
    >>> find_negative_index([0])
    1
    >>> find_negative_index([])
    0
    """
    left = 0
    right = len(array) - 1

    # Edge cases such as no values or all numbers are negative.
    if not array or array[0] < 0:
        return 0

    while right + 1 > left:
        mid = (left + right) // 2
        num = array[mid]

        # Num must be negative and the index must be greater than or equal to 0.
        if num < 0 and array[mid - 1] >= 0:
            return mid

        if num >= 0:
            left = mid + 1
        else:
            right = mid - 1
    # No negative numbers so return the last index of the array + 1 which is the length.
    return len(array)


def count_negatives_binary_search(grid: list[list[int]]) -> int:
    """
    An O(m logn) solution that uses binary search in order to find the boundary between
    positive and negative numbers

    >>> [count_negatives_binary_search(grid) for grid in test_grids]
    [8, 0, 0, 3, 1498500]
    """
    total = 0
    bound = len(grid[0])

    for i in range(len(grid)):
        bound = find_negative_index(grid[i][:bound])
        total += bound
    return (len(grid) * len(grid[0])) - total


def count_negatives_brute_force(grid: list[list[int]]) -> int:
    """
    This solution is O(n^2) because it iterates through every column and row.

    >>> [count_negatives_brute_force(grid) for grid in test_grids]
    [8, 0, 0, 3, 1498500]
    """
    return len([number for row in grid for number in row if number < 0])


def count_negatives_brute_force_with_break(grid: list[list[int]]) -> int:
    """
    Similar to the brute force solution above but uses break in order to reduce the
    number of iterations.

    >>> [count_negatives_brute_force_with_break(grid) for grid in test_grids]
    [8, 0, 0, 3, 1498500]
    """
    total = 0
    for row in grid:
        for i, number in enumerate(row):
            if number < 0:
                total += len(row) - i
                break
    return total


def benchmark() -> None:
    """Benchmark our functions next to each other"""
    from timeit import timeit

    print("Running benchmarks")
    setup = (
        "from __main__ import count_negatives_binary_search, "
        "count_negatives_brute_force, count_negatives_brute_force_with_break, grid"
    )
    for func in (
        "count_negatives_binary_search",  # took 0.7727 seconds
        "count_negatives_brute_force_with_break",  # took 4.6505 seconds
        "count_negatives_brute_force",  # took 12.8160 seconds
    ):
        time = timeit(f"{func}(grid=grid)", setup=setup, number=500)
        print(f"{func}() took {time:0.4f} seconds")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
