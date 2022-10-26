"""README, Author - Prasansha Satpathy(mailto:prasansha.satpathy@gmail.com)
Requirements:
  - scikit-fuzzy
  - numpy
  - matplotlib
Python:
  - 3.10
"""
import math as mt

import matplotlib.pyplot as plt


def singleton_membership(c: int) -> None:
    plt.stem(c, 1)
    plt.show()


def triangular_membership(a: int, b: int, c: int) -> None:
    """
    inputs : a,b,c
    triangular membership function with the end of plot is just c+5
    """
    list_, x_list = [], []

    x = c + 5
    for i in range(x):
        x_list.append(i)

        if i <= a:
            list_.append(0)

        elif i >= a and i <= b:
            list_.append(int((i - a) / (b - a)))

        elif i >= b and i <= c:
            list_.append(int((c - i) / (c - b)))

        elif i >= c:
            list_.append(0)

    plt.plot(x_list, list_)
    plt.show()


def trapezoidal_membership(a: int, b: int, c: int, d: int) -> None:
    """
    inputs : a, b, c, d
    trapezoidal_membership function with plot between 0 to d+5

    The shape of the membership function depends on the relative values of b and c.
    - When c is greater than b, the resulting membership function is trapezoidal.
    - When b is equal to c, the resulting membership function is equivalent to a
    triangular membership function with parameters [a b d].
    """
    x = d + 5
    x_list = []
    list_ = []

    for i in range(x):
        x_list.append(i)

        if i <= a:
            list_.append(0)

        elif i >= a and i <= b:
            list_.append(int((i - a) / (b - a)))

        elif i >= b and i <= c:
            list_.append(1)

        elif i >= c and i <= d:
            list_.append(int((d - i) / (d - c)))

        elif i >= d:
            list_.append(0)

    plt.plot(x_list, list_)
    plt.show()


def guassian_membership(c: int, s: int, m: int) -> None:
    """
    c : centre (analogous to  mean in statistics)
    s : width (analogous to )
    m : fuzzification factor
    The range we took was from 0 to 10*c
    """
    list_ = []
    x_list = []

    for i in range(0, 10 * (c)):
        x_list.append(i)
        list_.append(int(mt.exp(-0.5 * (((i - c) / (s)) ** m))))

    plt.plot(x_list, list_)
    plt.show()


if __name__ == "__main__":
    print("singleton_membership plottings:c")
    c = 10  # int(input())
    singleton_membership(c)

    print("triangular_membership plottings:a,b,c")
    a = 10  # int(input())
    b = 20  # int(input())
    c = 30  # int(input())
    triangular_membership(a, b, c)

    print("trapezoidal_membership plottings:a,b,c,d")
    a = 10  # int(input())
    b = 20  # int(input())
    c = 30  # int(input())
    d = 40  # int(input())
    trapezoidal_membership(a, b, c, d)

    print("guassian_membership plottings:c,s,m")
    c = 10  # int(input("centre"))
    s = 5  # int(input("width"))
    m = 2  # int(input("fuzzification factor"))
    guassian_membership(c, s, m)
