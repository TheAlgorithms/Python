"""
Greatest Common Divisor (GCD) Program
"""

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculates the Greatest Common Divisor (GCD) using recursion.
    """
    #  Bug fixed: Correct recursive definition
    return abs(a) if b == 0 else greatest_common_divisor(b, a % b)


def gcd_by_iterative(x: int, y: int) -> int:
    """
    Calculates the GCD using an iterative method (more memory efficient).
    """
    while y:
        x, y = y, x % y
    return abs(x)


def main():
    """Main function for user input and output."""
    try:
        nums = input("Enter two integers separated by comma (,): ").split(",")
        num_1 = int(nums[0].strip())
        num_2 = int(nums[1].strip())

        print(f"greatest_common_divisor({num_1}, {num_2}) = {greatest_common_divisor(num_1, num_2)}")
        print(f"gcd_by_iterative({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}")

    except (IndexError, ValueError):
        print(" Invalid input! Please enter two valid integers separated by a comma.")


if __name__ == "__main__":
    main()
