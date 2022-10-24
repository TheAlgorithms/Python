# To get an insight into naive recursive way to solve the Knapsack problem


"""
A shopkeeper has bags of wheat that each have different weights and different profits.
eg.
no_of_items 4
profit 5 4 8 6
weight 1 2 4 5
max_weight 5
Constraints:
max_weight > 0
profit[i] >= 0
weight[i] >= 0
Calculate the maximum profit that the shopkeeper can make given maxmum weight that can
be carried.
"""


def knapsack(
    weights: list, values: list, number_of_items: int, max_weight: int, index: int
) -> int:
    """
    Function description is as follows-
    :param weights: Take a list of weights
    :param values: Take a list of profits corresponding to the weights
    :param number_of_items: number of items available to pick from
    :param max_weight: Maximum weight that could be carried
    :param index: the element we are looking at
    :return: Maximum expected gain
    >>> knapsack([1, 2, 4, 5], [5, 4, 8, 6], 4, 5, 0)
    13
    >>> knapsack([3 ,4 , 5], [10, 9 , 8], 3, 25, 0)
    27
    """
    if index == number_of_items:
        return 0
    ans1 = 0
    ans2 = 0
    ans1 = knapsack(weights, values, number_of_items, max_weight, index + 1)
    if weights[index] <= max_weight:
        ans2 = values[index] + knapsack(
            weights, values, number_of_items, max_weight - weights[index], index + 1
        )
    return max(ans1, ans2)


if __name__ == "__main__":

    import doctest

    doctest.testmod()
