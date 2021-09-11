def persistence(num: int) -> int:
    """
    Return the persistence of a given number.
    
    https://en.wikipedia.org/wiki/Persistence_of_a_number

    >>> persistence(217)
    2
    >>> persistence(-1)
    Traceback (most recent call last):
        ...
    ValueError: persistence() does not accept negative values
    >>> persistence("long number")
    Traceback (most recent call last):
        ...
    ValueError: persistence() only accepts integral values
    """

    if not isinstance(num, int):
        raise ValueError("persistence() only accepts integral values")
    if num < 0:
        raise ValueError("persistence() does not accept negative values")
    
    steps = 0
    num_string = str(num)
    
    while len(num_string) != 1:
        numbers = [int(i) for i in num_string]

        total = 1
        for i in range(0, len(numbers)):
            total *= numbers[i]

        num_string = str(total)

        steps += 1
    return steps

if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
