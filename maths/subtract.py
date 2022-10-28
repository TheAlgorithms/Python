def subtraction(minuend: float, subtrahend: float) -> float:
    """
    Calculate the difference of two numbers.
    Subtraction is an arithmetic operation that represents
    the operation of removing objects from a collection.

    Source:
        https://en.wikipedia.org/wiki/Subtraction

    Parameters:
        minuend (float): The number it is subtracted from
        subtrahend (float): The number being subtracted


    Returns:
        The difference between two numbers

    >>> subtraction(10, 5)
    5
    >>> subtraction(5, 10)
    -5
    >>> subtraction(10.5, 5.5)
    5.0
    >>> subtraction(5.5, 10.5)
    -5.0
    >>> subtraction(10, 0)
    10
    >>> subtraction(0, 10)
    -10
    >>> subtraction(-5, 10)
    -15
    >>> subtraction(10, -5)
    15
    >>> subtraction(-5, -5)
    0
    >>> subtraction(0, 0)
    0
    """
    return minuend - subtrahend


if __name__ == "__main__":
    minuend = 5
    subtrahend = 6
    print(
        f"The difference of {minuend} - {subtrahend}"
        f"is {subtraction(minuend, subtrahend)}"
    )
