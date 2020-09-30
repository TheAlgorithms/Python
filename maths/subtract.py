"""
Just to check
"""


def subtract(a, b):
    """
    >>> subtract(5, 3)
    2
    >>> subtract(7, -3)
    10
    >>> subtract(-8, -3)
    -5
    """
    return a - b


if __name__ == "__main__":
    a = 100
    b = 50
    print(f"The subtraction of {a} - {b} is {subtract(a, b)}")
