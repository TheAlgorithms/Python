def max_product_subarray(numbers: list[int]) -> int:
    """
    Returns the maximum product that can be obtained by multiplying a
    contiguous subarray of the given integer list `nums`.

    Example:
    >>> max_product_subarray([2, 3, -2, 4])
    6
    >>> max_product_subarray([-2, 0, -1])
    0
    >>> max_product_subarray([2, 3, -2, 4, -1])
    48
    >>> max_product_subarray([2, 3, -2, 4.5, -1])
    54
    >>> max_product_subarray([-1])
    -1
    >>> max_product_subarray([])
    0
    >>> max_product_subarray("ABC")
    0
    >>> max_product_subarray("")
    0
    >>> max_product_subarray(None)
    0
    """
    if numbers is None or not isinstance(numbers, list):
        return 0

    n = len(numbers)

    if n == 0:
        return 0

    if not all(isinstance(x, int) for x in numbers):
        return 0

    max_till_now = numbers[0]
    min_till_now = numbers[0]
    max_prod = numbers[0]

    for i in range(1, n):
        # update the maximum and minimum subarray products
        if numbers[i] < 0:
            max_till_now, min_till_now = min_till_now, max_till_now
        max_till_now = max(numbers[i], max_till_now * numbers[i])
        min_till_now = min(numbers[i], min_till_now * numbers[i])

        # update the maximum product found till now
        max_prod = max(max_prod, max_till_now)

    return max_prod
