"""
https://en.wikipedia.org/wiki/Lucas_number
"""


def recursive_lucas_number(n_th_number: int) -> int:
    """
    Returns the nth lucas number
    >>> recursive_lucas_number(1)
    1
    >>> recursive_lucas_number(20)
    15127
    >>> recursive_lucas_number(0)
    2
    >>> recursive_lucas_number(25)
    167761
    >>> recursive_lucas_number(-1.5)
    Traceback (most recent call last):
        ...
    TypeError: recursive_lucas_number accepts only integer arguments.
    """
    if not isinstance(n_th_number, int):
        raise TypeError("recursive_lucas_number accepts only integer arguments.")
    if n_th_number == 0:
        return 2
    if n_th_number == 1:
        return 1

    return recursive_lucas_number(n_th_number - 1) + recursive_lucas_number(
        n_th_number - 2
    )


def dynamic_lucas_number(n_th_number: int) -> int:
    """
    Returns the nth lucas number
    >>> dynamic_lucas_number(1)
    1
    >>> dynamic_lucas_number(20)
    15127
    >>> dynamic_lucas_number(0)
    2
    >>> dynamic_lucas_number(25)
    167761
    >>> dynamic_lucas_number(-1.5)
    Traceback (most recent call last):
        ...
    TypeError: dynamic_lucas_number accepts only integer arguments.
    """
    if not isinstance(n_th_number, int):
        raise TypeError("dynamic_lucas_number accepts only integer arguments.")
    a, b = 2, 1
    for _ in range(n_th_number):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    n = int(input("Enter the number of terms in lucas series:\n").strip())
    print("Using recursive function to calculate lucas series:")
    print(" ".join(str(recursive_lucas_number(i)) for i in range(n)))
    print("\nUsing dynamic function to calculate lucas series:")
    print(" ".join(str(dynamic_lucas_number(i)) for i in range(n)))
