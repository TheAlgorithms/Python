def negative_binary_to_int(negative_binary: int) -> int:
    """
    a conversion algorithm from negative binary
    base to decimal

    https://en.wikipedia.org/wiki/Negative_base#:~:text=Binary-,Negabinary,-Ternary

    >>> negative_binary_to_int(101110)
    -38
    >>> negative_binary_to_int(10111110)
    -150
    >>> negative_binary_to_int(100)
    4
    >>> negative_binary_to_int(110)
    2
    """
    negative_binary_str = str(negative_binary)
    r = negative_binary_str[::-1]
    res = [int(r[c]) * (-2) ** c for c in range(len(r))]
    return sum(res)


if __name__ == "__main__":
    __import__("doctest").testmod()
