def is_armstrong(number: int) -> bool:
    """
    Check if a number is an Armstrong number.

    >>> is_armstrong(153)
    True
    >>> is_armstrong(123)
    False
    """
    digits = list(map(int, str(number)))
    power = len(digits)
    return sum(d**power for d in digits) == number


if __name__ == "__main__":
    print(is_armstrong(153))
