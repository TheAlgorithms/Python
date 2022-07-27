from collections import Counter


def sock_merchant(colors: list[int]) -> int:
    """
    >>> sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20])
    3
    >>> sock_merchant([1, 1, 3, 3])
    2
    """
    return sum(socks_by_color // 2 for socks_by_color in Counter(colors).values())


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    colors = [int(x) for x in input("Enter socks by color :").rstrip().split()]
    print(f"sock_merchant({colors}) = {sock_merchant(colors)}")
