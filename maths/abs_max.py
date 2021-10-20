def abs_max(x: list[int]) -> int:
        
    '''
    >> abs_max([-8, 5, -13, 9])
    -13
    >> abs_max([10, 0, 12, -1])
    12
    >>> abs_max([])
    Traceback (most recent call last):
    ValueError: abs_max() arg is an empty sequence
        
    ''' 
        
    if len(x) == 0:
        raise ValueError("abs_max() arg is an empty sequence")
    j = x[0]
    for i in x:
        if abs(i) > abs(j):
            j = i
    return j


def main():
    a = [-8, 5, 2, -1, -14]
    print(abs_max(a))  # abs_max = -14


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()
