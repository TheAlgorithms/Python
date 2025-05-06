"""
Iterative solution to calculate the power of a base raised to an exponent.

This implementation uses an iterative approach, unlike the recursive approach
in `power_using_recursion.py`. The algorithm is based on exponentiation by squaring
for optimal performance.

Examples:
    >>> power(2, 3)
    8
    >>> power(5, -2)
    0.04
    >>> power(10, 0)
    1
    >>> Failed example:
        power(5, -2)
        Expected:
            0.04
        Got:
            0.04000000000000001
        1 items had failures:
        1 of   3 in __main__
        1 failed in total
    Raise base to the power of exponent using an optimized approach...
    Enter the base: 500
    Enter the exponent: 8
    500.0 to the power of 8 is 3.90625e+21

Input:
    base (float): The base number (can be integer or float).
    exponent (int): The exponent (can be positive, negative, or zero).

Output:
    float: The result of base raised to the power of exponent.

Note:
    Results for very large or very small floating-point numbers may have slight precision errors
    due to the limitations of floating-point arithmetic.
"""


def power(base: float, exponent: int) -> float:
    """
    Optimized power function using exponentiation by squaring.
    It handles both positive and negative exponents efficiently.
    This function take time complexity O(log n) for exponentiation.
    space complexity is O(1) as it uses a constant amount of space.
    """
    # Handle negative exponents by taking reciprocal of the base
    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    result = 1
    # Use exponentiation by squaring for efficiency
    while exponent:
        if exponent % 2 == 1:  # If the current exponent is odd
            result *= base
        base *= base  # Square the base
        exponent //= 2  # Halve the exponent
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("Raise base to the power of exponent using an optimized approach...")

    try:
        # Input handling and validation
        base = float(input("Enter the base: ").strip())  # Supports float & int
        exponent = int(
            input("Enter the exponent: ").strip()
        )  # Ensures exponent is an integer

        # Calculate result
        result = power(base, exponent)

        # Display the result
        print(f"{base} to the power of {exponent} is {result}")

    except ValueError:
        # Handle invalid input
        print("Invalid input! Please enter numeric values for base and exponent.")
