def subtract(a: float, b: float) -> float:
    """
    >>> subtract(2, 1)
    1
    >>> subtract(2,4)
    -2
    """
    return a - b


if __name__ == "__main__":
    a = 2
    b = 1
    print(f"The difference between {a} and {b} is {subtract(a, b)}")
