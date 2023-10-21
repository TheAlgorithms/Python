"""
== Perfect Number ==
In number theory, a perfect number is a positive integer that is equal to the sum of
its positive divisors, excluding the number itself.
For example: 6 ==> divisors[1, 2, 3, 6]
    Excluding 6, the sum(divisors) is 1 + 2 + 3 = 6
    So, 6 is a Perfect Number

Other examples of Perfect Numbers: 28, 486, ...

https://en.wikipedia.org/wiki/Perfect_number
"""


def perfect(number: int) -> bool:
    """
    Check if a number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper
    divisors (excluding itself).

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is a perfect number, False otherwise.

    Examples:
    >>> perfect(27)
    False
    >>> perfect(28)
    True
    >>> perfect(29)
    False
    >>> perfect(6)
    True
    >>> perfect(12)
    False
    >>> perfect(496)
    True
    >>> perfect(8128)
    True
    """
    return sum(i for i in range(1, number // 2 + 1) if number % i == 0) == number


if __name__ == "__main__":
    print("Program to check whether a number is a Perfect number or not...")
    number = int(input("Enter number: ").strip())
    print(f"{number} is {'' if perfect(number) else 'not '}a Perfect Number.")
