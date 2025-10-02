import numpy as np


def pearson_correlation(data_x: np.ndarray, data_y: np.ndarray) -> float:
    """
    Calculate the Pearson correlation coefficient (PCC) between two arrays.

    Pearson correlation measures the linear relationship between two datasets,
    returning a value between -1 and 1:
      - 1   indicates a perfect positive linear correlation
      - 0   indicates no linear correlation
      - -1  indicates a perfect negative linear correlation

    Formula:
    r = Σ((x - mean(x)) * (y - mean(y))) / sqrt(Σ(x - mean(x))^2 * Σ(y - mean(y))^2)

    Reference: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

    Parameters:
    - x: 1D numpy array of values
    - y: 1D numpy array of values

    Returns:
    - The Pearson correlation coefficient (float)

      a = np.array([1, 2, 3, 4, 5])
      b = np.array([2, 4, 6, 8, 10])
      float(np.round(pearson_correlation(a, b), 5))
    1.0
      a = np.array([1, 2, 3, 4, 5])
      b = np.array([10, 9, 2, 6, 4])
      float(np.round(pearson_correlation(a, b), 5))
    -0.18845
      a = np.array([1, 2, 3])
      b = np.array([1, 2])
      pearson_correlation(a, b)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same length.
    """
    if len(data_x) != len(data_y):
        raise ValueError("Input arrays must have the same length.")

    x_mean = np.mean(data_x)
    y_mean = np.mean(data_y)

    numerator = np.sum((data_x - x_mean) * (data_y - y_mean))
    denominator = np.sqrt(np.sum((data_x - x_mean) ** 2) * np.sum((data_y - y_mean) ** 2))

    if denominator == 0:
        raise ValueError("Standard deviation of input arrays must not be zero.")

    return numerator / denominator
