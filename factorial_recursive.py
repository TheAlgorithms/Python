def factorial(n: int) -> int:
    """Return factorial of a given number n using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))  # Output: 120
