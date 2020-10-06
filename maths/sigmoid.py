# This is a sigmoid function
# x i function sigmoid is function variable
# a is the gain
import math


def sigmoid(x, a):

    """
    >>> sigmoid(0.5, 1)
    0.6224593312018546
    >>> add(2, 0.5)
    0.7310585786300049
    """
    p = math.exp(-a * x)
    return 1 / (1 + p)


def main():
    # enter values of gain and x
    x = 2
    gain = 0.5
    print(sigmoid(x, gain))


if __name__ == "__main__":
    main()
