def fibonacci_iterative(term_index: int) -> int:
    """
    Return the Fibonacci number at a given index using an iterative approach.

    Parameters:
        term_index (int): Index in the Fibonacci sequence. Must be a non-negative integer.

    Returns:
        int: The Fibonacci number at the specified index.

    Examples:
    >>> fibonacci_iterative(0)
    0
    >>> fibonacci_iterative(1)
    1
    >>> fibonacci_iterative(7)
    13
    """
    if term_index < 0:
        raise ValueError("term_index must be a non-negative integer.")

    if term_index <= 1:
        return term_index

    prev, curr = 0, 1
    for _ in range(2, term_index + 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    print(fibonacci_iterative(7))  # expected 13

