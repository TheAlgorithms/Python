"""
== Perfect Number ==
In number theory, a perfect number is a positive integer that is equal to the sum of
its positive divisors, excluding the number itself.

For example: 6 ==> divisors[1, 2, 3, 6]
    Excluding 6, the sum(divisors) is 1 + 2 + 3 = 6
    So, 6 is a Perfect Number

The first few perfect numbers are: 6, 28, 496, 8128, 33550336, ...

https://en.wikipedia.org/wiki/Perfect_number
https://oeis.org/A000396
"""


def perfect(number: int) -> bool:
    """
    Check if a number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper
    divisors (positive divisors excluding the number itself).

    The algorithm finds all divisors up to number//2 (since no proper divisor
    can be greater than half the number) and sums them for comparison.

    Time Complexity: O(sqrt(n)) with optimized divisor finding
    Space Complexity: O(1)

    Args:
        number: The positive integer to be checked.

    Returns:
        True if the number is a perfect number, False otherwise.

    Raises:
        ValueError: If number is not an integer.

    Examples:
        Basic perfect numbers:
        >>> perfect(6)
        True
        >>> perfect(28)
        True
        >>> perfect(496)
        True
        >>> perfect(8128)
        True

        Large perfect number:
        >>> perfect(33550336)
        True

        Non-perfect numbers:
        >>> perfect(12)
        False
        >>> perfect(27)
        False
        >>> perfect(29)
        False
        >>> perfect(100)
        False

        Edge cases:
        >>> perfect(1)
        False
        >>> perfect(2)
        False
        >>> perfect(0)
        False
        >>> perfect(-1)
        False
        >>> perfect(-6)
        False

        Numbers close to perfect numbers:
        >>> perfect(5)
        False
        >>> perfect(7)
        False
        >>> perfect(27)
        False
        >>> perfect(29)
        False
        >>> perfect(495)
        False
        >>> perfect(497)
        False
        >>> perfect(33550335)
        False
        >>> perfect(33550337)
        False

        Type validation:
        >>> perfect(12.34)
        Traceback (most recent call last):
        ...
        ValueError: number must be an integer
        >>> perfect("123")
        Traceback (most recent call last):
        ...
        ValueError: number must be an integer
        >>> perfect("Hello")
        Traceback (most recent call last):
        ...
        ValueError: number must be an integer
        >>> perfect([6])
        Traceback (most recent call last):
        ...
        ValueError: number must be an integer
        >>> perfect(None)
        Traceback (most recent call last):
        ...
        ValueError: number must be an integer

        Testing divisor sum calculation for known cases:
        >>> # For 6: divisors are 1, 2, 3 -> sum = 6
        >>> sum(i for i in range(1, 6//2 + 1) if 6 % i == 0) == 6
        True
        >>> # For 28: divisors are 1, 2, 4, 7, 14 -> sum = 28
        >>> sum(i for i in range(1, 28//2 + 1) if 28 % i == 0) == 28
        True
        >>> # For 12: divisors are 1, 2, 3, 4, 6 -> sum = 16 ≠ 12
        >>> sum(i for i in range(1, 12//2 + 1) if 12 % i == 0) == 12
        False
    """
    if not isinstance(number, int):
        raise ValueError("number must be an integer")

    if number <= 0:
        return False

    # Special case: 1 has no proper divisors
    if number == 1:
        return False

    # Find sum of all proper divisors
    # We only need to check up to number//2 since no proper divisor
    # can be greater than half the number
    divisor_sum = sum(i for i in range(1, number // 2 + 1) if number % i == 0)

    return divisor_sum == number


def perfect_optimized(number: int) -> bool:
    """
    Optimized version of perfect number checker using mathematical properties.

    This version uses the fact that divisors come in pairs (d, n/d) to reduce
    the search space to sqrt(n).

    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)

    Args:
        number: The positive integer to be checked.

    Returns:
        True if the number is a perfect number, False otherwise.

    Examples:
        >>> perfect_optimized(6)
        True
        >>> perfect_optimized(28)
        True
        >>> perfect_optimized(496)
        True
        >>> perfect_optimized(12)
        False
        >>> perfect_optimized(1)
        False
        >>> perfect_optimized(0)
        False
        >>> perfect_optimized(-1)
        False
    """
    if not isinstance(number, int):
        raise ValueError("number must be an integer")

    if number <= 1:
        return False

    divisor_sum = 1  # 1 is always a proper divisor for n > 1

    # Check divisors up to sqrt(number)
    i = 2
    while i * i <= number:
        if number % i == 0:
            divisor_sum += i
            # Add the paired divisor if it's different from i
            if i != number // i:
                divisor_sum += number // i
        i += 1

    return divisor_sum == number


def find_perfect_numbers(limit: int) -> list[int]:
    """
    Find all perfect numbers up to a given limit.

    Args:
        limit: The upper bound to search for perfect numbers.

    Returns:
        List of perfect numbers up to the limit.

    Examples:
        >>> find_perfect_numbers(10)
        [6]
        >>> find_perfect_numbers(30)
        [6, 28]
        >>> find_perfect_numbers(500)
        [6, 28, 496]
        >>> find_perfect_numbers(0)
        []
        >>> find_perfect_numbers(1)
        []
    """
    if not isinstance(limit, int) or limit < 0:
        raise ValueError("limit must be a non-negative integer")

    return [n for n in range(1, limit + 1) if perfect(n)]


def get_divisors(number: int) -> list[int]:
    """
    Get all proper divisors of a number (excluding the number itself).

    Args:
        number: The positive integer to find divisors for.

    Returns:
        List of proper divisors in ascending order.

    Examples:
        >>> get_divisors(6)
        [1, 2, 3]
        >>> get_divisors(28)
        [1, 2, 4, 7, 14]
        >>> get_divisors(12)
        [1, 2, 3, 4, 6]
        >>> get_divisors(1)
        []
        >>> get_divisors(7)
        [1]
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("number must be a positive integer")

    if number == 1:
        return []

    return [i for i in range(1, number // 2 + 1) if number % i == 0]


if __name__ == "__main__":
    from doctest import testmod

    print("Running doctests...")
    testmod(verbose=True)

    print("\nPerfect Number Checker")
    print("=" * 40)
    print("A perfect number equals the sum of its proper divisors.")
    print("Examples: 6 (1+2+3), 28 (1+2+4+7+14), 496, 8128, ...")
    print()

    while True:
        try:
            user_input = input("Enter a positive integer (or 'q' to quit): ").strip()
            if user_input.lower() == "q":
                break

            number = int(user_input)

            if number <= 0:
                print("Please enter a positive integer.")
                continue

            is_perfect = perfect(number)
            divisors = get_divisors(number)
            divisor_sum = sum(divisors)

            print(f"\nNumber: {number}")
            print(f"Proper divisors: {divisors}")
            print(f"Sum of divisors: {divisor_sum}")
            print(f"Is perfect: {'Yes' if is_perfect else 'No'}")

            if is_perfect:
                print(f"✓ {number} is a Perfect Number!")
            else:
                print(f"✗ {number} is not a Perfect Number.")

            print("-" * 40)

        except ValueError as e:
            if "invalid literal" in str(e):
                print("Please enter a valid integer.")
            else:
                print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
