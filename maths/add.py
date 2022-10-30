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
    a = 5
    b = 6
    print(f"The sum of {a} + {b} is {add(a, b)}")

    
    
    
    
def add3(a: float, b: float, c: float) -> float:
    """
    >>> add(2, 2)
    4
    >>> add(2, -2)
    0
    """
    return a + b + c 


if __name__ == "__main__":
    a = 5
    b = 6
    c = 7
    print(f"The sum of {a} + {b} is {add(a, b)}")
