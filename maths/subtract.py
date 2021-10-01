def subtract(a, b):
    """
    >>> subtract(3, 2)
    1
    >>> subtract(2, -2)
    4
    """
    return a - b


if __name__ == "__main__":
    a = 6
    b = 5
    print(f"The difference of of {a} and {b} is {subtract(a, b)}")
