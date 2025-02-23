def fibonacci(n, method="iterative"):
    """
    Compute the Fibonacci number using the specified method.

    Parameters:
    - n (int): The nth Fibonacci number to calculate.
    - method (str): The method to use ("iterative", "recursive", "memoized").

    Returns:
    - int: The nth Fibonacci number.
    """

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Iterative Approach (Default)
    if method == "iterative":
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    # Recursive Approach
    elif method == "recursive":
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fibonacci(n - 1, "recursive") + fibonacci(n - 2, "recursive")

    # Memoized Approach
    elif method == "memoized":
        memo = {}

        def fib_memo(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                return n
            memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
            return memo[n]

        return fib_memo(n)

    else:
        raise ValueError("Invalid method. Choose 'iterative', 'recursive', or 'memoized'.")


# Example Usage:
if __name__ == "__main__":
    print(fibonacci(10))                # Default (iterative)
    print(fibonacci(10, "recursive"))   # Recursive method
    print(fibonacci(10, "memoized"))    # Memoized method
