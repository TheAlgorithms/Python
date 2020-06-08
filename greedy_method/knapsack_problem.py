# To get an insight into Greedy Algorithm
# Knapsack is a common Greedy Algo problem


"""
You have bags of wheat with different weights and a different profits for each.
eg.
profit 5 8 7 1 12 3 4
weight 2 7 1 6 4  2 5
max_Weight 100
Calculate the max profit the shopkeeper can make for the given max_Weight that could be carried.
"""

# Importing copy module for deepcopy operations
import copy


def calc_Profit(profit: list, weight: list, max_Weight: int) -> int:
    """
    Function description is as follows-
    :param profit: Take a list of profits
    :param weight: Take a list of weight if bags corresponding to the profits
    :param max_Weight: Max. weight that could be carried
    :return: Max expected gain

    >>> calc_Profit([1,2,3], [3,4,5], 15)
    6
    >>> calc_Profit([10, 9 , 8], [3 ,4 , 5], 25)
    27

    """

    # List created to store profit gained for the 1kg in case of each weight
    # respectively
    profit_By_Weight = list()

    # Calculate and append profit/weight for each
    for i in range(len(weight)):
        profit_By_Weight.append(profit[i] / weight[i])

    # Creating a copy of the list and sorting proit/weight in ascending order
    temp_PBW = sorted(copy.deepcopy(profit_By_Weight))

    # declaring useful variables
    length = len(temp_PBW)
    limit = 0
    gain = 0
    i = 0

    # loop till the total weight do not reach max limit i.e. 15 kg and till i<l
    while limit <= 15 and i < length:

        # flag value for encountered greatest element in temp_PBW
        flag = temp_PBW[length - i - 1]
        """
        calculating index of the same flag in profit_By_Weight list.
        This will give the index of the first encountered element which is same as of flag.
        There may be one or more values same as that of flag but .index always encounter the very first element only.
        To curb this alter the values in profit_By_Weight once they are used Here it is done to -1
        because neither profit nor weight can be in negative.
        """
        index = profit_By_Weight.index(flag)
        profit_By_Weight[index] = -1

        # check if the weight encountered is less than the total weight
        # encountered before.
        if 15 - limit >= weight[index]:

            limit += weight[index]
            # Adding profit gained for the given weight 1 ===
            # weight[index]/weight[index]
            gain += 1 * profit[index]

        else:
            # Since the weight encountered is greater than limit, therefore take the required number of remaining kgs
            # and calculate profit for it.
            # weight remaining/ weight[index]
            gain += ((15 - limit) / weight[index]) * profit[index]
            break
        i += 1

    return gain


if __name__ == "__main__":

    # Input profit, weight and max_Weight (all positive values).

    profit = [int(x) for x in input().split()]
    weight = [int(x) for x in input().split()]
    max_Weight = int(input())

    if len(profit) != len(weight):
        print("The length of both the arrays must be same! Try again!")

    if max_Weight < 0:
        print("Gotcha! Weight is a positive quantity")

    for i in range(len(profit)):
        if (profit[i] or weight[i]) < 0:
            print("Ono! Input positive values only! Better luck next time")
            break
        else:
            calc_Profit(profit, weight, max_Weight)
