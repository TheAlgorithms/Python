"""
Karatsuba Multiplication Algorithm
----------------------------------
Given two binary strings that represent the value of two integers,
find the product of the two strings using the Karatsuba algorithm.

Example:
    "1100" (12) x "1010" (10) = 120
"""


def karatsuba_multiply(bin_num1: str, bin_num2: str) -> int:
    """
    Multiply two binary strings using the Karatsuba algorithm.

    Args:
        bin_num1 (str): The first binary string.
        bin_num2 (str): The second binary string.

    Returns:
        int: The product of the two binary strings as an integer.

    Examples:
        >>> karatsuba_multiply("1100", "1010")
        120
        >>> karatsuba_multiply("11", "11")
        9
        >>> karatsuba_multiply("101", "10")
        10
    """
    # Convert binary strings to integers
    x = int(bin_num1, 2)
    y = int(bin_num2, 2)

    # Base case for recursion
    if x < 2 or y < 2:
        return x * y

    # Calculate the size of the numbers
    n = max(len(bin_num1), len(bin_num2))
    half = n // 2

    # Split the binary strings
    x_high = x >> half
    x_low = x & ((1 << half) - 1)
    y_high = y >> half
    y_low = y & ((1 << half) - 1)

    # Recursive multiplications
    a = karatsuba_multiply(bin(x_high)[2:], bin(y_high)[2:])
    d = karatsuba_multiply(bin(x_low)[2:], bin(y_low)[2:])
    e = karatsuba_multiply(bin(x_high + x_low)[2:], bin(y_high + y_low)[2:]) - a - d

    # Combine results
    return (a << (2 * half)) + (e << half) + d


if __name__ == "__main__":
    import doctest

    doctest.testmod()
