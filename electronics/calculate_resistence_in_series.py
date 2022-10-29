resistors_in_series = [100, 150, 330]

def calculate_resistence_in_series(resistors_in_series: list) -> float:
    """
    Calculate total resistance of resistors used in series
    
    >>> calculate_resistence_in_series(resistors_in_series)
    580
    """
    total = 0
    for val in resistors_in_series:
        total = total + val
    return total
    
if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
