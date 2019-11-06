# Lucas Sequence Using Recursion


def recur_luc(n):
    """
    >>> recur_luc(1)
    1
    >>> recur_luc(0)
    2
    """
    if n == 1:
        return n
    if n == 0:
        return 2
    return recur_luc(n - 1) + recur_luc(n - 2)


if __name__ == "__main__":
    limit = int(input("How many terms to include in Lucas series:"))
    print("Lucas series:")
    for i in range(limit):
        print(recur_luc(i))
