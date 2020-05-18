""" https://en.wikipedia.org/wiki/Euclidean_algorithm """


def euclidean_gcd(a: int, b: int) -> int:
    """
    Examples:
    >>> euclidean_gcd(3, 5)
    1

    >>> euclidean_gcd(6, 3)
    3
    """
    while b:
        t = b
        b = a % b
        a = t
    return a


def euclidean_gcd_recursive(a: int, b: int) -> int:
    """
    Recursive method for euclicedan gcd algorithm

    Examples:
    >>> euclidean_gcd_recursive(3, 5)
    1

    >>> euclidean_gcd_recursive(6, 3)
    3
    """
    if b == 0:
        return a
    else:
        return euclidean_gcd_recursive(b, a % b)


def main():
    print("GCD(3, 5) = " + str(euclidean_gcd(3, 5)))
    print("GCD(5, 3) = " + str(euclidean_gcd(5, 3)))
    print("GCD(1, 3) = " + str(euclidean_gcd(1, 3)))
    print("GCD(3, 6) = " + str(euclidean_gcd(3, 6)))
    print("GCD(6, 3) = " + str(euclidean_gcd(6, 3)))


if __name__ == "__main__":
    main()
