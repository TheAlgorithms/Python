"""
Catalan Numbers

Catalan numbers form a sequence of natural numbers that occur in various counting
problems in combinatorics. The nth Catalan number can be expressed directly in
terms of binomial coefficients.

Formula: C(n) = (2n)! / ((n + 1)! * n!)

Alternative formula: C(n) = C(n-1) * 2(2n-1) / (n+1)

Applications:
- Number of different ways n + 1 factors can be completely parenthesized
- Number of different binary search trees with n keys
- Number of paths with n steps east and n steps north that don't cross diagonal
- Number of ways to triangulate a polygon with n + 2 sides

Reference: https://en.wikipedia.org/wiki/Catalan_number
"""


def catalan_number(node_count: int) -> int:
    """
    Calculate the nth Catalan number using dynamic programming approach.

    Args:
        node_count: A non-negative integer representing the position in sequence

    Returns:
        The nth Catalan number

    Raises:
        ValueError: If node_count is negative

    Examples:
    >>> catalan_number(0)
    1
    >>> catalan_number(1)
    1
    >>> catalan_number(5)
    42
    >>> catalan_number(10)
    16796
    >>> catalan_number(15)
    9694845
    >>> catalan_number(-1)
    Traceback (most recent call last):
        ...
    ValueError: node_count must be a non-negative integer
    >>> catalan_number(3.5)
    Traceback (most recent call last):
        ...
    ValueError: node_count must be a non-negative integer
    """
    if not isinstance(node_count, int) or node_count < 0:
        raise ValueError("node_count must be a non-negative integer")

    if node_count <= 1:
        return 1

    # Dynamic programming approach
    catalan = [0] * (node_count + 1)
    catalan[0] = catalan[1] = 1

    for i in range(2, node_count + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]

    return catalan[node_count]


def catalan_number_recursive(node_count: int) -> int:
    """
    Calculate the nth Catalan number using recursive formula with memoization.

    Args:
        node_count: A non-negative integer representing the position in sequence

    Returns:
        The nth Catalan number

    Raises:
        ValueError: If node_count is negative

    Examples:
    >>> catalan_number_recursive(0)
    1
    >>> catalan_number_recursive(1)
    1
    >>> catalan_number_recursive(5)
    42
    >>> catalan_number_recursive(10)
    16796
    >>> catalan_number_recursive(-1)
    Traceback (most recent call last):
        ...
    ValueError: node_count must be a non-negative integer
    """
    if not isinstance(node_count, int) or node_count < 0:
        raise ValueError("node_count must be a non-negative integer")

    memo: dict[int, int] = {}

    def helper(n: int) -> int:
        if n <= 1:
            return 1
        if n in memo:
            return memo[n]

        result = 0
        for i in range(n):
            result += helper(i) * helper(n - 1 - i)

        memo[n] = result
        return result

    return helper(node_count)


def catalan_number_binomial(node_count: int) -> int:
    """
    Calculate the nth Catalan number using binomial coefficient formula.

    Formula: C(n) = (2n)! / ((n + 1)! * n!)
             which equals: C(2n, n) / (n + 1)

    Args:
        node_count: A non-negative integer representing the position in sequence

    Returns:
        The nth Catalan number

    Raises:
        ValueError: If node_count is negative

    Examples:
    >>> catalan_number_binomial(0)
    1
    >>> catalan_number_binomial(1)
    1
    >>> catalan_number_binomial(5)
    42
    >>> catalan_number_binomial(10)
    16796
    >>> catalan_number_binomial(15)
    9694845
    >>> catalan_number_binomial(-1)
    Traceback (most recent call last):
        ...
    ValueError: node_count must be a non-negative integer
    """
    if not isinstance(node_count, int) or node_count < 0:
        raise ValueError("node_count must be a non-negative integer")

    if node_count <= 1:
        return 1

    # Calculate binomial coefficient C(2n, n)
    result = 1
    for i in range(node_count):
        result = result * (2 * node_count - i) // (i + 1)

    # Divide by (n + 1)
    return result // (node_count + 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Print first 15 Catalan numbers
    print("First 15 Catalan numbers:")
    for i in range(15):
        print(f"C({i}) = {catalan_number(i)}")
