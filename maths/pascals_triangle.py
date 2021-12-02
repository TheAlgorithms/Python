"""
Pascal's Triangle is a triangular array that tabulates the result of binomial 
expansions. The nth row of the triangle can be thought of as the coefficients 
for a binomial expression raised to the power of x.
		
e.g. (a + b)^3 --> 1 (a^3) + 3 (a^2b) + 3 (ab^2) + 1 (b^3) --> 1 3 3 1,
which is equivalent to the third row of pascal's triangle.

More information is available at: https://en.wikipedia.org/wiki/Pascal%27s_triangle
"""

from typing import List


def pascals_triangle_row(n: int) -> List[int]:
    """
    Compute the nth row of Pascal's Triangle using the binomial theorem.

    Each row n can be represented as a binomial expression raised to the power n.
    Each value is therefore the binomial coefficient of its index. This value can be
    found using the combinations formula (alternatively called C(N, k) or nCk) where 
    N is the row number and k is the current index.

    So, triangle[n][k] = C(n, k) = n! / k! (n-k)!, which applies for each index k in row n.

    This can be further simplified by computing each value dynamically from the previous 
    value. This is done by multiplying each value by (N-k) / (k+1) to find the next value:

    C(N, 0) = 1
    C(N, 1) = N / 1
    C(N, 2) = (N)(N-1) / 1*2
    C(N, 3) = (N)(N-1)(N-2) / 1*2*3

    This pattern is generalized as C(N, k+1) = C(N, k) * (N-k) / (k+1)

    More information is available at:
    https://en.wikipedia.org/wiki/Pascal%27s_triangle#Calculating_a_row_or_diagonal_by_itself
    https://en.wikipedia.org/wiki/Binomial_theorem

    >>> pascals_triangle_row(0)
    [1]
    >>> pascals_triangle_row(5)
    [1, 5, 10, 10, 5, 1]
    >>> pascals_triangle_row(-1)
    Traceback (most recent call last):
    ...
    ValueError: n cannot be less than zero
    """

    if n < 0:
        raise ValueError("n cannot be less than zero")

    row = [0 for i in range(n + 1)]

    row[0] = 1
    row[-1] = 1

    for k in range(n // 2):
        index_val = row[k] * (n - k) // (k + 1)

        row[k + 1] = index_val
        row[n - k - 1] = index_val

    return row


def pascals_triangle_total(rows: int) -> List[List[int]]:
    """
    Compute all of pascal's triangle up to the given depth by summing the
    two values immediately above each index. Note that depth is zero-indexed,
    so calculating 5 rows will return rows 0 through 5, inclusive.

    >>> pascals_triangle_total(0)
    [[1]]
    >>> pascals_triangle_total(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> pascals_triangle_total(-1)
    Traceback (most recent call last):
    ...
    ValueError: The size of Pascal's Triangle cannot be a negative number
    """

    if rows < 0:
        raise ValueError("The size of Pascal's Triangle cannot be a negative number")
    elif rows == 0:
        return [[1]]

    # make the total number of rows zero-indexed
    rows += 1

    # initialize an empty triangle with the top two layers filled
    triangle = [[0 for i in range(d)] for d in range(1, rows + 1)]
    triangle[0] = [1]
    triangle[1] = [1, 1]

    for d in range(2, rows):

        triangle[d][0] = 1
        triangle[d][-1] = 1

        # compute the value at each index by summing the two numbers in the row above it
        for i in range(1, d):
            triangle[d][i] = triangle[d - 1][i] + triangle[d - 1][i - 1]

    return triangle


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    [print(r) for r in pascals_triangle_total(10)]
