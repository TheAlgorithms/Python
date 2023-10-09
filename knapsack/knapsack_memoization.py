"""
A shopkeeper has bags of wheat that each have different weights and different profits.
eg.
no_of_items : 5
profit [15, 14,10,45,30]
weight [2,5,1,3,4]
max_weight that can be carried : 7

Constraints:
    max_weight > 0
    profit[i] >= 0
    weight[i] >= 0

Calculate:
     The maximum profit that the shopkeeper can make given maxmum weight that can
be carried.

This problem is implemented here with MEMOIZATION method using the concept of
Dynamic Programming
"""
"""
for more information visit https://en.wikipedia.org/wiki/Memoization
"""


def knapsack(
    values: list, weights: list, num_of_items: int, max_weight: int, dp: list
) -> int:
    """
    Function description is as follows-
    :param weights: Take a list of weights
    :param values: Take a list of profits corresponding to the weights
    :param number_of_items: number of items available to pick from
    :param max_weight: Maximum weight that could be carried
    :param dp: it is a list of list, i.e, a table whose (i,j)
                cell represents the maximum profit earned
                for i items and j as the maximum weight allowed, it
                is an essential part for implementing this problem
                using memoization dynamic programming
    :return: Maximum expected gain

    Testcase 1:
    >>> values = [1, 2, 4, 5]
    >>> wt = [5, 4, 8, 6]
    >>> n = len(values)
    >>> w = 5
    >>> dp = [[-1 for x in range(w+1)] for y in range(n+1)]
    >>> knapsack(values,wt,n,w,dp)
    2

    Testcase 2:
    >>> values = [3 ,4 , 5]
    >>> wt = [10, 9 , 8]
    >>> n = len(values)
    >>> w = 25
    >>> dp = [[-1 for x in range(w+1)] for y in range(n+1)]
    >>> knapsack(values,wt,n,w,dp)
    9

    Testcase 3:
    >>> values = [15, 14,10,45,30]
    >>> wt = [2,5,1,3,4]
    >>> n = len(values)
    >>> w = 7
    >>> dp = [[-1 for x in range(w+1)] for y in range(n+1)]
    >>> knapsack(values,wt,n,w,dp)
    75
    """
    # no profit gain if any of these two become zero
    if max_weight == 0 or num_of_items == 0:
        dp[num_of_items][max_weight] = 0
        return 0
    # if this case is previously encountered => maximum gain for this case is already
    elif dp[num_of_items][max_weight] != -1:
        # in dp table
        return dp[num_of_items][max_weight]

    # if the item can be included in the bag
    elif weights[num_of_items - 1] <= max_weight:
        # ans1 stores the maximum profit if the item at
        #  index num_of_items -1 is included in the bag
        incl = knapsack(
            values,
            weights,
            num_of_items - 1,
            max_weight - weights[num_of_items - 1],
            dp,
        )
        ans1 = values[num_of_items - 1] + incl
        # ans2 stores the maximum profit if the item at
        # index num_of_items -1 is not included in the bag
        ans2 = knapsack(values, weights, num_of_items - 1, max_weight, dp)
        # the final answer is the maximum profit gained from any of ans1 or ans2
        dp[num_of_items][max_weight] = max(ans1, ans2)
        return dp[num_of_items][max_weight]

    # if the item's weight exceeds the max_weight of the bag
    #  => it cannot be included in the bag
    else:
        dp[num_of_items][max_weight] = knapsack(
            values, weights, num_of_items - 1, max_weight, dp
        )
        return dp[num_of_items][max_weight]


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="knapsack", verbose=True)
