# Python code to print Pascal's triangle of given size N. 
# Input: N
# Output: Triangle. 
# Created on Fri Apr 10 01:11:44 2020

def pascals_triangle(N):
    """Prints the elements of the Pascal Triangle
    >>> p = pascals_triangle(5)
    >>> print_pascals_triangle(p)
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    """
    a = []
    for i in range(N):
        a.append([])
        a[i].append(1)
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if i != 0:
            a[i].append(1)
    return a


def print_pascals_triangle(a):
    """Prints the elements of the Pascal Triangle
    >>> p = pascals_triangle(5)
    >>> print_pascals_triangle(p)
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    """
    for i in a:
        print(' '.join(map(str,i)))


def main():
    from doctest import testmod

    testmod()
    N = 7
    p = pascals_triangle(N)
    print_pascals_triangle(p)


if __name__ == "__main__":
    main()