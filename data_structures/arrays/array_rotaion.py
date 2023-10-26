# https://www.geeksforgeeks.org/array-rotation/

def rotate_array(input_array, positions_to_rotate):
    """
    Rotate an input array to the right by a specified number of positions.

    Parameters:
    - input_array (list): The input array to be rotated.
    - positions_to_rotate (int): The number of positions to rotate the input array to the right.

    Returns:
    - list: The rotated array.

    >>> rotate_array([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    >>> rotate_array([7, 9, 1, 4, 6], 3)
    [1, 4, 6, 7, 9]
    >>> rotate_array([11, 12, 13, 14, 15], 5)
    [11, 12, 13, 14, 15]
    >>> rotate_array(['a', 'b', 'c', 'd'], 2)
    ['c', 'd', 'a', 'b']
    >>> rotate_array([], 3)
    []
    """

    if not input_array:
        return input_array

    positions_to_rotate = positions_to_rotate % len(input_array)  # Ensure positions_to_rotate is within the array size
    rotated_array = input_array[-positions_to_rotate:] + input_array[:-positions_to_rotate]

    return rotated_array

if __name__ == "__main__":
    import doctest

    doctest.testmod()
