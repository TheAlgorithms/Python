"""Prime Adam Int Check"""
import math


def prime_check(number: int) -> bool:
    """
    A number is prime if it has exactly two dividers: 1 and itself.
    Example : 2, 3, 5, 7
    """
    if number < 2:
        # Numbers less than 2 are not prime.
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        # If the number has more than 2 dividers, it is not a prime numbe.
        if number % i == 0:
            return False
    # If the number doesnot have more than 2 dividers it is a prime number.
    return True


def prime_adam_check(number: int) -> bool:
    """
    Check if a number is Prime Adam Integer.

    A number is prime adam integer if it is a Prime number as well as Adam number.

    A number is Adam if the square of the number and
    square of the reverse of the number are reverseof each other.
    Example : 13 (13^2 and 31^2 are reverse of each other).
    """

    # Check if the number is Prime.
    if prime_check(number):
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
    print("Program to check whether a number is a Prime Adam Int or not...")
    number = int(input("Enter number: ").strip())
    print(f"{number} is {'' if prime_adam_check(number) else 'not '}a Prime Adam Int.")
