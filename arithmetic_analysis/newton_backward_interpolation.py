# https://www.geeksforgeeks.org/newton-forward-backward-interpolation/
import math


# for calculating u value
def ucal(value_of_u: float, value_of_n: int) -> float:
    """
    >>> ucal(1, 2)
    2
    >>> ucal(1.1, 2)
    2.5410000000000004
    >>> ucal(1.2, 2)
    3.168
    """
    temp = value_of_u
    for i in range(value_of_n):
        temp = temp * (value_of_u + i)
    return temp


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    n = int(input("enter the numbers of values: "))
    y: list[list[float]] = []
    for i in range(n):
        y.append([])
    for i in range(n):
        for j in range(n):
            y[i].append(j)
            y[i][j] = 0

    print("enter the values of parameters in a list: ")
    x = list(map(int, input().split()))

    print("enter the values of corresponding parameters: ")
    for i in range(n):
        y[i][0] = float(input())

    value = int(input("enter the value to interpolate: "))
    u = (value - x[n - 1]) / (x[1] - x[0])

    # for calculating forward difference table

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

    summ = y[n - 1][0]
    for i in range(1, n):
        summ += (ucal(u, i) * y[n - 1][i]) / math.factorial(i)

    print(f"the value at {value} is {summ}")
