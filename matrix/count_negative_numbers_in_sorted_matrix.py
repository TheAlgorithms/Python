"""
Given an matrix of numbers in which all rows and all columns are sorted in decreasing
order, return the number of negative numbers in grid.

Leetcode reference: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
"""


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

    # Edge cases such as no values or
    # all numbers are negative
    if not array or array[0] < 0:
        return 0

    while right + 1 > left:
        mid = (left + right) // 2
        num = array[mid]

        # Num must be negative and the index about num
        # must be greater than or equal to 0
        if num < 0 and array[mid - 1] >= 0:
            return mid

        if num >= 0:
            left = mid + 1
        else:
            right = mid - 1
    # No negative numbers so return the last index
    # of the array + 1 which is also the length
    return len(array)


def count_negatives_binary_search(grid: list[list[int]]) -> int:
    """
    An O(m logn) solution that uses binary search
    in order to find the boundary between positive and
    negative numbers

    >>> count_negatives_binary_search(
    ...    [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    8
    >>> count_negatives_binary_search([[3,2],[1,0]])
    0
    >>> count_negatives_binary_search([[7,7,6]])
    0
    >>> count_negatives_binary_search([[7,7,6],[-1,-2,-3]])
    3
    """
    total = 0
    bound = len(grid[0])

    for i in range(len(grid)):
        bound = find_negative_index(grid[i][:bound])
        total += bound
    return (len(grid) * len(grid[0])) - total


def count_negatives_brute_force(grid: list[list[int]]) -> int:
    """
    This solution is O(n^2) because it iterates through
    every column and row.

    >>> count_negatives_brute_force(
    ...    [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    8
    >>> count_negatives_brute_force([[3,2],[1,0]])
    0
    >>> count_negatives_brute_force([[7,7,6]])
    0
    >>> count_negatives_brute_force([[7,7,6],[-1,-2,-3]])
    3
    """
    total = 0
    for m in range(len(grid)):
        for n in range(len(grid[m])):
            if grid[m][n] < 0:
                total += 1
    return total


def count_negatives_brute_force_with_break(grid: list[list[int]]) -> int:
    """
    Similar to the solution above, however uses break
    in order to reduce the number of iterations

    >>> count_negatives_brute_force_with_break(
    ...    [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    8
    >>> count_negatives_brute_force_with_break([[3,2],[1,0]])
    0
    >>> count_negatives_brute_force_with_break([[7,7,6]])
    0
    >>> count_negatives_brute_force_with_break([[7,7,6],[-1,-2,-3]])
    3
    """
    total = 0
    for row in grid:
        for i, number in enumerate(row):
            if number < 0:
                total += len(row) - i
                break
    return total


def generate_large_matrix() -> list[list[int]]:
    """
    >>> generate_large_matrix() # doctest: +ELLIPSIS
    [[1000, ..., -999], [999, ..., -1001], ..., [2, ..., -1998]]
    """
    return [list(range(1000 - i, -1000 - i, -1)) for i in range(1000)]


grid = generate_large_matrix()
def benchmark() -> None:
    """Benchmark our functions next to each other"""
    from timeit import timeit

    print("Running benchmarks")
    setup = (
        "from __main__ import count_negatives_binary_search,count_negatives_brute_force"
        ",count_negatives_brute_force_with_break,grid"
    )
    for func in (
        "count_negatives_binary_search",  # 175.51 seconds
        "count_negatives_brute_force_with_break",  # 271.04 seconds
        "count_negatives_brute_force",  # 646.65 seconds
    ):
        time = timeit(f"{func}(grid=grid)", setup=setup, number=500)
        print(f"{func}() took {time} seconds")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    benchmark()
