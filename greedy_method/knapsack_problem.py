# To get an insight into Greedy Algorithm
# Knapsack is a common Greedy Algo problem


"""
You have bags of wheat with different weights and a different profits for each.
eg.
profit 5 8 7 1 12 3 4
weight 2 7 1 6 4  2 5
max_Weight 100

Constraints:
max_Weight > 0
profit[i] >= 0
weight[i] >= 0
Calculate the max profit the shopkeeper can make for the given max_Weight that could be carried.
"""
from typing import Union


def calc_profit(profit: list, weight: list, max_Weight: int) -> Union[str, int]:
    """
    Function description is as follows-
    :param profit: Take a list of profits
    :param weight: Take a list of weight if bags corresponding to the profits
    :param max_Weight: Max. weight that could be carried
    :return: Max expected gain

    >>> calc_profit([1,2,3], [3,4,5], 15)
    6
    >>> calc_profit([10, 9 , 8], [3 ,4 , 5], 25)
    27
    """
    if len(profit) != len(weight):
        raise IndexError(
            "<< The length of both the arrays must be same! Try again.. >>"
        )

    if max_Weight <= 0:
        raise ValueError(
            "<< Gotcha! max_Weight is a positive quantity greater than zero! >>"
        )

    for i in range(len(profit)):
        if profit[i] < 0:
            raise ValueError(
                "<< Ono! Profit means positive value. Better luck next time! >>"
            )

        if weight[i] < 0:
            raise ValueError(
                "<< Oops! Could not accept a negative value for weight. Try Again.. >>"
            )

    # List created to store profit gained for the 1kg in case of each weight
    # respectively
    profit_By_Weight = list()

    # Calculate and append profit/weight for each element
    profit_By_Weight = [p / w for p, w in zip(profit, weight)]

    # Creating a copy of the list and sorting profit/weight in ascending order
    temp_PBW = sorted(profit_By_Weight)

    # declaring useful variables
    length = len(temp_PBW)
    limit = 0
    gain = 0
    i = 0

    # loop till the total weight do not reach max limit e.g. 15 kg and till i<length
    while limit <= max_Weight and i < length:

        # flag value for encountered greatest element in temp_PBW
        flag = temp_PBW[length - i - 1]
        """
        Calculating index of the same flag in profit_By_Weight list.
        This will give the index of the first encountered element which is same as of flag.
        There may be one or more values same as that of flag but .index always encounter the
        very first element only.
        To curb this alter the values in profit_By_Weight once they are used Here it is done to -1
        because neither profit nor weight can be in negative.
        """
        index = profit_By_Weight.index(flag)
        profit_By_Weight[index] = -1

        # check if the weight encountered is less than the total weight
        # encountered before.
        if max_Weight - limit >= weight[index]:

            limit += weight[index]
            # Adding profit gained for the given weight 1 ===
            # weight[index]/weight[index]
            gain += 1 * profit[index]

        else:
            # Since the weight encountered is greater than limit, therefore take the required number of
            # remaining kgs
            # and Calculate profit for it.
            # weight remaining/ weight[index]
            gain += ((max_Weight - limit) / weight[index]) * profit[index]
            break
        i += 1

    return gain


if __name__ == "__main__":

    # Input profit, weight and max_Weight (all positive values).

    profit = [int(x) for x in input().split()]
    weight = [int(x) for x in input().split()]
    max_Weight = int(input("Max weight allowed: "))

    # Function Call
    calc_profit(profit, weight, max_Weight)
