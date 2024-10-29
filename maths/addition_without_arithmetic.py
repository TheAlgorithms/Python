def add(first: int, second: int) -> int:
    """
    Add two integers using bitwise operations.

    Examples:
    >>> add(3, 5)
    8
    >>> add(13, 5)
    18
    >>> add(-7, 2)
    -5
    >>> add(0, -7)
    -7
    >>> add(-321, 0)
    -321
    """
    while second != 0:
        carry = first & second       # Calculate carry
        first = first ^ second       # Add without carry
        second = carry << 1          # Prepare carry for next iteration
    return first

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    first = int(input("Enter the first number: ").strip())
    second = int(input("Enter the second number: ").strip())
    print(f"The sum is: {add(first, second)}")
