# Reeka
def sum_of_ap_series(a: int, d: int, n: int) -> int:
    """
    Calculates the sum of the first 'n' terms of an arithmetic progression (AP)
    series with the first term 'a' and common difference 'd'.

    Parameters:
    a (int): The first term of the AP.
    d (int): The common difference between terms.
    n (int): The number of terms to sum.

    Returns:
    int: The sum of the first 'n' terms of the AP.

    Examples:
    >>> sum_of_ap_series(1, 1, 5)  # Sum of first 5 natural numbers
    15
    >>> sum_of_ap_series(2, 3, 4)  # Sum of 2, 5, 8, 11
    26
    >>> sum_of_ap_series(5, 0, 3)  # Sum of 5, 5, 5
    15
    >>> sum_of_ap_series(1, 2, 1)  # Single term AP series
    1
    >>> sum_of_ap_series(1, -1, 5)  # Decreasing AP series
    -5
    >>> sum_of_ap_series(1, 1, -5)  # Negative 'n' should raise an error
    Traceback (most recent call last):
    ...
    ValueError: Number of terms 'n' must be a positive integer
    >>> sum_of_ap_series(1, 1, 0)  # Zero terms should also raise an error
    Traceback (most recent call last):
    ...
    ValueError: Number of terms 'n' must be a positive integer
    """
    if n <= 0:
        raise ValueError("Number of terms 'n' must be a positive integer")

    # Formula for the sum of an AP series: S_n = n/2 * (2a + (n-1) * d)
    return n * (2 * a + (n - 1) * d) // 2


# Reeka
