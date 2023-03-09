"""
Just to check
"""


def add(a: float, b: float) -> float:
    """
    >>> add(2, 2)
    4
    >>> add(2, -2)
    0
    """
    return a + b


if __name__ == "__main__":
    a = float(input("Enter the first value to be added: ))
    b = float(input("Enter the second value to be added: ))
    print(f"The sum of {a} + {b} is {add(a, b)}")
