"""Adam Integer Check"""


def prime_adam_check(number: int) -> bool:
    """
    Check if a number is Adam Integer.

    A number is Adam if the square of the number and square
    of the reverse of the number are reverse of each other.
    Example : 11 (11^2 and 11^2 are reverse of each other).

    >>> prime_adam_check(14)
    False
    >>> prime_adam_check(13)
    True
    """

    # Get the square of the number.
    square = str(number * number)
    # Get the reverse of th number
    reverse = int(str(number)[::-1])
    # Get the square of reverse of the number.
    square_reverse = str(reverse * reverse)
    # Check if square and square_reverse are reverse of each other.
    if square == square_reverse[::-1]:
        return True
    return False


if __name__ == "__main__":
    print("Program to check whether a number is an Adam Int or not...")
    number = int(input("Enter number: ").strip())
    print(f"{number} is {'' if prime_adam_check(number) else 'not '}an Adam Int.")
