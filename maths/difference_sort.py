def diff(a=int, c=int) -> int:
    """
    Sorting 2 list numbers without same numbers
    >>> diff(6,6)
    Enter 1st list numbers: 1 2 3 6 4 7
    Enter 2nd list numbers: 1 2 36 96 78 99
    Sorted list:
    3
    4
    6
    7
    36
    78
    96
    99
    """
    # Taking input lists
    b = input("Enter 1st list numbers: ").split()
    d = input("Enter 2nd list numbers: ").split()
    # Making set of list
    x = set(b)
    y = set(d)
    # Find numbers which are not same in lists
    p = y.difference(x)
    q = x.difference(y)
    # Make union of 2 lists numbers
    r = p.union(q)
    print("Sorted list: ")
    # Printing numbers in sorted manner
    print("\n".join(sorted(r, key=int)))


if __name__ == "__main__":
    diff(5, 5)
