def fact(n):
    """
    Return 1, if n is 1 or below,
    otherwise, return n * fact(n-1).
    """
    return 1 if n <= 1 else n * fact(n - 1)


"""
Show factorial for i,
where i ranges from 1 to 20.
"""
for i in range(1, 21):
    print(i, ": ", fact(i), sep="")
