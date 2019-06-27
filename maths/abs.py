"""Absolute Value."""


def absVal(num):
    """
    Find the absolute value of a number.

    >>absVal(-5)
    5
    >>absVal(0)
    0
    """
    if num < 0:
        return -num
    else:
        return num


def main():
    """Print absolute value of -34."""
    print(absVal(-34))  # = 34


if __name__ == '__main__':
    main()
