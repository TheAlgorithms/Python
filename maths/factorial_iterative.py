"""
Factorial using Iteration
Time Complexity: O(n)
Space Complexity: O(1)
"""

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(factorial(5))
