def generate_seating_arrangement(n):
    """
    Generates the nth binary sequence where no two '1's are adjacent.
    
    Args:
        n (int): The position of the sequence to retrieve.
    
    Returns:
        str: The nth valid binary sequence.
    
    Examples:
        >>> generate_seating_arrangement(4)
        '101'
        >>> generate_seating_arrangement(6)
        '1001'
        >>> generate_seating_arrangement(9)
        '10001'
    """
    k2 = 2
    k1 = ["0"] * (n + 1)
    k1[1] = "1"
    a1 = 1

    while k2 < (n + 1):
        if k1[a1][-1] == "0":
            k1[k2] = k1[a1] + "0"
            k2 += 1
            if k2 >= (n + 1):
                break
            k1[k2] = k1[a1] + "1"
            k2 += 1
            if k2 >= (n + 1):
                break
            a1 += 1
        elif k1[a1][-1] == "1":
            k1[k2] = k1[a1] + "0"
            k2 += 1
            if k2 >= (n + 1):
                break
            a1 += 1
    return k1[n]

# Doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
