"""
Subtraction of two numbers
"""


def subtract(a: int, b: int) -> int:
    """
    >>> subtract(2, 2)
    0
    >>> subtract(2, -2)
    4
    """
    return a - b


if __name__ == "__main__":
    a = 5
    b = 6
    print(f"The sum of {a} + {b} is {subtract(a, b)}")
