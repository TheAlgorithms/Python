"""
Just to check
"""


def add(a, b):
    """
    >>> add(2, 2)
    4
    >>> add(2, -2)
    0
    """
    return a + b

def sum_fun(a, b):
    l = []
    l.append(a)
    l.append(b)
    return sum(l)

if __name__ == "__main__":
    a = 5
    b = 6
    print(f"The sum of {a} + {b} is {add(a, b)}")
    print(f"The sum of {a} + {b} using sum function is {sum_fun(a, b)}")