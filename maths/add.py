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
    a = int(input())
    b = int(input())
    print(f"The sum of {a} + {b} is {add(a, b)}")
