def subtract(num1: float, num2: float) -> float:
    """
    >>> subtract(2, 1)
    1
    >>> subtract(2,4)
    -2
    """
    return num1 - num2


if __name__ == "__main__":
    num1 = 2
    num2 = 1
    print(f"The difference between {num1} and {num2} is {subtract(num1, num2)}")
