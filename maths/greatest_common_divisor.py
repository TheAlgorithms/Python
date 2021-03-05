"""
Greatest Common Divisor.

Wikipedia reference: https://en.wikipedia.org/wiki/Greatest_common_divisor

gcd(a, b) = gcd(a, -b) = gcd(-a, b) = gcd(-a, -b) by definition of divisibility
"""


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor (GCD).
    >>> greatest_common_divisor(24, 40)
    8
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
    >>> greatest_common_divisor(-3, 9)
    3
    >>> greatest_common_divisor(9, -3)
    3
    >>> greatest_common_divisor(3, -9)
    3
    >>> greatest_common_divisor(-3, -9)
    3
    """
    return abs(b) if a == 0 else greatest_common_divisor(b % a, a)


def gcd_by_iterative(x: int, y: int) -> int:
    """
    Below method is more memory efficient because it does not create additional
    stack frames for recursive functions calls (as done in the above method).
    >>> gcd_by_iterative(24, 40)
    8
    >>> greatest_common_divisor(24, 40) == gcd_by_iterative(24, 40)
    True
    >>> gcd_by_iterative(-3, -9)
    3
    >>> gcd_by_iterative(3, -9)
    3
    >>> gcd_by_iterative(1, -800)
    1
    >>> gcd_by_iterative(11, 37)
    1
    """
    while y:  # --> when y=0 then loop will terminate and return x as final GCD.
        x, y = y, x % y
    return abs(x)


def main():
    """
    Call Greatest Common Divisor function.
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
