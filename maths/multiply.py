"""
Just to check
"""


def multiply(a, b):
    """
    >>> multiply(6, 4)
    24
    >>> multiply(2, -5)
    -10
    >>> multiply(-20, -5)
    -100
    """
    return a * b


if __name__ == "__main__":
    a = 100
    b = 50
    print(f"The multiplication of {a} x {b} is {multiply(a, b)}")
