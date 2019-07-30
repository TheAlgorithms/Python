from .abs import abs_val


def absMin(x):
    """
    >>> absMin([0,5,1,11])
    0
    >>> absMin([3,-10,-2])
    -2
    """
    j = x[0]
    for i in x:
        if abs_val(i) < abs_val(j):
            j = i
    return j


def main():
    a = [-3,-1,2,-11]
    print(absMin(a))  # = -1


if __name__ == '__main__':
    main()