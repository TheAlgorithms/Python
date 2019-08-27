"""Absolute Value."""


def abs_val(num):
    """
    Find the absolute value of a number.

    >>abs_val(-5)
    5
    >>abs_val(0)
    0
    """
    if num < 0:
        return -num

    # Returns if number is not < 0
    return num


def main():
    """Print absolute value of -34."""
    print(abs_val(-34))  # = 34


if __name__ == '__main__':
    main()
