"""
This program calculates the nth Fibonacci number in O(log n) time complexity.

The fast doubling method leverages mathematical properties of Fibonacci numbers:
- F(2n) = F(n) × [2×F(n+1) - F(n)]
- F(2n+1) = F(n+1)² + F(n)²

These identities allow us to compute F(n) by recursively computing values at n/2,
effectively halving the problem size at each step, similar to binary exponentiation.

Time Complexity: O(log n) - We halve the input at each recursive step
Space Complexity: O(log n) - Recursion stack depth

Performance: Can calculate F(1,000,000) in less than a second!

Example:
    >>> fibonacci(10)
    55
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
"""

from __future__ import annotations

import sys


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using the fast doubling method.
    
    This function computes F(n) where the Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1
    
    Args:
        n (int): The index of the Fibonacci number to compute (must be non-negative).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
        >>> [fibonacci(i) for i in range(13)]
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    """
    if n < 0:
        raise ValueError("Negative arguments are not supported")
    return _fib(n)[0]


def _fib(n: int) -> tuple[int, int]:
    """
    Helper function that returns (F(n), F(n+1)) using fast doubling.
    
    This internal function uses the following mathematical identities:
    - F(2n) = F(n) × [2×F(n+1) - F(n)]
    - F(2n+1) = F(n+1)² + F(n)²
    
    By computing these values recursively at n/2, we achieve O(log n) complexity.
    
    Args:
        n (int): The index for which to compute Fibonacci numbers.
    
    Returns:
        tuple[int, int]: A tuple containing (F(n), F(n+1)).
    
    Examples:
        >>> _fib(0)
        (0, 1)
        >>> _fib(1)
        (1, 1)
        >>> _fib(10)
        (55, 89)
    """
    if n == 0:  # Base case: (F(0), F(1)) = (0, 1)
        return (0, 1)

    # Recursive step: compute (F(n//2), F(n//2+1))
    a, b = _fib(n // 2)
    
    # Apply fast doubling formulas:
    # c = F(2k) where k = n//2
    # d = F(2k+1) where k = n//2
    c = a * (b * 2 - a)
    d = a * a + b * b
    
    # Return (F(n), F(n+1)) based on whether n is even or odd
    return (d, c + d) if n % 2 else (c, d)


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(f"fibonacci({n}) is {fibonacci(n)}")
