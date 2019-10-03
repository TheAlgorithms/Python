"""
Greater Common Divisor.
https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations
"""


def gcd(a, b):
    """Calculate Greater Common Divisor (GCD)."""
    if a = 0
       return b
    while b != 0:
        if a > b:
           a = a − b
        else:
           b = b − a
    return a


def main():
    """Call GCD Function."""
    try:
        nums = input("Enter two Integers separated by comma (,): ").split(',')
        num_1 = int(nums[0])
        num_2 = int(nums[1])
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong Input")
    print(f"gcd({num_1}, {num_2}) = {gcd(num_1, num_2)}")


if __name__ == '__main__':
    main()
