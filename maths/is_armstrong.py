def is_armstrong(n: int) -> bool:
    """
    Check if a number is an Armstrong number.

    An Armstrong number (Narcissistic number) is a number that is equal
    to the sum of its digits each raised to the power of the number of digits.

    Example:
    153 = 1^3 + 5^3 + 3^3
    """

    digits = list(map(int, str(n)))
    num_digits = len(digits)
    return n == sum(d**num_digits for d in digits)


if __name__ == "__main__":
    print(is_armstrong(153))  # True
    print(is_armstrong(370))  # True
    print(is_armstrong(10))  # False
