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
        a, b = b, a % b
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
    return a if b == 0 else euclidean_gcd_recursive(b, a % b)


def main():
    print(f"euclidean_gcd(3, 5) = {euclidean_gcd(3, 5)}")
    print(f"euclidean_gcd(5, 3) = {euclidean_gcd(5, 3)}")
    print(f"euclidean_gcd(1, 3) = {euclidean_gcd(1, 3)}")
    print(f"euclidean_gcd(3, 6) = {euclidean_gcd(3, 6)}")
    print(f"euclidean_gcd(6, 3) = {euclidean_gcd(6, 3)}")

    print(f"euclidean_gcd_recursive(3, 5) = {euclidean_gcd_recursive(3, 5)}")
    print(f"euclidean_gcd_recursive(5, 3) = {euclidean_gcd_recursive(5, 3)}")
    print(f"euclidean_gcd_recursive(1, 3) = {euclidean_gcd_recursive(1, 3)}")
    print(f"euclidean_gcd_recursive(3, 6) = {euclidean_gcd_recursive(3, 6)}")
    print(f"euclidean_gcd_recursive(6, 3) = {euclidean_gcd_recursive(6, 3)}")


if __name__ == "__main__":
    main()
