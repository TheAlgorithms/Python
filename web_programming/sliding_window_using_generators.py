def sliding_window(elements, window_size):
    """
    Generate sliding windows of size window_size from the given elements.

    Args:
        elements (list): The input list of elements.
        window_size (int): The size of the sliding window.

    Returns:
        generator: A generator that yields sublists of size window_size.

    Example:
        >>> lst = [1, 2, 3, 4, 5, 6, 7, 8]
        >>> sw_gen = sliding_window(lst, 3)
        >>> print(next(sw_gen))
        [1, 2, 3]
        >>> print(next(sw_gen))
        [2, 3, 4]
        
    References:
    https://stackoverflow.com/questions/8269916/what-is-sliding-window-algorithm-examples    
    """
    if len(elements) <= window_size:
        return elements
    for i in range(len(elements) - window_size + 1):
        yield elements[i:i + window_size]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
