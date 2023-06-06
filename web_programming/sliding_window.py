def sliding_window(elements, window_size):
    """
    Generate sliding windows of a specified size over a list of elements.

    Args:
        elements (list): The input list of elements.
        window_size (int): The size of the sliding window.

    Returns:
        list: A list of sliding windows.

    Example:
        >>> lst = [1, 2, 3, 4, 5, 6, 7, 8]
        >>> result = sliding_window(lst, 3)
        >>> print(result)
        [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]
    """

    if len(elements) <= window_size:
        return [elements]

    windows = []
    for i in range(len(elements) - window_size + 1):
        window = elements[i:i+window_size]
        windows.append(window)

    return windows

if __name__ == "__main__":
    import doctest

    doctest.testmod()