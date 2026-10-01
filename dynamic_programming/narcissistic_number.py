"""
Find all narcissistic numbers up to a given limit using dynamic programming.

A narcissistic number (also known as an Armstrong number or plus perfect number)
is a number that is the sum of its own digits each raised to the power of the
number of digits.

For example, 153 is a narcissistic number because 153 = 1^3 + 5^3 + 3^3.

This implementation uses dynamic programming with memoization to efficiently
compute digit powers and find all narcissistic numbers up to a specified limit.

The DP optimization caches digit^power calculations. When searching through many
numbers, the same digit power calculations occur repeatedly (e.g., 153, 351, 135
all need 1^3, 5^3, 3^3). Memoization avoids these redundant calculations.

Examples of narcissistic numbers:
    Single digit: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    Three digit: 153, 370, 371, 407
    Four digit: 1634, 8208, 9474
    Five digit: 54748, 92727, 93084

Reference: https://en.wikipedia.org/wiki/Narcissistic_number
"""


def find_narcissistic_numbers(limit: int) -> list[int]:
    """
    Find all narcissistic numbers up to the given limit using dynamic programming.

    This function uses memoization to cache digit power calculations, avoiding
    redundant computations across different numbers with the same digit count.

    Args:
        limit: The upper bound for searching narcissistic numbers (exclusive)

    Returns:
        list[int]: A sorted list of all narcissistic numbers below the limit

    Examples:
        >>> find_narcissistic_numbers(10)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> find_narcissistic_numbers(160)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153]
        >>> find_narcissistic_numbers(400)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371]
        >>> find_narcissistic_numbers(1000)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
        >>> find_narcissistic_numbers(10000)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]
        >>> find_narcissistic_numbers(1)
        [0]
        >>> find_narcissistic_numbers(0)
        []
    """
    if limit <= 0:
        return []

    narcissistic_nums = []

    # Memoization: cache[(power, digit)] = digit^power
    # This avoids recalculating the same power for different numbers
    power_cache: dict[tuple[int, int], int] = {}

    def get_digit_power(digit: int, power: int) -> int:
        """Get digit^power using memoization (DP optimization)."""
        if (power, digit) not in power_cache:
            power_cache[(power, digit)] = digit**power
        return power_cache[(power, digit)]

    # Check each number up to the limit
    for number in range(limit):
        # Count digits
        num_digits = len(str(number))

        # Calculate sum of powered digits using memoized powers
        remaining = number
        digit_sum = 0
        while remaining > 0:
            digit = remaining % 10
            digit_sum += get_digit_power(digit, num_digits)
            remaining //= 10

        # Check if narcissistic
        if digit_sum == number:
            narcissistic_nums.append(number)

    return narcissistic_nums


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Demonstrate the dynamic programming approach
    print("Finding all narcissistic numbers up to 10000:")
    print("(Using memoization to cache digit power calculations)")
    print()

    narcissistic_numbers = find_narcissistic_numbers(10000)
    print(f"Found {len(narcissistic_numbers)} narcissistic numbers:")
    print(narcissistic_numbers)
