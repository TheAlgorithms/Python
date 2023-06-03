def max_sectors_of_circle(num_cuts: float) -> float:
    """
    returns the maximum amount of
    sectors a circle can be divided
    by if cut 'num_cuts' times

    >>> max_sectors_of_circle(54)
    1486.0
    >>> max_sectors_of_circle(7)
    29.0
    >>> max_sectors_of_circle(22.5)
    265.375
    >>> max_sectors_of_circle(-222)
    -1
    """

    return ((num_cuts + 2 + num_cuts**2) * (1 / 2)) if num_cuts >= 0 else -1


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
