import numpy as np

def pearson_correlation(data_x: np.ndarray, data_y: np.ndarray) -> float:
    """
    Calculate the Pearson correlation coefficient between two sets of data.

    Parameters:
    data_x (np.ndarray): Array of numeric values representing a column of data 
                         that will be compared with another column to determine
                         how strongly the two vectors are related.
    data_y (np.ndarray): Array of numeric values representing the second column 
                         of data to compare with data_x.

    Returns:
    float: Pearson correlation coefficient between data_x and data_y.

    Reference:
    https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

    Example:
    >>> data_x = np.array([1, 2, 3, 4, 5])
    >>> data_y = np.array([2, 4, 6, 8, 10])
    >>> round(pearson_correlation(data_x, data_y), 2)
    1.0
    """
    if len(data_x) != len(data_y):
        raise ValueError("data_x and data_y must have the same length")
    
    n = len(data_x)
    if n == 0:
        return 0.0

    mean_x = np.mean(data_x)
    mean_y = np.mean(data_y)

    numerator = np.sum((data_x - mean_x) * (data_y - mean_y))
    denominator = np.sqrt(np.sum((data_x - mean_x)**2) * np.sum((data_y - mean_y)**2))

    if denominator == 0:
        return 0.0

    return numerator / denominator


if __name__ == "__main__":
    import doctest
    doctest.testmod()
