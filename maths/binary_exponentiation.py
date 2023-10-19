"""Binary Exponentiation."""

# Author : Junth Basnet
# Time Complexity : O(logn)


def binary_exponentiation(a: int, n: int) -> int:
    """
    Compute a number raised by some quantity
    >>> binary_exponentiation(-1, 3)
    -1
    >>> binary_exponentiation(-1, 4)
    1
    >>> binary_exponentiation(2, 2)
    4
    >>> binary_exponentiation(3, 5)
    243
    >>> binary_exponentiation(10, 3)
    1000
    >>> binary_exponentiation(5e3, 1)
    5000.0
    >>> binary_exponentiation(-5e3, 1)
    -5000.0
    """
    if n == 0:
        return 1

    elif n % 2 == 1:
        return binary_exponentiation(a, n - 1) * a

    else:
        b = binary_exponentiation(a, n // 2)
        return b * b


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        BASE = int(float(input("Enter Base : ").strip()))
        POWER = int(input("Enter Power : ").strip())
    except ValueError:
        print("Invalid literal for integer")

    RESULT = binary_exponentiation(BASE, POWER)
    print(f"{BASE}^({POWER}) : {RESULT}")
