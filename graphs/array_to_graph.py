"""
Reference: https://gist.github.com/harigro/28df9ec639f74f217473f85065acf9d8
"""


def divide_array_to_graph(arr: list[int], base: int) -> dict[int, list[int]]:
    """
    >>> divide_array_to_graph(arr=[1, 2, 3, 4, 5, 6, 7, 8], base=2)
    {0: [1, 2], 1: [3, 4], 2: [5, 6], 3: [7, 8]}
    >>> divide_array_to_graph(arr=[1, 2, 3, 4, 5, 6, 7, 8], base=3)
    {0: [1, 2, 3, 4], 1: [5, 6, 7, 8]}
    """
    length = len(arr)
    parts = len(arr) // base  # Desired number of parts
    part_size = length // parts  # Size of each part

    # Divide the array into smaller parts
    result = [arr[i * part_size : (i + 1) * part_size] for i in range(parts)]

    # Insert the result into a dictionary with keys from 0 to 3
    result_dict = {i: result[i] for i in range(parts)}

    return result_dict


if __name__ == "__main__":
    # Example usage
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    print(divide_array_to_graph(array, 2))

    import doctest

    doctest.testmod()
