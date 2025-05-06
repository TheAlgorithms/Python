def power(base: float, exponent: int) -> float:
    """
    Optimized power function using exponentiation by squaring.

    Args:
        base (float): The base number.
        exponent (int): The exponent.

    Returns:
        float: The result of base raised to the power of exponent.

    Examples:
        >>> power(2, 3)
        8.0
        >>> power(5, -2)
        0.04
        >>> power(10, 0)
        1.0
        >>> power(7, 2)
        49.0
        >>> power(2, -3)
        0.125
        >>> power(2.5, 4)
        39.0625
        >>> power(-3.5, 2)
        12.25
        >>> power(-2, 3)
        -8.0
        >>> power(0, 5)
        0.0
        >>> power(0, 0)
        1.0
        >>> power(0, -1)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: 0.0 cannot be raised to a negative power.
        >>> power(1, 1000)
        1.0

    """
    result = 1.0
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    while exponent:
        if exponent % 2 == 1:
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
