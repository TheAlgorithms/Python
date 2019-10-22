"""
Greatest Common Divisor.

Wikipedia reference: https://en.wikipedia.org/wiki/Greatest_common_divisor
"""


def gcd(a, b):
    """
    Calculate Greatest Common Divisor (GCD).
    >>> gcd(24, 40)
    8
    """
    return b if a == 0 else gcd(b % a, a)


"""
Below method is more efficient.
This method is not acquire more memory cause is no use of any stacks(chunk of a memory
space).  While above method is good one but acquire more memory for huge number because
of more recursive call to evaluate GCD.
"""


def gcd_by_iterative(x, y):
    """
    >>> gcd_by_iterative(24, 40)
    8
    >>> gcd(24, 40) == gcd_by_iterative(24, 40)
    True
    """
    while y:  # --> when y=0 then loop will terminate and return x as final GCD.
        x, y = y, x % y
    return x


def main():
    """Call GCD function."""
    try:
        nums = input("Enter two integers separated by comma (,): ").split(",")
        num_1 = int(nums[0])
        num_2 = int(nums[1])
        print(f"gcd({num_1}, {num_2}) = {gcd(num_1, num_2)}")
        print(f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}")
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong input")


if __name__ == "__main__":
    main()
