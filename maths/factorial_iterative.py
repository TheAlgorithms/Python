def factorial_iterative(n: int) -> int:
    """
    Return the factorial of n using an iterative approach.
    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # simple demonstration
    print(factorial_iterative(5))  # expected 120
