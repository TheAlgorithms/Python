# Author: Abhijeeth S

import math


def res(x, y):
    """
    This function return the x^y.
    >>> res(3,4)
    81
    >>> res(1,1)
    1
    >>> res(1,0)
    1
    >>> res(0,1)
    0
    >>> res(10,1)
    10
    >>> res(10,2)
    100
    """
    if 0 not in (x, y):
        # We use the relation x^y = y*log10(x), where 10 is the base.
        return y * math.log10(x)
    else:
        if x == 0:  # 0 raised to any number is 0
            return 0
        elif y == 0:
            return 1  # any number raised to 0 is 1


if __name__ == "__main__":  # Main function
    # Read two numbers from input and typecast them to int using map function.
    # Here x is the base and y is the power.
    prompt = "Enter the base and the power separated by a comma: "
    x1, y1 = map(int, input(prompt).split(","))
    x2, y2 = map(int, input(prompt).split(","))

    # We find the log of each number, using the function res(), which takes two
    # arguments.
    res1 = res(x1, y1)
    res2 = res(x2, y2)

    # We check for the largest number
    if res1 > res2:
        print("Largest number is", x1, "^", y1)
    elif res2 > res1:
        print("Largest number is", x2, "^", y2)
    else:
        print("Both are equal")
