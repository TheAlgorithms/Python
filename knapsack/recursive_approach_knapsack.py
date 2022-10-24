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


def knapsack(weights: list, values: list, n: int, max_weight: int, index: int) -> int:
    """
    Function description is as follows-
    :param weights: Take a list of weights
    :param values: Take a list of profits corresponding to the weights
    :param max_weight: Maximum weight that could be carried
    :param index: the element we are looking at
    :return: Maximum expected gain
    >>> knapsack([1, 2, 4, 5], [5, 4, 8, 6], 4, 15)
    13
    >>> knapsack([3 ,4 , 5], [10, 9 , 8], 3, 25)
    27
    """
    if index == len(weights):
        return 0
    ans1 = 0
    ans2 = 0
    ans1 = knapsack(weights, values, n, max_weight, index + 1)
    if weights[index] <= max_weight:
        ans2 = values[index] + knapsack(
            weights, values, n, max_weight - weights[index], index + 1
        )
    return max(ans1, ans2)


def take_input():
    """
    This function is to take input from the user
    """
    n = int(input("Input number of items: "))

    if n == 0:
        return list(), list(), n, 0

    weights = list(map(int, input("Input weights separated by spaces: ").split(" ")))
    values = list(map(int, input("Input profits separated by spaces: ").split(" ")))
    max_weight = int(input("Max weight allowed: "))

    return weights, values, n, max_weight


if __name__ == "__main__":
    print(
        "Input profits, weights, and then max_weight (all positive ints) separated by "
        "spaces."
    )
    weights, values, n, max_weight = take_input()

    # Function Call
    print(knapsack(weights, values, n, max_weight, 0))
