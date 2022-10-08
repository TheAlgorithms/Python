"""
Illustrate how to add the integer without arithmetic operation
Author: suraj Kumar
Time Complexity: 1
https://en.wikipedia.org/wiki/Bitwise_operation
"""


def add(first: int, sec: int) -> int:  # Create a function
    """
    implementation of addition of integer
    :param first: int
    :param sec: int
    :return: int
    Examples:
    >>> add(3,5)
    8
    >>> add(13,5)
    18
    """
    while sec != 0:

        c = first & sec

        first = first ^ sec

        sec = c << 1
    return first


if __name__ == "__main__":
    first = int(input("Enter the number for first: "))
    sec = int(input("Enter the number for sec: "))
    import doctest

    doctest.testmod()
    
    # print("Sum of two numbers", add(first, sec))
    # Display sum of two numbers
