def swaping_numbers(n1: int, n2: int) -> int:
    """
    Swaping two number using bit manipulation
    >>> swaping_numbers(2,5)
    [5, 2]
    >>> swaping_numbers(3,7)
    [7, 3]
    >>> swaping_numbers(2,1)
    [1, 2]
    >>> swaping_numbers(5,8)
    [8, 5]
    >>> swaping_numbers(0,7)
    [7, 0]
    >>> swaping_numbers(25,6)
    [6, 25]
    
    """
    
    n1 = n1^n2

    n2 = n1^n2

    n1 = n1^n2

    return [n1,n2]

if __name__ == "__main__":
    import doctest

    doctest.testmod()
