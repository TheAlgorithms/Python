"""
Greatest Common Divisor.

Wikipedia reference: https://en.wikipedia.org/wiki/Greatest_common_divisor
"""


def greatest_common_divisor(a, b):
    """
    Calculate Greatest Common Divisor (GCD).
    >>> greatest_common_divisor(24, 40)
    8
    """
    return b if a == 0 else greatest_common_divisor(b % a, a)


"""
Below method is more memory efficient because it does not use the stack (chunk of memory).
While above method is good, uses more memory for huge numbers because of the recursive calls
required to calculate the greatest common divisor.
"""


def gcd_by_iterative(x, y):
    """
    >>> gcd_by_iterative(24, 40)
    8
    >>> greatest_common_divisor(24, 40) == gcd_by_iterative(24, 40)
    True
    """
    while y:  # --> when y=0 then loop will terminate and return x as final GCD.
        x, y = y, x % y
    return x


def main():
    """Call Greatest Common Divisor function."""
    try:
        nums = input("Enter two integers separated by comma (,): ").split(",")
        num_1 = int(nums[0])
        num_2 = int(nums[1])
        print(f"greatest_common_divisor({num_1}, {num_2}) = {greatest_common_divisor(num_1, num_2)}")
        print(f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}")
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong input")


if __name__ == "__main__":
    main()
