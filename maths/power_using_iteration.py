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
    return round(result, 5)  # Round to 5 decimal places


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
