def is_k_power_of_n(n: int, k: int) -> bool:
    """
    Given two positive integers, n and k, this function determines if k
    is a power of n. A number k is a power of n if k = n^x for some
    non-negative integer x.

    >>> is_k_power_of_n(2, 8)
    True
    >>> is_k_power_of_n(3, 10)
    False
    >>> is_k_power_of_n(5, 5)
    True
    >>> is_k_power_of_n(10, 1000)
    True
    >>> is_k_power_of_n(4, 2)
    False
    >>> is_k_power_of_n(1, 1)
    True
    >>> is_k_power_of_n(1, 5)
    False
    >>> is_k_power_of_n(0, 16)
    Traceback (most recent call last):
        ...
    ValueError: Both n and k must be positive integers
    >>> is_k_power_of_n(2, -8)
    Traceback (most recent call last):
        ...
    ValueError: Both n and k must be positive integers
    >>> is_k_power_of_n(2, 'a')
    Traceback (most recent call last):
        ...
    TypeError: n and k must be integers
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers")

    if n <= 0 or k <= 0:
        raise ValueError("Both n and k must be positive integers")

    if n == 1:
        return k == 1

    while k % n == 0:
        k //= n
    return k == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
