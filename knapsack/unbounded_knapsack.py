'''
Unbounded knapsack is much similar to 0/1 knapsack.
But, in unbounded knapsack repetition of item is allowed (that is, we can pick the same item more than one time).
This is not the case in 0/1 knapsack, where we have choice to pick or not pick the item, and one item can be picked only once.

The main idea of this algorithm is to maximize the total profit by picking all the items that fits into total capacity of the bag.
'''

def knapSack(W, wt, val, n):
    '''
    Function description is as follows-
    :param W: Maximun weight that the bag can hold
    :param wt: list of weight
    :param val: list of profits
    :param n: length of val list
    :return: Returns the maximum value that can be put in a knapsack of capacity 'W'

    >>> knapSack(50, [10, 20, 30], [60, 100, 120], 3)
    300
    '''

    # We initialize the matrix with 0 at first.
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):

            # base condition
            # if the capacity 'W'==0 or array is empty
            # return 0 (i.e, store zero in K[i][w])
            if i == 0 or w == 0:
                K[i][w] = 0

            # if the weight of current item is less than 'W'
            # we have choice to add it to bag more than once or not add it to bag
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i][w-wt[i-1]],  K[i-1][w])   # we can pick the same item multiple times so, K[i][w-wt[i-1]]
            
            # if the weight of current item is greater than 'W'
            # we can't pick that item, so we move to pick next item in the list.
            else:
                K[i][w] = K[i-1][w]

    # the final answer (i.e, profit) will
    # be stored in K[-1][-1] 
    return K[-1][-1]


# Driver code
if __name__ == "__main__":
    val = [60, 100, 120]  # value array (i.e, profit)
    wt = [10, 20, 30]  # weight array
    W = 50  # total capacity the bag can hold

    n = len(val)
    print(knapSack(W, wt, val, n)) 
