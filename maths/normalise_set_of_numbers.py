from typing import List, Union


def normalize_array(
    arr: List[float], lower_bound: float, upper_bound: float
) -> List[float]:
    """
    Normalize an array to the range [0, 1]
    given the lower and upper bounds.

    Parameters:
        arr (list): Input array of numbers.
        lower_bound (float): Lower bound for normalization.
        upper_bound (float): Upper bound for normalization.

    Returns:
        list: Normalized array.

    Example:
    >>> arr = [10, 20, 30, 40]
    >>> lower_bound = 10
    >>> upper_bound = 40
    >>> normalize_array(arr, lower_bound, upper_bound)
    [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]

    Example 2:
    >>> normalize_array([1,2,3],1,3)
    [0.0, 0.5, 1.0]
    """
    normalized_arr = []
    for num in arr:
        normalized_num = (num - lower_bound) / (upper_bound - lower_bound)
        normalized_arr.append(normalized_num)
    return normalized_arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
