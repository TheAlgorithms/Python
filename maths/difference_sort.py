def diff(b: list, d: list) -> list:
    """
    Sorting 2 list numbers without same numbers
    >>> diff([1, 2, 3, 6, 4, 7], [1, 2, 36, 96, 78, 99])
    [3, 4, 6, 7, 36, 78, 96, 99]
    """
    # Making set of list
    x = set(b)
    y = set(d)
    # Find numbers which are not same in lists
    p = y.difference(x)
    q = x.difference(y)
    # Make union of 2 lists numbers
    r = p.union(q)
    r = list(r)
    r.sort()
    return r


if __name__ == "__main__":
    diff(5, 5)
