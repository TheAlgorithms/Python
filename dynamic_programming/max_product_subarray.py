def max_product_subarray(numbers: list[int]) -> int:
    """
    Returns the maximum product that can be obtained by multiplying a
    contiguous subarray of the given integer list `nums`.

    Example:
    >>> max_product_subarray([2, 3, -2, 4])
    6
    >>> max_product_subarray((-2, 0, -1))
    0
    >>> max_product_subarray([2, 3, -2, 4, -1])
    48
    >>> max_product_subarray([-1])
    -1
    >>> max_product_subarray([0])
    0
    >>> max_product_subarray([])
    0
    >>> max_product_subarray("")
    0
    >>> max_product_subarray(None)
    0
    >>> max_product_subarray([2, 3, -2, 4.5, -1])
    Traceback (most recent call last):
        ...
    ValueError: numbers must be an iterable of integers
    >>> max_product_subarray("ABC")
    Traceback (most recent call last):
        ...
    ValueError: numbers must be an iterable of integers
    """
    if not numbers:
        return 0

    if not isinstance(numbers, (list, tuple)) or not all(
        isinstance(number, int) for number in numbers
    ):
        raise ValueError("numbers must be an iterable of integers")

    max_till_now = min_till_now = max_prod = numbers[0]

    for i in range(1, len(numbers)):
        # update the maximum and minimum subarray products
        number = numbers[i]
        if number < 0:
            max_till_now, min_till_now = min_till_now, max_till_now
        max_till_now = max(number, max_till_now * number)
        min_till_now = min(number, min_till_now * number)

        # update the maximum product found till now
        max_prod = max(max_prod, max_till_now)

    return max_prod
