"""
Greatest Common Divisor.
Wikipedia reference: https://en.wikipedia.org/wiki/Greatest_common_divisor
gcd(a, b) = gcd(a, -b) = gcd(-a, b) = gcd(-a, -b) by definition of divisibility
"""


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor (GCD) using Euclidean algorithm recursively.

    The GCD of two integers is the largest positive integer that divides both numbers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The greatest common divisor of a and b

    Examples:
        Basic cases:
        >>> greatest_common_divisor(24, 40)
        8
        >>> greatest_common_divisor(48, 18)
        6
        >>> greatest_common_divisor(100, 25)
        25
        >>> greatest_common_divisor(17, 19)
        1

        Edge cases with small numbers:
        >>> greatest_common_divisor(1, 1)
        1
        >>> greatest_common_divisor(1, 800)
        1
        >>> greatest_common_divisor(11, 37)
        1
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(16, 4)
        4

        Cases with zero:
        >>> greatest_common_divisor(0, 5)
        5
        >>> greatest_common_divisor(5, 0)
        5
        >>> greatest_common_divisor(0, 0)
        0

        Negative numbers:
        >>> greatest_common_divisor(-3, 9)
        3
        >>> greatest_common_divisor(9, -3)
        3
        >>> greatest_common_divisor(3, -9)
        3
        >>> greatest_common_divisor(-3, -9)
        3
        >>> greatest_common_divisor(-24, -40)
        8
        >>> greatest_common_divisor(-48, 18)
        6

        Large numbers:
        >>> greatest_common_divisor(1071, 462)
        21
        >>> greatest_common_divisor(12345, 54321)
        3

        Same numbers:
        >>> greatest_common_divisor(42, 42)
        42
        >>> greatest_common_divisor(-15, -15)
        15

        One divides the other:
        >>> greatest_common_divisor(15, 45)
        15
        >>> greatest_common_divisor(7, 49)
        7
    """
    return abs(b) if a == 0 else greatest_common_divisor(b % a, a)


def gcd_by_iterative(x: int, y: int) -> int:
    """
    Calculate Greatest Common Divisor (GCD) using iterative Euclidean algorithm.

    This method is more memory efficient because it does not create additional
    stack frames for recursive function calls.

    Args:
        x: First integer
        y: Second integer

    Returns:
        The greatest common divisor of x and y

    Examples:
        Basic cases:
        >>> gcd_by_iterative(24, 40)
        8
        >>> gcd_by_iterative(48, 18)
        6
        >>> gcd_by_iterative(100, 25)
        25
        >>> gcd_by_iterative(17, 19)
        1

        Verify equivalence with recursive version:
        >>> greatest_common_divisor(24, 40) == gcd_by_iterative(24, 40)
        True
        >>> greatest_common_divisor(48, 18) == gcd_by_iterative(48, 18)
        True
        >>> greatest_common_divisor(100, 25) == gcd_by_iterative(100, 25)
        True

        Edge cases with small numbers:
        >>> gcd_by_iterative(1, 1)
        1
        >>> gcd_by_iterative(1, 800)
        1
        >>> gcd_by_iterative(11, 37)
        1
        >>> gcd_by_iterative(16, 4)
        4

        Cases with zero:
        >>> gcd_by_iterative(0, 5)
        5
        >>> gcd_by_iterative(5, 0)
        5
        >>> gcd_by_iterative(0, 0)
        0

        Negative numbers:
        >>> gcd_by_iterative(-3, -9)
        3
        >>> gcd_by_iterative(3, -9)
        3
        >>> gcd_by_iterative(-3, 9)
        3
        >>> gcd_by_iterative(1, -800)
        1
        >>> gcd_by_iterative(-24, -40)
        8
        >>> gcd_by_iterative(-48, 18)
        6

        Large numbers:
        >>> gcd_by_iterative(1071, 462)
        21
        >>> gcd_by_iterative(12345, 54321)
        3

        Same numbers:
        >>> gcd_by_iterative(42, 42)
        42
        >>> gcd_by_iterative(-15, -15)
        15

        One divides the other:
        >>> gcd_by_iterative(15, 45)
        15
        >>> gcd_by_iterative(7, 49)
        7
    """
    while y:  # --> when y=0 then loop will terminate and return x as final GCD.
        x, y = y, x % y
    return abs(x)


def main():
    """
    Call Greatest Common Divisor function with user input.

    Prompts user for two integers separated by comma and calculates their GCD
    using both recursive and iterative methods.

    Examples:
        This function handles user input, so direct doctests aren't practical.
        However, it should handle valid input like "24,40" and invalid input gracefully.
    """
    try:
        nums = input("Enter two integers separated by comma (,): ").split(",")
        num_1 = int(nums[0])
        num_2 = int(nums[1])
        print(
            f"greatest_common_divisor({num_1}, {num_2}) = "
            f"{greatest_common_divisor(num_1, num_2)}"
        )
        print(f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}")
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong input")


if __name__ == "__main__":
    main()
