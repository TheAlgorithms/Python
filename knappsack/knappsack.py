from typing import List


# A naive recursive implementation of 0-1 Knapsack Problem

def knapsack(capacity: int, weights: List[int], value: List[int], counter) -> int:
    """
    Returns the maximum value that can be put in a knapsack of a capacity,
    whereby each weight has a specific value.

    >>> capactiy = 50
    >>> values = [60, 100, 120]
    >>> weights = [10, 20, 30]
    >>> counter = len(values)
    >>> print(knapsack(capactiy, weights, values, counter))
    50

    The result is 50 cause the values of 100 and 120 got the weight of 50
    which is the limit of the capacity.
    """

    # Base Case
    if counter == 0 or capacity == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity,
    #   then this item cannot be included in the optimal solution,
    # else return the maximum of two cases:
    #   (1) nth item included
    #   (2) not included
    if weights[counter - 1] > capacity:
        return knapsack(capacity, weights, value, counter - 1)
    else:
        left_capacity = capacity - weights[counter - 1]
        new_value_included = value[counter - 1] + knapsack(left_capacity, weights, value, counter - 1)
        without_new_value = knapsack(capacity, weights, value, counter - 1)
        return max(new_value_included, without_new_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
